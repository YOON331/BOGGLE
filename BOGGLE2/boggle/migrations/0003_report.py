# Generated by Django 4.2.13 on 2024-05-29 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boggle', '0002_dictionary_quiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('work', models.CharField(default='null', max_length=400)),
                ('image', models.ImageField(blank=True, null=True, upload_to='task_images_2/')),
            ],
        ),
    ]
