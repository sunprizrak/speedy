# Generated by Django 4.2.7 on 2023-11-02 16:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='privacypolicy',
            options={'verbose_name': 'Privacy policy'},
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
