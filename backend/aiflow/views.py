from rest_framework import viewsets

from backend.aiflow.models import Block, OllamaModelConfig, PythonCodeConfig
from backend.aiflow.serializers import BlockSerializer, OllamaModelConfigSerializer, PythonCodeConfigSerializer


class BlockViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer


class OllamaModelConfigViewSet(viewsets.ModelViewSet):
    queryset = OllamaModelConfig.objects.all()
    serializer_class = OllamaModelConfigSerializer


class PythonCodeConfigViewSet(viewsets.ModelViewSet):
    queryset = PythonCodeConfig.objects.all()
    serializer_class = PythonCodeConfigSerializer
