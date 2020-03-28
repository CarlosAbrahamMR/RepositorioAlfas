# Generated by Django 3.0.3 on 2020-03-28 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0003_auto_20200327_2206'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UsuarioCanciones',
            new_name='PlaylistCanciones',
        ),
        migrations.CreateModel(
            name='UsuariosCanciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Cancion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]