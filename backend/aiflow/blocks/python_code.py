from rest_framework.response import Response
from backend.aiflow.models import PythonCodeConfig

import subprocess

def python_code(flow, block, flow_results, previous_output):
    config = PythonCodeConfig.objects.get(block=block)
    try:
        process = subprocess.run([
                'python', '-c', config.code
            ],
            input=previous_output,
            capture_output=True,
            text=True,
            check=True
        )
        output = process.stdout
        flow_results[flow.id][block.id]['output'] = output
        previous_output = output
    except subprocess.CalledProcessError as e:
        flow_results[flow.id][block.id]['status'] = 'Failed'
        flow_results[flow.id][block.id]['error'] = f"Python code execution failed: {e.stderr}"
        flow.status = 'Failed'
        flow.save()
        return Response({'error': f"Flow failed at block '{block.name}': Python code execution error"},
                        status=500)
    except Exception as e:
        flow_results[flow.id][block.id]['status'] = 'Failed'
        flow_results[flow.id][block.id]['error'] = str(e)
        flow.status = 'Failed'
        flow.save()
        return Response({'error': f"Flow failed at block '{block.name}': {str(e)}"}, status=500)

    return flow_results, previous_output
