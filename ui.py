# ui.py

import gradio as gr
from zero_light import ZeroLightAI

# Initialize the AI
ai = ZeroLightAI()

# Handle text input
def handle_text(prompt):
    if not prompt.strip():
        return "Please enter something."
    
    result = ai.generate_code(prompt)
    return result  # Only return text, no voice

# Define Gradio UI (text-only)
with gr.Blocks() as demo:
    gr.Markdown("## 🤖 David AI – Zero Light")
    gr.Markdown("Type your request below. David AI will respond with code.")

    txt_input = gr.Textbox(label="What should I build?")
    txt_output = gr.Textbox(label="AI Output", lines=10)
    txt_btn = gr.Button("Generate")

    txt_btn.click(fn=handle_text, inputs=txt_input, outputs=txt_output)
