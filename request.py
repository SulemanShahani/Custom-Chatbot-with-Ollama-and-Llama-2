import requests
import json
import gradio as gr

# Correct the URL format
url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',
}

history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model": "mlgurur",
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        data = response.json()
        actual_response = data.get('response', 'No response key in the response JSON.')
        return actual_response
    else:
        error_message = f"Error {response.status_code}: {response.text}"
        print(error_message)
        return error_message

interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=2, placeholder="Enter Your Prompt"),
    outputs="text"
)

interface.launch()
