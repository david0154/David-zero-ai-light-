MODEL_CONFIG = {
    "default": {
        "name": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        "quantized": False
    },
    "alt_options": [
        {
            "name": "bigcode/starcoder2-3b",
            "quantized": False
        },
        {
            "name": "Salesforce/codegen-350M-mono",
            "quantized": False
        },
        {
            "name": "TheBloke/CodeLlama-7B-GGUF",
            "quantized": True
        }
    ]
}