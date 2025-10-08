from django.db import models

class Reel(models.Model):
    title = models.CharField(max_length=200)      # Reel ka title
    url = models.URLField()                        # Instagram reel ka URL
    source = models.CharField(max_length=50)      # Instagram, TikTok, etc.
    description = models.TextField(blank=True)    # Optional description
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp

    def __str__(self):
        return self.title
