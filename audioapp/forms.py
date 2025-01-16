# forms.py
# from django import forms
# from .models import AudioFile

# class AudioFileForm(forms.ModelForm):
#     class Meta:
#         model = AudioFile
#         fields = ['audio']

from django import forms
from .models import AudioFile

class AudioFileForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = ('audio',)

    def clean(self):
        cleaned_data = super().clean()
        audio = cleaned_data.get('audio')
        if not audio:
            raise forms.ValidationError('You must provide an audio file.')
        return cleaned_data
