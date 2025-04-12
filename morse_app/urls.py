from django.urls import path
from .views import (
    welcome, translator,
    text_to_morse, morse_to_text,
    image_upload, extract_text
)

urlpatterns = [
    path("", welcome, name="welcome"),
    path("translator/", translator, name="translator"),
    path("text-to-morse/", text_to_morse, name="text_to_morse"),
    path("morse-to-text/", morse_to_text, name="morse_to_text"),
    path("image/", image_upload, name="image_upload"),
    path("extract_text/", extract_text, name="extract_text"),
]