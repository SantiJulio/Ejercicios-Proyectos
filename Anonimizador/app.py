import streamlit as st
import spacy
import re
import os

# Configuración de la página (Debe ser la primera línea de Streamlit)
st.set_page_config(
    page_title="Anonimizador Judicial AI",
    page_icon="⚖️",
    layout="wide"
)

# Carga optimizada del modelo de SpaCy con descarga automática integrada
@st.cache_resource
def load_nlp():
    try:
        # Intentamos cargar el modelo normalmente
        return spacy.load("es_core_news_lg")
    except OSError:
        # Si no está instalado en la nube, forzamos su descarga por consola
        with st.spinner("Instalando dependencias de lenguaje en el servidor (Solo la primera vez)..."):
            os.system("python -m spacy download es_core_news_lg")
        return spacy.load("es_core_news_lg")

nlp = load_nlp()

def anonimizar_texto(texto: str) -> str:
    """Función de anonimización (tu lógica de backend)"""
    # Expresiones regulares
    patron_dni = r'\b\d{1,2}(?:\.\d{3}){2}\b|\b\d{7,8}\b'
    texto_anon = re.sub(patron_dni, "[DNI OCULTO]", texto)
    
    patron_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    texto_anon = re.sub(patron_email, "[CORREO OCULTO]", texto_anon)
    
    # NLP con SpaCy
    doc = nlp(texto_anon)
    desplazamientos = []
    
    for ent in doc.ents:
        if ent.label_ == "PER":
            desplazamientos.append((ent.start_char, ent.end_char, "[SUJETO ANONIMIZADO]"))
            
    texto_lista = list(texto_anon)
    for start, end, reemplazo in sorted(desplazamientos, key=lambda x: x[0], reverse=True):
        texto_lista[start:end] = list(reemplazo)
        
    return "".join(texto_lista)

# --- INTERFAZ DE USUARIO ---

st.markdown('<div class="main-title">⚖️ Sistema de Anonimización de Sentencias Judiciales</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Herramienta orientada a la protección de datos personales (Ley 25.326) para el Poder Judicial de San Juan.</div>', unsafe_allow_html=True)

# Layout de dos columnas para entrada de datos
col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Entrada de Documento")
    
    # Opción 1: Pegar texto
    texto_ingresado = st.text_area(
        "Pegue la sentencia o resolución aquí:", 
        height=300,
        placeholder="Ej: En la Ciudad de San Juan, el Sr. Juan Pérez..."
    )
    
    # Opción 2: Subir archivo
    archivo_subido = st.file_uploader("O suba un archivo de texto (.txt)", type=["txt"])
    
    if archivo_subido is not None:
        texto_ingresado = archivo_subido.read().decode("utf-8")

with col2:
    st.subheader("🔒 Resultado Anonimizado")
    
    # Botón de acción
    if st.button("Procesar Documento", type="primary"):
        if texto_ingresado.strip():
            with st.spinner("Analizando entidades con NLP..."):
                resultado = anonimizar_texto(texto_ingresado)
                
            # Mostrar resultado en un área de texto de solo lectura
            st.text_area("Texto listo para publicación:", value=resultado, height=300)
            
            # Botón para descargar el resultado
            st.download_button(
                label="📥 Descargar Texto Anonimizado",
                data=resultado,
                file_name="sentencia_anonimizada.txt",
                mime="text/plain"
            )
        else:
            st.warning("Por favor, ingrese o suba un texto para procesar.")