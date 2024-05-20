# Custom-Chatbot-with-Ollama-and-Llama-2
This project demonstrates how to create a custom chatbot using the Ollama framework and Llama 2. The chatbot is designed to assist students passionate about building a high-profile career in Machine Learning in Pakistan.



Installation
Prerequisites
Python installed on your system.
Ollama CLI installed.
Llama 2 model downloaded.

Steps
1.Clone the repository:
git clone https://github.com/SulemanShahani/llama-2.git
cd llama-2

2.Ensure you have ollama installed:
ollama version

3.Download and verify Llama 2 models:
ollama list
Ensure llama2 is listed.

Install required Python packages:
pip install requests gradio


Ensure you have ollama installed:
ollama version

Running the Chatbot
Verify the Model Creation:

Make sure you have created the model named mlgurur. If not, follow these steps:
ollama create mlgurur -f modelfile.ollama

Verify the model creation:
ollama list
Ensure mlgurur is listed.


Run the request.py script:

Start the chatbot server by running:
python request.py

This will start a local server and open a Gradio interface at http://127.0.0.1:7860.

Usage
Open the Gradio interface in your web browser.
Enter your prompt in the textbox and press enter.
The chatbot will respond based on the provided custom model.


