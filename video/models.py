from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=256, unique=True, null=False)
    about = models.TextField(max_length=500, null=False)
    video = models.FileField(null=False, upload_to='video/')
    published = models.DateTimeField(null=False, auto_now_add=True, blank=True)
    source = models.URLField(null=True)

    def __str__(self) -> str:
        return str(self.title)
