import streamlit as st
from transformers import pipeline
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

# Cargamos el pipeline de NER optimizado para español de forma cacheada
@st.cache_resource
def load_ner_pipeline():
    # Usamos un modelo robusto de reconocimiento de entidades en español
    return pipeline("ner", model="mrm8488/bert-spanish-ner-model", aggregation_strategy="simple")

ner_pipeline = load_ner_pipeline()

def anonimizar_texto(texto: str) -> str:
    # 1. Regex para DNI y Correos
    patron_dni = r'\b\d{1,2}(?:\.\d{3}){2}\b|\b\d{7,8}\b'
    texto_anon = re.sub(patron_dni, "[DNI OCULTO]", texto)
    
    patron_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    texto_anon = re.sub(patron_email, "[CORREO OCULTO]", texto_anon)
    
    # 2. IA para nombres de personas
    entidades = ner_pipeline(texto_anon)
    
    # Filtrar solo entidades que correspondan a personas (PER)
    desplazamientos = []
    for ent in entidades:
        if ent['entity_group'] == 'PER':
            desplazamientos.append((ent['start'], ent['end'], "[SUJETO ANONIMIZADO]"))
            
    # Reemplazar de atrás hacia adelante para mantener consistencia de índices
    texto_lista = list(texto_anon)
    for start, end, reemplazo in sorted(desplazamientos, key=lambda x: x[0], reverse=True):
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
            with st.spinner("Analizando entidades con BERT IA..."):
                resultado = anonimizar_texto(texto_ingresado)
            st.text_area("Texto listo para publicación:", value=resultado, height=300)
            st.download_button(label="📥 Descargar Texto Anonimizado", data=resultado, file_name="sentencia_anonimizada.txt", mime="text/plain")
        else:
            st.warning("Por favor, ingrese o suba un texto para procesar.")