from django.shortcuts import render
from pathlib import Path
from django.conf import settings
from .forms import InputForm
from datetime import datetime


LOG_FILE_PATH = Path(settings.BASE_DIR) / 'ex02' / 'logs.txt'

def index(request):
    history = []
    form = InputForm()
    return render(request, 'forms.html', {'form': form, 'history': history})

