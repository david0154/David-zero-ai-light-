# main.py

import os
import sys
import time
from zero_light import ZeroLightAI
from voice_light import VoiceLight

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_output(code):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = os.path.join(OUTPUT_DIR, f"output_{timestamp}.txt")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
    return filename

def run_cli():
    ai = ZeroLightAI()
    speaker = VoiceLight()

    speaker.speak("Welcome to David AI Zero Light. What do you want me to build?")

    while True:
        try:
            prompt = input("\n🗣️ What should I build? (or 'exit')\n> ")
            if prompt.lower() == 'exit':
                speaker.speak("Goodbye!")
                break

            speaker.speak("Working on your request.")
            result = ai.generate_code(prompt)
            print("\n📦 Output:\n")
            print(result)

            file_path = save_output(result)
            print(f"\n💾 Code saved to: {file_path}")
            speaker.speak("Code saved successfully.")

        except KeyboardInterrupt:
            speaker.speak("Goodbye!")
            break

def run_ui():
    """Run the Gradio UI version of David AI."""
    try:
        from ui import demo
        print("[✅] Launching Gradio UI...")
        demo.launch()
    except Exception as e:
        print(f"❌ Failed to launch UI: {e}")
        print("💡 Make sure 'ui.py' defines 'demo' and Gradio is installed.")

# ✅ Must come last — after all functions are defined
if __name__ == "__main__":
    if "--cli" in sys.argv:
        run_cli()
    else:
        run_ui()
