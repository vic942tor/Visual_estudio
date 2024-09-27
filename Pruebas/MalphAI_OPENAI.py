import openai

# Reemplaza 'YOUR_PROJECT_API_KEY' con tu clave API de OpenAI
openai.api_key = 0
def malphite_response(prompt):
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # O usa el modelo que prefieras, como "gpt-4"
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

def malphite_chat():
    print("Hola, soy Malphite. Escribe 'salir' para terminar la conversación.")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == 'salir':
            print("Malphite: ¡Hasta luego!")
            break
        response = malphite_response(user_input)
        print(f"Malphite: {response}")

if __name__ == "__main__":
    malphite_chat()
