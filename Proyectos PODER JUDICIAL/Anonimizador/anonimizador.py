import re
import spacy

# Cargamos el modelo de lenguaje en español de SpaCy
try:
    nlp = spacy.load("es_core_news_lg")
except OSError:
    raise OSError("Debes descargar el modelo ejecutando: python -m spacy download es_core_news_lg")

def anonimizar_texto_judicial(texto: str) -> str:
    """
    Recibe un texto judicial y anonimiza nombres de personas, 
    DNIs, direcciones y correos electrónicos.
    """
    # --- ETAPA 1: Anonimización por Expresiones Regulares (Regex) ---
    # Patrón para DNI (Formatos comunes: XX.XXX.XXX o XXXXXXXX)
    patron_dni = r'\b\d{1,2}(?:\.\d{3}){2}\b|\b\d{7,8}\b'
    texto_anonimizado = re.sub(patron_dni, "[DNI OCULTO]", texto)
    
    # Patrón para Correos Electrónicos
    patron_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    texto_anonimizado = re.sub(patron_email, "[CORREO OCULTO]", texto_anonimizado)

    # --- ETAPA 2: Anonimización por NLP (SpaCy) ---
    doc = nlp(texto_anonimizado)
    
    # Lista para almacenar los cambios de entidades de personas
    desplazamientos = []
    
    for ent in doc.ents:
        # PER identifica personas (Nombres y Apellidos)
        if ent.label_ == "PER":
            desplazamientos.append((ent.start_char, end_char := ent.end_char, "[Sujeto Anonimizado]"))
            
    # Reemplazamos las entidades de atrás hacia adelante para no romper los índices
    texto_lista = list(texto_anonimizado)
    for start, end, reemplazo in sorted(desplazamientos, key=lambda x: x[0], reverse=True):
        texto_lista[start:end] = list(reemplazo)
        
    return "".join(texto_lista)

if __name__ == "__main__":
    texto_ejemplo = (
        "En la provincia de San Juan, el Sr. Juan Carlos Pérez, con DNI 34.555.666, "
        "domiciliado en Av. Ignacio de la Roza 450 Oeste, comparece ante el Tribunal. "
        "Se deja constancia de que su correo de contacto es juan.perez@email.com. "
        "La Dra. María Alejandra Gómez dictó la correspondiente resolución."
    )
    
    print("--- TEXTO ORIGINAL ---")
    print(texto_ejemplo)
    print("\n--- TEXTO ANONIMIZADO ---")
    print(anonimizar_texto_judicial(texto_ejemplo))
