from django.db import models


# Create your models here.


class Flow(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Block(models.Model):
    flow = models.ForeignKey(Flow, related_name='blocks', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=[
        ('ollama_model', 'Ollama Model'),
        ('python_code', 'Python Code'),
    ])
    order = models.IntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.type})"


class OllamaModelBlock(Block):
    class Meta:
        proxy = True

    @property
    def config(self):
        try:
            return self.ollamamodelconfig
        except OllamaModelConfig.DoesNotExist:
            return None


class OllamaModelConfig(models.Model):
    block = models.OneToOneField(OllamaModelBlock, on_delete=models.CASCADE, primary_key=True,
                                 related_name='ollamamodelconfig')
    model_name = models.CharField(max_length=255)
    prompt = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Config for {self.block.name}"


class PythonCodeBlock(Block):
    class Meta:
        proxy = True

    @property
    def config(self):
        try:
            return self.pythoncodeconfig
        except PythonCodeConfig.DoesNotExist:
            return None


class PythonCodeConfig(models.Model):
    block = models.OneToOneField(PythonCodeBlock, on_delete=models.CASCADE, primary_key=True,
                                 related_name='pythoncodeconfig')
    code = models.TextField()

    def __str__(self):
        return f"Config for {self.block.name}"
