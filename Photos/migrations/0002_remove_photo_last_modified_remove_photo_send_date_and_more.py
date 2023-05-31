# Generated by Django 4.2.1 on 2023-05-31 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Photos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='last_modified',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='send_date',
        ),
        migrations.AddField(
            model_name='photo',
            name='owner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Dono'),
        ),
        migrations.AddField(
            model_name='photo',
            name='shared_with',
            field=models.ManyToManyField(related_name='shared_with', to=settings.AUTH_USER_MODEL, verbose_name='Compartilhado com'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='discription',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='', verbose_name='Foto'),
        ),
    ]