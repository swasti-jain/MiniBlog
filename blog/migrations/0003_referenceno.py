# Generated by Django 4.0.2 on 2022-05-27 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_news_science_technology'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenceNo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=50)),
            ],
        ),
    ]