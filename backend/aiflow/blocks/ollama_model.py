import json
import requests

from backend.aiflow.models import OllamaModelConfig


def ollama_model(flow, block, flow_results, previous_output):
    config = OllamaModelConfig.objects.get(block=block)
    payload = {"prompt": config.prompt + (f"\nPrevious output: {previous_output}" if previous_output else ""),
               "model": config.model_name}
    response = requests.post('http://localhost:11434/api/generate', json=payload, stream=True)
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
