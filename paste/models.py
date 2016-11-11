from django.db import models

class pasteModel(models.Model):
    slug = models.CharField(max_length=30)
    name = models.CharField(max_length=200, default='Untitled')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.slug