import csv
import random
from datetime import datetime, timedelta

def generar_dataset_judicial(filename="causas_judiciales_sanjuan.csv", total_registros=1000):
    fueros_juzgados = {
        "Penal (Colegio de Jueces)": ["Sala I", "Sala II", "Sala III", "Unidad Conclusiva de Causas"],
        "Civil, Comercial y Minería": ["1° Juzgado Civil", "2° Juzgado Civil", "3° Juzgado Civil", "4° Juzgado Civil"],
        "Laboral": ["1° Juzgado Laboral", "2° Juzgado Laboral", "3° Juzgado Laboral"],
        "Familia": ["1° Juzgado de Familia", "2° Juzgado de Familia"]
    }
    
    estados = ["En Trámite", "Resuelto", "Archivado", "Para Sentencia", "Suspendido"]
    tipos_proceso = ["Amparo", "Daños y Perjuicios", "Despido", "Homicidio", "Hurto", "Divorcio", "Sucesorio"]
    
    fecha_fin_rango = datetime.now()
    fecha_inicio_rango = fecha_fin_rango - timedelta(days=365 * 3) # Últimos 3 años

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Cabeceras del Pipeline de Datos
        writer.writerow([
            "Nro_Expediente", "Fuero", "Juzgado_Radicacion", 
            "Tipo_Proceso", "Fecha_Inicio", "Estado_Causa", "Dias_Activo"
        ])
        
        for i in range(1, total_registros + 1):
            anio_exp = random.randint(2023, 2026)
            nro_exp = f"{random.randint(1000, 99999)}/{str(anio_exp)[2:]}"
            
            fuero = random.choice(list(fueros_juzgados.keys()))
            juzgado = random.choice(fueros_juzgados[fuero])
            tipo = random.choice(tipos_proceso)
            estado = random.choice(estados)
            tiempo_aleatorio = random.random()
            fecha_inicio = fecha_inicio_rango + timedelta(seconds=int(tiempo_aleatorio * (fecha_fin_rango - fecha_inicio_rango).total_seconds()))
            
            if estado in ["Resuelto", "Archivado"]:
                dias_activo = random.randint(30, 400)
            else:
                dias_activo = (fecha_fin_rango - fecha_inicio).days
                
            writer.writerow([
                nro_exp, fuero, juzgado, tipo, 
                fecha_inicio.strftime('%Y-%m-%d'), estado, max(0, dias_activo)
            ])
            
    print(f"✔️ Dataset exitosamente generado: '{filename}' con {total_registros} registros.")

if __name__ == "__main__":
    generar_dataset_judicial()