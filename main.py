import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'your-api-key'

def get_chat_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can choose different models like "text-curie-001" or "text-babbage-001"
            prompt=prompt,
            max_tokens=150,  # Adjust based on how detailed you want the responses
            temperature=0.7,  # Adjust for creativity; lower is more deterministic
            top_p=1.0,  # Adjust for diverse responses
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    print("Chatbot: Hello! How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        prompt = f"You are a customer service chatbot. A user asks: '{user_input}'"
        response = get_chat_response(prompt)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
