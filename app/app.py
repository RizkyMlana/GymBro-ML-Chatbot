import gradio as gr
# from app.chatbot_logic import process_input

def add_numbers(a, b):
    return a + b

interface = gr.Interface(
    fn=add_numbers,
    inputs=[gr.Number(label="First Number"), gr.Number(label="Second Number")],
    outputs=gr.Number(label="Sum")
)
interface.launch()