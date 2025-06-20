# ui.py

import gradio as gr
from zero_light import ZeroLightAI
from voice_light import VoiceLight

# Initialize AI and Voice
ai = ZeroLightAI()
speaker = VoiceLight()

# Handle text input
def handle_text(prompt):
    if not prompt.strip():
        return "Please enter something."
    
    result = ai.generate_code(prompt)
    speaker.speak(result)
    return result

# Handle voice input
def handle_voice(audio_file):
    import whisper
    model = whisper.load_model("base")  # Auto-downloads on first use
    result = model.transcribe(audio_file)
    return handle_text(result["text"])

# Define Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 🤖 David AI – Zero Light")
    gr.Markdown("Type or speak your request. David AI will generate and speak code for you.")

    with gr.Tab("💬 Text Input"):
        txt_input = gr.Textbox(label="What should I build?")
        txt_output = gr.Textbox(label="AI Output", lines=10)
        txt_btn = gr.Button("Generate")
        txt_btn.click(fn=handle_text, inputs=txt_input, outputs=txt_output)

    with gr.Tab("🎙️ Voice Input"):
        mic_input = gr.Audio(source="microphone", type="filepath", label="Speak here")
        mic_output = gr.Textbox(label="AI Output", lines=10)
        mic_btn = gr.Button("Generate from Voice")
        mic_btn.click(fn=handle_voice, inputs=mic_input, outputs=mic_output)
