import streamlit as st
import re

# Configuración de la página
st.set_page_config(
    page_title="Anonimizador Judicial AI",
    page_icon="⚖️",
    layout="wide"
)

# Estilo personalizado (Colores institucionales azul/gris)
st.markdown("""
    <style>
    .main-title { color: #1E3A8A; font-size: 32px; font-weight: bold; margin-bottom: 20px; }
    .subtitle { color: #4B5563; font-size: 18px; margin-bottom: 30px; }
    </style>
""", unsafe_allow_html=True)

def anonimizar_texto_judicial(texto: str) -> str:
    """
    Procesa y enmascara datos sensibles en documentos judiciales 
    mediante un motor algorítmico de patrones y expresiones regulares.
    """
    texto_anon = texto
    
    # 1. Enmascaramiento de Correos Electrónicos
    patron_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    texto_anon = re.sub(patron_email, "[CORREO OCULTO]", texto_anon)
    
    # 2. Enmascaramiento de DNI / Pasaportes (Formatos: XX.XXX.XXX, XX XXX XXX o XXXXXXXX)
    patron_dni = r'\b\d{1,2}(?:[\s.]\d{3}){2}\b|\b\d{7,8}\b'
    texto_anon = re.sub(patron_dni, "[DNI OCULTO]", texto_anon)
    
        # 3. Enmascaramiento de Nombres Propios tras palabras clave de actores legales
    patrones_actores = [
        r'\b(?:Sr\.|Sra\.|Don|Doña)\s+([A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?:\s+[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)*)',
        r'\b(?:ciudadano|ciudadana)\s+([A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?:\s+[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)*)',
        r'\b(?:caratulados|autos)\s+"([A-ZÁÉÍÓÚÑ][a-záéíóúñ]+\s+c/\s+[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)"'
    ]
    
    for patron in patrones_actores:
        coincidencias = re.findall(patron, texto_anon)
        for coincidencia in coincidencias:
            if coincidencia not in ["Fiscal", "Juez", "Secretaria", "Defensor"]:
                texto_anon = texto_anon.replace(coincidencia, "[SUJETO ANONIMIZADO]")
            
    return texto_anon

# --- INTERFAZ DE USUARIO ---
st.markdown('<div class="main-title">⚖️ Sistema de Anonimización de Sentencias Judiciales</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Herramienta orientada a la protección de datos personales (Ley 25.326) para el Poder Judicial de San Juan.</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Entrada de Documento")
    texto_ingresado = st.text_area(
        "Pegue la sentencia o resolución aquí:", 
        height=300, 
        placeholder="Ej: En la Ciudad de San Juan, el Sr. Juan Carlos Pérez, con DNI 34.555.666..."
    )
    archivo_subido = st.file_uploader("O suba un archivo de texto (.txt)", type=["txt"])
    if archivo_subido is not None:
        texto_ingresado = archivo_subido.read().decode("utf-8")

with col2:
    st.subheader("🔒 Resultado Anonimizado")
    if st.button("Procesar Documento", type="primary"):
        if texto_ingresado.strip():
            with st.spinner("Procesando estructura del documento..."):
                resultado = anonimizar_texto_judicial(texto_ingresado)
            st.text_area("Texto listo para publicación:", value=resultado, height=300)
            st.download_button(
                label="📥 Descargar Texto Anonimizado", 
                data=resultado, 
                file_name="sentencia_anonimizada.txt", 
                mime="text/plain"
            )
        else:
            st.warning("Por favor, ingrese o suba un texto para procesar.")