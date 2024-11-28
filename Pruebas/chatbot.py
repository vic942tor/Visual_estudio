from transformers import LlamaForCausalLM, LlamaTokenizer

# Configurar el modelo y tokenizer de LLaMA
model_name = "meta-llama/Llama-2-7b-hf"  # Modelo compatible con múltiples idiomas
tokenizer = LlamaTokenizer.from_pretrained(model_name)
model = LlamaForCausalLM.from_pretrained(model_name)

# Memoria para la conversación
conversation_history = []

def chatbot_response(user_input, history):
    # Agregar entrada del usuario al historial
    history.append(f"Usuario: {user_input}")
    context = "\n".join(history) + "\nChatbot:"

    # Tokenizar el contexto
    inputs = tokenizer(context, return_tensors="pt", padding=True, truncation=True)

    # Generar respuesta en español
    outputs = model.generate(
        inputs["input_ids"],
        max_length=inputs["input_ids"].shape[1] + 50,  # Longitud ajustada
        temperature=0.7,  # Controlar la creatividad
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
        do_sample=True,
    )

    # Decodificar la respuesta
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    chatbot_reply = generated_text[len(context):].strip()

    # Agregar respuesta del chatbot al historial
    history.append(f"Chatbot: {chatbot_reply}")
    return chatbot_reply

def main():
    print("Bienvenido al chatbot basado en LLaMA. Escribe 'salir' para terminar.")
    global conversation_history
    while True:
        user_input = input("Usuario: ")
        if user_input.lower() == "salir":
            print("Chatbot: ¡Adiós!")
            break
        reply = chatbot_response(user_input, conversation_history)
        print(f"Chatbot: {reply}")

if __name__ == "__main__":
    main()



