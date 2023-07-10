#!/bin/python3
from flask import Flask, request
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def transdocker():
    data = request.get_data(as_text=True)  # Get the input string from the request
    response = translate(data)  # Call your helloWorld function with the input string
    return response

def translate(input_string):
    # Your logic for processing the input string and generating the response
    # For now, let's simply return a modified version of the input string

    tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-de")
    model = TFAutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-de")

    # Example input text
    input_text = "Hello, how are you?"

    # Tokenize the input text
    input_tokens = tokenizer.encode(input_string, return_tensors="pt")

    # Generate the translation
    translated_tokens = model.generate(input_tokens)

    # Decode the translated tokens back into text
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

    return translated_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)