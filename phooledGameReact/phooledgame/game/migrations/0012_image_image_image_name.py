# Generated by Django 5.0.2 on 2024-03-25 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0011_phishingattribute_phishgamesessioncards_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='avatars/'),
        ),
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default='image', max_length=100),
        ),
    ]