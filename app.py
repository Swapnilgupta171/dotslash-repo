import spacy

# Load the small English model for spaCy
nlp = spacy.load("en_core_web_sm")

# Example Context Dictionary (this is a simplified version)
context_dict = {
    "I": "general",
    "feeling": "sad",
    "good": "general",
    "down": "sad",
    "Earth": "geography",
    "crust": "geography",
    "core": "geography",
    "challenge": "general"
}

def context_based_word_identification(sentence):
    # Process the input sentence with spaCy
    doc = nlp(sentence)
    
    result = []
    
    for token in doc:
        word = token.text
        # Check if the word exists in our context dictionary
        if word.lower() in context_dict:
            result.append(f"{word.lower()}_{context_dict[word.lower()]}")
        else:
            # If no context is found, append as a general word
            result.append(f"{word.lower()}_general")
    
    return result

# Test Cases
input1 = "I am not feeling too good today"
output1 = context_based_word_identification(input1)
print(f"Input: {input1}\nOutput: {output1}\n")

input2 = "Earth’s crust and core"
output2 = context_based_word_identification(input2)
print(f"Input: {input2}\nOutput: {output2}")