# Generated by Django 4.2.13 on 2024-05-24 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boggle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hNm', models.CharField(blank=True, max_length=255, null=True)),
                ('explain', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('correct_answer', models.CharField(max_length=100)),
                ('wrong_answers', models.JSONField()),
            ],
        ),
    ]
