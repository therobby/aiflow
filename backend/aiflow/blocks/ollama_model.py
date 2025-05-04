import json
import requests
import os

from backend.aiflow.models import OllamaModelConfig

def ollama_model(flow, block, flow_results, previous_output):
    config = OllamaModelConfig.objects.get(block=block)
    payload = {
        "prompt": config.prompt + (f"\nPrevious output: {previous_output}" if previous_output else ""),
        "model": config.model_name
    }
    ollama_generate_url = os.environ.get('OLLAMA_GENERATE_URL')
    ollama_generate_url = ollama_generate_url if ollama_generate_url is not None else 'http://localhost:11434/api/generate'
    response = requests.post(ollama_generate_url, json=payload, stream=True)
    response.raise_for_status()
    output = ""
    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode('utf-8'))
            output += data.get('response', '')
            if data.get('done'):
                break
    flow_results[flow.i][block.id]['output'] = output
    previous_output = output
    return flow_results, previous_output
