import openai
import gradio as gr

# Set your OpenAI API key
openai.api_key = "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"

# Initialize messages with a system role
messages = [{"role": "system", "content": "You are a bot designed to explain Ohm's Law to school students."}]

# Define a function to interact with the OpenAI API
def CustomChatGPT(user_input):
    try:
        # Add the user's input to the conversation
        messages.append({"role": "user", "content": user_input})
        
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use a suitable model
            messages=messages
        )
        
        # Get the assistant's reply
        ChatGPT_reply = response["choices"][0]["message"]["content"]
        
        # Add the assistant's reply to the conversation
        messages.append({"role": "assistant", "content": ChatGPT_reply})
        return ChatGPT_reply
    
    except openai.error.OpenAIError as e:
        # Catch OpenAI API errors
        return f"OpenAI API Error: {e}"
    except Exception as e:
        # Catch all other errors
        return f"An unexpected error occurred: {e}"

# Create a Gradio interface
demo = gr.Interface(
    fn=CustomChatGPT,  # Function to call
    inputs="text",  # Text input for the user
    outputs="text",  # Text output for the bot
    title="Ohm's Law Chatbot",
    description="Ask me anything about Ohm's Law!"
)

# Launch the app
demo.launch(share=True)
