from django.contrib import admin
from .models import TranslationHistory

@admin.register(TranslationHistory)
class TranslationHistoryAdmin(admin.ModelAdmin):
    list_display = ('input_text', 'morse_output', 'created_at')
    search_fields = ('input_text', 'morse_output')