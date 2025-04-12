from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import default_storage
from .models import TranslationHistory
from django.views.decorators.csrf import csrf_exempt

import os
import pytesseract
from PIL import Image

# Path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Pinky\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# Full Morse Code Dictionary (Extended)
MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--', ':': '---...',
    ';': '-.-.-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', '_': '..--.-',
    '=': '-...-', '+': '.-.-.', '-': '-....-', '"': '.-..-.', "'": '.----.',
    '/': '-..-.', '@': '.--.-.', '$': '...-..-', ' ': '/'
}

# Reverse Dictionary for Morse to Text
REVERSE_MORSE_DICT = {value: key for key, value in MORSE_DICT.items()}

def welcome(request):
    return render(request, 'morse_app/welcome.html')

def translator(request):
    return render(request, 'morse_app/translator.html')

def image_upload(request):
    return render(request, 'morse_app/image_upload.html')

def text_to_morse(request):
    if request.method == 'GET':
        text = request.GET.get('text', '').upper()
        unsupported_chars = [char for char in text if char not in MORSE_DICT]

        if unsupported_chars:
            return JsonResponse({'error': f"Unsupported characters: {', '.join(unsupported_chars)}"}, status=400)

        morse_code = ' '.join(MORSE_DICT.get(char, '') for char in text)
        return JsonResponse({'morse_code': morse_code})

def morse_to_text(request):
    if request.method == 'GET':
        morse_code = request.GET.get('morse', '')
        words = morse_code.strip().split(' / ')
        translated_words = []

        for word in words:
            chars = [REVERSE_MORSE_DICT.get(code, '?') for code in word.split()]
            translated_words.append(''.join(chars))

        text = ' '.join(translated_words)

        if '?' in text:
            return JsonResponse({'error': "Invalid Morse Code entered!"}, status=400)

        return JsonResponse({'text': text})

def extract_text(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        image_path = default_storage.save('temp/' + image.name, image)
        image_full_path = os.path.join(default_storage.location, image_path)

        try:
            extracted_text = pytesseract.image_to_string(Image.open(image_full_path)).strip().upper()

            if not extracted_text or not any(char.isalnum() for char in extracted_text):
                return JsonResponse({'error': 'Unsupported image. No valid text found.'})

            morse_code = ' '.join(MORSE_DICT.get(char, '') for char in extracted_text if char in MORSE_DICT)

            return JsonResponse({
                'text': extracted_text,
                'morse': morse_code
            })

        except Exception as e:
            return JsonResponse({'error': f'OCR Failed: {str(e)}'}, status=400)

        finally:
            if os.path.exists(image_full_path):
                os.remove(image_full_path)

    return JsonResponse({'error': 'No image uploaded or invalid request'}, status=400)