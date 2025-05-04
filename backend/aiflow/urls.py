from rest_framework.routers import DefaultRouter

from backend.aiflow import views
from backend.aiflow.views.flow_view import FlowViewSet

router = DefaultRouter()
router.register(f'flows', FlowViewSet)
router.register(f'blocks', views.BlockViewSet)
router.register(f'ollama_configs', views.OllamaModelConfigViewSet)
router.register(f'python_configs', views.PythonCodeConfigViewSet)
