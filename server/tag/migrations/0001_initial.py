# Generated by Django 5.0.4 on 2024-04-10 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("tag_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
            ],
        ),
    ]
