# Generated by Django 4.2.15 on 2024-08-20 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boggle", "0007_report_latitude_report_longitude_alter_report_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="report",
            name="title",
            field=models.CharField(default="null", max_length=400),
        ),
        migrations.AlterField(
            model_name="report",
            name="work",
            field=models.CharField(default="null", max_length=400),
        ),
    ]
