from django.db import models

class TranslationHistory(models.Model):
    input_text = models.TextField()
    morse_output = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)