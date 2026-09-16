import pandas as pd
import json
df = pd.read_csv("causas_judiciales_sanjuan.csv")
df.to_json("datos_judiciales_completos.json", orient="records", force_ascii=False, indent=4)
print("Generada lista cruda de 1000 expedientes.")

def generar_analitica_judicial():
    # 1. Cargar el dataset generado
    df = pd.read_csv("causas_judiciales_sanjuan.csv")
    
    # 2. Calcular KPIs Generales
    total_causas = int(df.shape[0])
    en_tramite = int(df[df["Estado_Causa"] == "En Trámite"].shape[0])
    resueltas = int(df[df["Estado_Causa"] == "Resuelto"].shape[0])
    promedio_dias = round(float(df["Dias_Activo"].mean()), 1)
    
    # 3. Distribución de causas por Fuero (para gráfico de torta/barras)
    por_fuero = df["Fuero"].value_counts().to_dict()
    
    # 4. Estado de causas por Fuero (para gráfico de barras apiladas)
    estado_por_fuero = df.groupby(["Fuero", "Estado_Causa"]).size().unstack(fill_value=0).to_dict(orient="index")
    
    # 5. Promedio de días activo por Tipo de Proceso
    dias_por_proceso = df.groupby("Tipo_Proceso")["Dias_Activo"].mean().round(1).to_dict()
    
    # 6. Estructurar el JSON final
    analitica_json = {
        "kpis": {
            "total_causas": total_causas,
            "en_tramite": en_tramite,
            "resueltas": resueltas,
            "promedio_dias_resolucion": promedio_dias
        },
        "graficos": {
            "causas_por_fuero": por_fuero,
            "estados_por_fuero": estado_por_fuero,
            "dias_por_proceso": dias_por_proceso
        }
    }
    
    # 7. Guardar archivo listo para el Frontend
    with open("datos_judiciales.json", "w", encoding="utf-8") as f:
        json.dump(analitica_json, f, ensure_ascii=False, indent=4)
        
    print("✔️ Pipeline completado. 'datos_judiciales.json' generado para el Frontend.")

if __name__ == "__main__":
    generar_analitica_judicial()