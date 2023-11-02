from django.db import models
from ckeditor.fields import RichTextField


class PrivacyPolicy(models.Model):
    text = RichTextField()

    def save(self, *args, **kwargs):
        if PrivacyPolicy.objects.exists() and not self.pk:
            return
        else:
            super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Privacy policy'

    def __str__(self):
        return 'Policy-privacy'