### ☁️ Pipeline Automatizado de Ingesta Serverless (GCP & Data Engineering)
Solución de arquitectura en la nube diseñada para optimizar, centralizar y automatizar el flujo de ingesta de reportes mensuales de causas y expedientes emitidos por los diferentes juzgados del **Poder Judicial de San Juan**.

---

## 🗺️ Diagrama Lógico de la Arquitectura Cloud
[ Juzgados de San Juan ] 
       │
       ▼ (Carga de Reporte Mensual .csv)
 ┌──────────────┐
 │ Cloud Storage│  <--- Event Trigger: google.storage.object.finalize
 └──────┬───────┘
        │
        ▼ (Activación Síncrona en milisegundos)
 ┌─────────────────┐
 │ Cloud Functions │  <--- Procesamiento en Python / Limpieza en Memoria con Pandas
 └──────┬──────────┘
        │
        ▼ (Streaming Ingestion Job / Apache Arrow)
 ┌──────────────┐
 │   BigQuery   │  <--- Data Warehouse Analítico Estructurado
 └──────────────┘

---

## 🛠️ Tecnologías e Infraestructura Implementada
*   **Google Cloud Storage (GCS):** Repositorio seguro de almacenamiento de objetos (Buckets) configurado con políticas de control de acceso para la recepción de archivos planos `CSV`.
*   **Google Cloud Functions (FaaS):** Entorno de ejecución serverless activado mediante eventos nativos de almacenamiento (`object.finalize`), permitiendo el procesamiento inmediato de la información sin mantener servidores encendidos de forma ociosa.
*   **Google BigQuery (Data Warehouse):** Almacén analítico masivo escalable donde se aloja el histórico consolidado de expedientes judiciales para consultas de auditoría interna y Business Intelligence.
*   **Python, Pandas & PyArrow:** Engine de software encargado del parsing de bytes, filtrado relacional de registros íntegros (Data Cleaning) y optimización de streams binarios hacia los clústeres relacionales de Google Cloud.

## 🚀 Impacto Operativo Institucional
1.  **Automatización Total (Mano de obra cero):** El personal del juzgado solo necesita arrastrar el reporte generado al bucket. El sistema se encarga de estructurar e impactar las métricas de forma transparente en segundos.
2.  **Blindaje y Calidad de Datos:** Filtrado estricto programático que descarta datos corruptos o filas nulas en el número de expediente antes de guardarse permanentemente.
3.  **Eficiencia de Costos:** Al basarse en componentes Serverless, el Poder Judicial no paga por servidores dedicados mensuales; la infraestructura solo consume recursos durante los segundos que dura el procesamiento del archivo plano.
