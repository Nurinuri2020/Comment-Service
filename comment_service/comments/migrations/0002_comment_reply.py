# Generated by Django 3.1.1 on 2020-10-07 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='replies', to='comments.comment', verbose_name='Ответ на комментарий'),
        ),
    ]