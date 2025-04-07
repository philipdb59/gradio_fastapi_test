from fastapi import FastAPI
import gradio as gr

app = FastAPI()

# Define a function to handle the chatbot's response
def chat_response(message, history):
    # For simplicity, the bot just echoes the user's message
    response = "You wrote: " + message["text"]
    if message.get("files"):
        response += " and uploaded " + str(len(message["files"])) + " files."
    return response

# Create a Gradio ChatInterface
demo = gr.ChatInterface(
    fn=chat_response,
    type="messages",
    multimodal=True,
    textbox=gr.MultimodalTextbox(
        interactive=True,
        placeholder="Enter message or upload file...",
        file_count="multiple",
        sources=["upload", "microphone"],
    ),
    title="Echo Bot",
    description="Upload any text or files and see the bot's response!",
)

if __name__ == "__main__":
    demo.launch(show_error=True)

app = gr.mount_gradio_app(app, demo, path="/")
