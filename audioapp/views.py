# audioapp/views.py

from django.shortcuts import render, redirect
from django.conf import settings
from .forms import AudioFileForm
from .models import AudioFile
import os
import requests
import time

# AssemblyAI API configuration
upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'
API_KEY_ASSEMBLYAI = settings.API_KEY_ASSEMBLYAI or os.environ.get("API_KEY_ASSEMBLYAI")

headers_auth_only = {'authorization': API_KEY_ASSEMBLYAI}
headers = {
    "authorization": API_KEY_ASSEMBLYAI,
    "content-type": "application/json"
}

CHUNK_SIZE = 5_242_880  # 5MB

def upload(filename):
    def read_file(filename):
        with open(filename, 'rb') as f:
            while True:
                data = f.read(CHUNK_SIZE)
                if not data:
                    break
                yield data

    upload_response = requests.post(upload_endpoint, headers=headers_auth_only, data=read_file(filename))
    return upload_response.json()['upload_url']

def transcribe(audio_url):
    transcript_request = {'audio_url': audio_url}
    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
    return transcript_response.json()['id']

def poll(transcript_id):
    polling_endpoint = f'{transcript_endpoint}/{transcript_id}'
    polling_response = requests.get(polling_endpoint, headers=headers)
    return polling_response.json()

def get_transcription_result_url(url):
    transcribe_id = transcribe(url)
    while True:
        data = poll(transcribe_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']
        print("waiting for 30 seconds")
        time.sleep(30)

def save_transcript(url, title):
    data, error = get_transcription_result_url(url)
    if data:
        transcripts_dir = os.path.join(settings.MEDIA_ROOT, 'transcripts')
        if not os.path.exists(transcripts_dir):
            os.makedirs(transcripts_dir)
        filename = os.path.join(transcripts_dir, f'{title}.txt')
        with open(filename, 'w') as f:
            f.write(data['text'])
        print('Transcript saved')
        return filename
    elif error:
        print("Error!!!", error)
        return None

def landing_page(request):
    return render(request, 'audioapp/landing_page.html')

# audioapp/views.py

def upload_page(request):
    context = {}
    if request.method == 'POST':
        form = AudioFileForm(request.POST, request.FILES)
        if form.is_valid():
            audio_file = form.save()
            audio_path = audio_file.audio.path
            audio_url = upload(audio_path)  # Upload the audio file
            transcript_filename = save_transcript(audio_url, f"transcript_{audio_file.id}")  # Save transcript

            if transcript_filename:
                with open(transcript_filename, 'r') as file:
                    transcript_text = file.read()
                audio_file.transcript = transcript_text
                audio_file.save()

                # Set the transcription text to context
                context['transcription'] = transcript_text
            else:
                context['transcription'] = 'Error in transcription.'

    else:
        form = AudioFileForm()

    context['form'] = form
    return render(request, 'audioapp/upload_page.html', context)




def record_page(request):
    context={}
    if request.method == 'POST' and 'audio' in request.FILES:
        form = AudioFileForm(request.POST, request.FILES)
        if form.is_valid():
            audio_file = form.save()
            audio_path = audio_file.audio.path
            audio_url = upload(audio_path)
            transcript_filename = save_transcript(audio_url, f"transcript_{audio_file.id}")

            if transcript_filename:
                with open(transcript_filename, 'r') as file:
                    transcript_text = file.read()
                audio_file.transcript = transcript_text
                audio_file.save()
                context['transcription'] = transcript_text
                #return redirect('audioapp:record_page')  # Redirect to the same page to display the transcription
            else:
                context['transcription'] = 'Error in transcription.'


    else:
        form = AudioFileForm()

    # Fetch the latest AudioFile object to display the transcript
    # latest_audio = AudioFile.objects.latest('id') if AudioFile.objects.exists() else None
    context['form'] = form
    return render(request, 'audioapp/record_page.html', context)

