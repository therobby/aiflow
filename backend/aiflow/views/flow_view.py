import requests
from rest_framework import viewsets
from rest_framework.response import Response

from backend.aiflow.blocks.ollama_model import ollama_model
from backend.aiflow.blocks.python_code import python_code
from backend.aiflow.models import Flow, PythonCodeConfig, OllamaModelConfig
from backend.aiflow.serializers import FlowSerializer
from rest_framework.decorators import action


class FlowViewSet(viewsets.ModelViewSet):
    queryset = Flow.objects.all()
    serializer_class = FlowSerializer

    @action(detail=True, methods=['post'])
    def run(self, request, pk=None):
        # MVP TEMP
        flow_results = {}
        flow = self.get_object()
        flow.status = 'Running'
        flow.save()
        flow_results[flow.id] = {}

        blocks = flow.blocks.order_by('order')
        previous_output = None

        try:
            for block in blocks:
                flow_results[flow.id][block.id] = {'status': 'Running'}

                match block.type:
                    case 'ollama_model':
                        flow_results, previous_output = ollama_model(flow, block, flow_results, previous_output)
                    case 'python_code':
                        flow_results, previous_output = python_code(flow, block, flow_results, previous_output)
                    case _:
                        flow_results[flow.id][block.id]['status'] = 'Failed'
                        flow_results[flow.id][block.id]['error'] = f"Unknown block type: {block.type}"
                        flow.status = 'Failed'
                        flow.save()
                        return Response({'error': f"Flow failed at block '{block.name}': Unknown block type"},
                                        status=400)

                if flow_results[flow.id][block.id]['status'] == 'Failed':
                    return Response(
                        {'error': f"Flow failed at block '{block.name}': {flow_results[flow.id][block.id]['error']}"},
                        status=500)

                flow_results[flow.id][block.id]['status'] = 'Success'

            flow.status = 'Success'
            flow.save()
            return Response(
                {'message': f"Flow '{flow.name}' completed successfully.", 'results': flow_results[flow.id]})

        except OllamaModelConfig.DoesNotExist:
            flow.status = 'Failed'
            flow.save()
            return Response({'error': "Flow failed: Ollama model configuration not found."}, status=400)
        except PythonCodeConfig.DoesNotExist:
            flow.status = 'Failed'
            flow.save()
            return Response({'error': "Flow failed: Python code configuration not found."}, status=400)
        except requests.exceptions.RequestException as e:
            flow.status = 'Failed'
            flow.save()
            return Response({'error': f"Flow failed: Error communicating with Ollama: {str(e)}"}, status=500)
        except Exception as e:
            flow.status = 'Failed'
            flow.save()
            return Response({'error': f"Flow failed: An unexpected error occurred: {str(e)}"}, status=500)
