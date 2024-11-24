import openai

# Set up OpenAI API key
openai.api_key = "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"

def classify_sentence(sentence):
    """
    Classifies the words in a sentence based on their context using OpenAI GPT models.
    """
    prompt = f"""
    Classify the words in the following sentence based on their context. 
    Append a category to each word (e.g., 'geography', 'general', etc.), and remove unnecessary or common words.

    Sentence: "{sentence}"

    Return the output as a list of words with their category.
    """
    try:
        # Use gpt-3.5-turbo model with ChatCompletion API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that classifies words based on their context."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.7
        )
        # Extract and return the model's response
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Welcome to Context-Based Word Classifier!")
    print("Enter a sentence to classify words based on their context. Type 'exit' to quit.")
    
    while True:
        user_input = input("Enter a sentence: ")
        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        result = classify_sentence(user_input)
        print(f"Classified Output: {result}")

if __name__ == "__main__":
    main()
