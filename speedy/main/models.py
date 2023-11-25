from django.db import models
from ckeditor.fields import RichTextField


class PrivacyPolicy(models.Model):
    game_name = models.CharField(max_length=100, null=True, unique=True)
    text = RichTextField()

    class Meta:
        verbose_name = 'Privacy policy'

    def __str__(self):
        return f'Policy-privacy for {self.game_name}'