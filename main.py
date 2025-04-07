from fastapi import FastAPI
import gradio as gr
import matplotlib.pyplot as plt
 
app = FastAPI()
 
def generate_plantuml_plot(file_content):
    # For demonstration, generate a simple plot showing the file content text.
    fig, ax = plt.subplots()
    ax.text(0.5, 0.5, file_content, ha='center', va='center', fontsize=12, wrap=True)
    ax.axis('off')
    return fig
 
def handle_chat(message, chat_history):
    # For demonstration, echo the chat message.
    chat_history.append({"role": "user", "content": message})
    chat_history.append({"role": "assistant", "content": "You said: " + message})
    return "", chat_history
 
with gr.Blocks() as demo:
    # File upload component with allowed file types and type set to 'filepath'
    file_upload = gr.File(label="Upload PlantUML File", file_types=[".txt", ".uml"], type="filepath")
    # Plot output for displaying the generated PlantUML plot
    plantuml_plot = gr.Plot(label="PlantUML Plot")
    # Chat components
    chat_input = gr.Textbox(label="Chat Input")
    chat_output = gr.Chatbot(type="messages", label="Chat Window")
    # Set up event listener: update plot when a file is uploaded
    file_upload.change(generate_plantuml_plot, inputs=file_upload, outputs=plantuml_plot)
    # Set up event listener: handle chat input submissions
    chat_input.submit(handle_chat, inputs=[chat_input, chat_output], outputs=[chat_input, chat_output])
 
# Mount the Gradio Blocks app into the FastAPI app at the specified path
app = gr.mount_gradio_app(app, demo, path="/")
