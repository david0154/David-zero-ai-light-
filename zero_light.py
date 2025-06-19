import os
import sys
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class ZeroLightAI:
    def __init__(self):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
        print(f"🚀 Loading lightweight model on {self.device}...")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name).to(self.device)

    def generate_code(self, prompt, max_tokens=512):
        print("🧠 Thinking...")
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        output = self.model.generate(**inputs, max_length=max_tokens, do_sample=True, top_k=50, top_p=0.95)
        code = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return code