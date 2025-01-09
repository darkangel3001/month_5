# Generated by Django 5.1.4 on 2025-01-09 13:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.IntegerField(choices=[(1, '⭐'), (2, '⭐ ⭐'), (3, '⭐ ⭐ ⭐'), (4, '⭐ ⭐ ⭐ ⭐'), (5, '⭐ ⭐ ⭐ ⭐ ⭐')], default=1),
        ),
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movie_app.movie'),
        ),
    ]
