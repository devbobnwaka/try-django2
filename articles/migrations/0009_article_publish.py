# Generated by Django 3.2.13 on 2022-07-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_remove_article_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='publish',
            field=models.DateField(blank=True, null=True),
        ),
    ]