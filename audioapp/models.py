from django.db import models

class AudioFile(models.Model):
    audio = models.FileField(upload_to='audio/')
    transcript = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Track the time of upload

    def __str__(self):
        return self.audio.name
