import nltk
from nltk.chat.util import Chat, reflections
pairs = [
    (r'Hola|Hola!', ['*Se pone a bailar*']),
    (r'¿Cómo estás?', ['Rock solid']),
    (r'¿Qué puedes hacer?', ['Nothing can break me']),
    (r'(.*) (gracias|gracias por tu ayuda)', ['*Se pone a bailar*']),
    (r'Salir|Adiós', ['*se muere*']),
]
Malphite = Chat(pairs, reflections)

def chat():
    print("¡Hola! Soy Malphite. Escribe 'Salir' o 'Adiós' para terminar la conversación.")
    while True:
        user_input = input("Tú: ")
        response = Malphite.respond(user_input)
        if response:
            print("Chatbot: " + response)
        else:
            print("Chatbot: Lo siento, no entendí eso.")
        if user_input.lower() in ['salir', 'adiós']:
            break

if __name__ == "__main__":
    chat()