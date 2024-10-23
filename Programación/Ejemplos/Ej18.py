import numpy as np
import json
import nltk
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM, Embedding
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from googlesearch import search
import requests
from bs4 import BeautifulSoup

# Descargar datos de NLTK
nltk.download('punkt')

# Cargar memoria desde un archivo JSON
def cargar_memoria(filename='memoria.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Guardar memoria en un archivo JSON
def guardar_memoria(respuestas, filename='memoria.json'):
    with open(filename, 'w') as f:
        json.dump(respuestas, f)

# Cargar respuestas anteriores si existen
respuestas = cargar_memoria()

# Datos de entrenamiento (ejemplo simple)
datos_entrenamiento = [
    ("Hola", "saludo"),
    ("¿Cómo estás?", "saludo"),
    ("¿Qué tal?", "saludo"),
    ("Adiós", "despedida"),
    ("Nos vemos", "despedida"),
    ("Chao", "despedida"),
    ("¿Cuál es tu nombre?", "pregunta_nombre"),
    ("¿Quién eres?", "pregunta_nombre"),
    ("Dime tu nombre", "pregunta_nombre"),
]

# Preprocesamiento de los datos
entrenamiento_preguntas = [pregunta for pregunta, etiqueta in datos_entrenamiento]
entrenamiento_etiquetas = [etiqueta for pregunta, etiqueta in datos_entrenamiento]

# Crear el Tokenizer para convertir texto en secuencias
tokenizer = Tokenizer()
tokenizer.fit_on_texts(entrenamiento_preguntas)
secuencias_entrenamiento = tokenizer.texts_to_sequences(entrenamiento_preguntas)

# Obtener las palabras únicas
vocabulario_size = len(tokenizer.word_index) + 1

# Padding de las secuencias para que todas tengan la misma longitud
max_len = 5
entrenamiento_x = pad_sequences(secuencias_entrenamiento, maxlen=max_len)

# Codificar las etiquetas
encoder = LabelEncoder()
etiquetas_encoded = encoder.fit_transform(entrenamiento_etiquetas)

# Crear el modelo de red neuronal con Embeddings y LSTM
modelo = Sequential()
modelo.add(Embedding(input_dim=vocabulario_size, output_dim=16, input_length=max_len))
modelo.add(LSTM(64, return_sequences=True))
modelo.add(LSTM(32))
modelo.add(Dropout(0.5))
modelo.add(Dense(32, activation='relu'))
modelo.add(Dense(len(set(entrenamiento_etiquetas)), activation='softmax'))

# Compilar el modelo
modelo.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
modelo.fit(entrenamiento_x, np.array(etiquetas_encoded), epochs=300, batch_size=8, verbose=1)

# Función para predecir la etiqueta de una pregunta
def predecir_clase(pregunta):
    secuencia = tokenizer.texts_to_sequences([pregunta])
    secuencia = pad_sequences(secuencia, maxlen=max_len)
    prediccion = modelo.predict(secuencia)[0]
    etiqueta_predicha = encoder.inverse_transform([np.argmax(prediccion)])[0]
    return etiqueta_predicha

# Función para buscar en Google y extraer contenido
def buscar_en_google(query):
    resultados = list(search(query))  # Eliminar el argumento num
    return resultados


# Función para hacer scraping del contenido de una página web
def hacer_scraping(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error si la respuesta es un error
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraer texto de los párrafos
        parrafos = soup.find_all('p')
        contenido = ' '.join([p.get_text() for p in parrafos])
        return contenido or "No se encontró contenido en los párrafos."
    except Exception as e:
        return f"Error al hacer scraping: {str(e)}"

# Función para entrenar el modelo con nueva información
def entrenar_con_nueva_interaccion(pregunta, etiqueta):
    global modelo
    global entrenamiento_preguntas
    global entrenamiento_etiquetas
    global respuestas
    
    # Agregar los nuevos datos al conjunto de entrenamiento
    entrenamiento_preguntas.append(pregunta)
    entrenamiento_etiquetas.append(etiqueta)

    # Actualizar el tokenizer y los datos
    tokenizer.fit_on_texts(entrenamiento_preguntas)
    secuencias_entrenamiento = tokenizer.texts_to_sequences(entrenamiento_preguntas)
    entrenamiento_x = pad_sequences(secuencias_entrenamiento, maxlen=max_len)
    etiquetas_encoded = encoder.fit_transform(entrenamiento_etiquetas)
    
    # Reentrenar el modelo con los nuevos datos
    modelo.fit(entrenamiento_x, np.array(etiquetas_encoded), epochs=50, batch_size=8, verbose=1)

    # Guardar la nueva respuesta en memoria
    respuestas[etiqueta] = respuestas.get(etiqueta, "No tengo una respuesta a eso.")
    guardar_memoria(respuestas)

# Chat con el chatbot que aprende
def chatbot():
    print("Chatbot: ¡Hola! Escribe 'salir' para terminar la conversación.")
    while True:
        entrada_usuario = input("Tú: ")
        if entrada_usuario.lower() == "salir":
            print("Chatbot: ¡Adiós!")
            break

        etiqueta = predecir_clase(entrada_usuario)
        if etiqueta in respuestas:
            print("Chatbot:", respuestas[etiqueta])
        else:
            # Si no encuentra una respuesta predefinida, busca en Google
            print("Chatbot: No tengo una respuesta a eso, buscando información...")
            resultados = buscar_en_google(entrada_usuario)
            if resultados:
                url = resultados[0]
                contenido = hacer_scraping(url)
                print("Chatbot: He encontrado algo en la web:", contenido)
            else:
                print("Chatbot: No se encontraron resultados en Google.")

            # Preguntar al usuario cómo debería responder
            nueva_respuesta = input("¿Cómo debería responder a eso? ")
            respuestas[etiqueta] = nueva_respuesta
            entrenar_con_nueva_interaccion(entrada_usuario, etiqueta)

# Ejecutar el chatbot
chatbot()
# Función para buscar en Google y extraer contenido
