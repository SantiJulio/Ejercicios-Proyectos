import functions_framework
import pandas as pd
from google.cloud import storage
from google.cloud import bigquery
import io

# Inicializamos los clientes globales de Google Cloud
storage_client = storage.Client()
bigquery_client = bigquery.Client()

@functions_framework.cloud_event
def procesar_reporte_judicial(cloud_event):
    """
    Cloud Function activada por Event Trigger (GCS).
    Se ejecuta automáticamente en milisegundos cuando cae un CSV en el Bucket.
    """
    data = cloud_event.data
    bucket_name = data["bucket"]
    file_name = data["name"]
    
    print(f"📦 Nuevo reporte detectado en GCP Storage: {file_name} (Bucket: {bucket_name})")
    
    # 1. Conectarse al Bucket y descargar el archivo CSV a la memoria (Serverless)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    contenido_bytes = blob.download_as_bytes()
    
    # 2. Pipeline de Limpieza y Transformación con Pandas
    try:
        # Convertimos los bytes en un DataFrame de Pandas
        df = pd.read_csv(io.BytesIO(contenido_bytes), encoding="utf-8")
        
        # Filtro de Calidad de Datos: Removemos filas sin número de expediente
        df_limpio = df.dropna(subset=["Nro_Expediente"])
        
        # Auditoría de Ingesta: Agregamos columna con la fecha de procesamiento en la nube
        df_limpio["Fecha_Ingesta_Cloud"] = pd.to_datetime('now').strftime('%Y-%m-%d %H:%M:%S')
        
        print(f"🧹 Data Cleaning exitoso. Registros válidos a procesar: {len(df_limpio)}")
        
    except Exception as e:
        print(f"❌ Error crítico procesando la estructura del CSV: {str(e)}")
        return

    # 3. Streaming Ingestion hacia el Data Warehouse de BigQuery
    # Estructura de tabla simulada en la nube para el Poder Judicial
    dataset_id = "poder_judicial_sanjuan"
    table_id = "historico_causas"
    table_ref = bigquery_client.dataset(dataset_id).table(table_id)
    
    # Configuración del Job de Ingesta en la Base de Datos Analítica
    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_APPEND", # Agrega los nuevos datos al histórico existente
        autodetect=True                   # Detecta automáticamente el tipo de dato de las columnas
    )
    
    try:
        # Enviamos la carga estructurada a la nube de BigQuery
        job = bigquery_client.load_table_from_dataframe(df_limpio, table_ref, job_config=job_config)
        job.result() # Esperamos que se complete la operación en los clusters de GCP
        
        print(f"🚀 pipeline Completado Exitosamente. Datos impactados en BigQuery ({dataset_id}.{table_id}).")
        
    except Exception as e:
        print(f"❌ Error de persistencia insertando en BigQuery Warehouse: {str(e)}")