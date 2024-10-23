from django.shortcuts import render
from pathlib import Path
from django.conf import settings
from .forms import InputForm
from datetime import datetime
import os


LOG_FILE_PATH = Path(settings.BASE_DIR)/'ex02'/'logs.txt'

def forms(request): 
    history = []
    if os.path.exists(LOG_FILE_PATH):
        with open(LOG_FILE_PATH, 'r') as log_file:
            for line in log_file:
                history.append(line.strip())
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            timestamp = datetime.now().strftime('%a-%d-%b-%Y %H:%M:%S')
            with open(LOG_FILE_PATH, 'a') as log_file:
                log_file.write(f"{timestamp} - {input_text}\n")
            history.append(f"{timestamp} - {input_text}")
    else:
        form = InputForm()
    return render(request, 'forms.html', {'form': form, 'history': history})

