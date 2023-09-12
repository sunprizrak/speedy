from django.db import models
from PIL import Image


def path_logo(instance, filename):
    return 'games/{game_name}/logo/{filename}'.format(game_name=instance.name, filename=filename)


class Game(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to=path_logo, default='games/default.png', blank=True)
    description = models.TextField(max_length=200)
    apple_store = models.URLField(blank=True)
    google_store = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
        ordering = ['-created']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.logo.path)
        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.logo.path)