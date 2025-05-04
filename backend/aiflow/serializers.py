from rest_framework import serializers
from .models import Flow, Block, OllamaModelConfig, PythonCodeConfig

class OllamaModelConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = OllamaModelConfig
        fields = ['id', 'model_name', 'prompt']

class PythonCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonCodeConfig
        fields = ['id', 'code']

class BlockSerializer(serializers.ModelSerializer):
    ollamamodelconfig = OllamaModelConfigSerializer(read_only=True)
    pythoncodeconfig = PythonCodeConfigSerializer(read_only=True)

    class Meta:
        model = Block
        fields = ['id', 'name', 'type', 'order', 'flow', 'ollamamodelconfig', 'pythoncodeconfig']
        read_only_fields = ['flow', 'ollamamodelconfig', 'pythoncodeconfig']

    def create(self, validated_data):
        block_type = validated_data.pop('type')
        flow = validated_data['flow']
        block = Block.objects.create(flow=flow, type=block_type, **validated_data)
        return block

class FlowSerializer(serializers.ModelSerializer):
    blocks = BlockSerializer(many=True, read_only=True)

    class Meta:
        model = Flow
        fields = ['id', 'name', 'description', 'status', 'created_at', 'blocks']
        read_only_fields = ['id', 'status', 'created_at', 'blocks']