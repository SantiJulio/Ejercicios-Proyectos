import streamlit as st
import spacy
import re
import subprocess
import sys

# Configuración de la página (Debe ser la primera línea de Streamlit)
st.set_page_config(
    page_title="Anonimizador Judicial AI",
    page_icon="⚖️",
    layout="wide"
)

# Carga optimizada del modelo de SpaCy con descarga síncrona controlada
@st.cache_resource
def load_nlp():
    try:
        return spacy.load("es_core_news_lg")
    except OSError:
        # Descarga el modelo usando el pipeline de ejecución nativo del sistema
        subprocess.run([sys.executable, "-m", "spacy", "download", "es_core_news_lg"], check=True)
        return spacy.load("es_core_news_lg")

nlp = load_nlp()

# Estilo personalizado (Colores institucionales azul/gris)
st.markdown("""
    <style>
    .main-title { color: #1E3A8A; font-size: 32px; font-weight: bold; margin-bottom: 20px; }
    .subtitle { color: #4B5563; font-size: 18px; margin-bottom: 30px; }
    </style>
""", unsafe_allow_html=True)

def anonimizar_texto(texto: str) -> str:
    """Función de anonimización"""
    patron_dni = r'\b\d{1,2}(?:\.\d{3}){2}\b|\b\d{7,8}\b'
    texto_anon = re.sub(patron_dni, "[DNI OCULTO]", texto)
    
    patron_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    texto_anon = re.sub(patron_email, "[CORREO OCULTO]", texto_anon)
    
    doc = nlp(texto_anon)
    desplazamientos = []
    
    for ent in doc.ents:
        if ent.label_ == "PER":
            desplazamientos.append((ent.start_char, ent.end_char, "[SUJETO ANONIMIZADO]"))
            
    texto_lista = list(texto_anon)
    for start, end, reemplazo in sorted(desplazamientos, key=lambda x: x, reverse=True):
        texto_lista[start:end] = list(reemplazo)
        
    return "".join(texto_lista)

# --- INTERFAZ DE USUARIO ---
st.markdown('<div class="main-title">⚖️ Sistema de Anonimización de Sentencias Judiciales</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Herramienta orientada a la protección de datos personales (Ley 25.326) para el Poder Judicial de San Juan.</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Entrada de Documento")
    texto_ingresado = st.text_area("Pegue la sentencia o resolución aquí:", height=300, placeholder="Ej: En la Ciudad de San Juan, el Sr. Juan Pérez...")
    archivo_subido = st.file_uploader("O suba un archivo de texto (.txt)", type=["txt"])
    if archivo_subido is not None:
        texto_ingresado = archivo_subido.read().decode("utf-8")

with col2:
    st.subheader("🔒 Resultado Anonimizado")
    if st.button("Procesar Documento", type="primary"):
        if texto_ingresado.strip():
            with st.spinner("Analizando entidades con NLP..."):
                resultado = anonimizar_texto(texto_ingresado)
            st.text_area("Texto listo para publicación:", value=resultado, height=300)
            st.download_button(label="📥 Descargar Texto Anonimizado", data=resultado, file_name="sentencia_anonimizada.txt", mime="text/plain")
        else:
            st.warning("Por favor, ingrese o suba un texto para procesar.")