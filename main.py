from fastapi import FastAPI
import gradio as gr
import matplotlib.pyplot as plt
 
# Function to generate a PlantUML plot from the uploaded file content
def generate_plantuml_plot(file_content):
    # For demonstration, we'll just return a simple plot
    fig, ax = plt.subplots()
    ax.text(0.5, 0.5, file_content, ha='center', va='center', fontsize=12, wrap=True)
    ax.axis('off')
    return fig
 
# Function to handle chat messages
def handle_chat(message, chat_history):
    # For demonstration, we'll just echo the message back
    chat_history.append({"role": "user", "content": message})
    chat_history.append({"role": "assistant", "content": "You said: " + message})
    return "", chat_history

app = FastAPI()

# Create the Gradio app
with gr.Blocks() as demo:
    # File upload component
    file_upload = gr.File(label="Upload PlantUML File", file_types=[".txt", ".uml"], type="filepath")  # Changed type to 'filepath'
    # Output area for the PlantUML plot
    plantuml_plot = gr.Plot(label="PlantUML Plot")
    # Small chat window
    chat_input = gr.Textbox(label="Chat Input")
    chat_output = gr.Chatbot(type="messages", label="Chat Window")
    # Event listener for file upload
    file_upload.change(generate_plantuml_plot, inputs=file_upload, outputs=plantuml_plot)
    # Event listener for chat input
    chat_input.submit(handle_chat, inputs=[chat_input, chat_output], outputs=[chat_input, chat_output])

app = gr.mount_gradio_app(app, demo, path="/")
