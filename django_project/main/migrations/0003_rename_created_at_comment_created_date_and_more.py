# Generated by Django 5.0.6 on 2024-06-06 10:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_at',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='content',
            new_name='text',
        ),
        migrations.AddField(
            model_name='news',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='news_comments', to='main.comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_comments', to='main.news'),
        ),
    ]