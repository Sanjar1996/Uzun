# Generated by Django 3.2.6 on 2021-08-10 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainsitemodels',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='futuremodels',
            name='plan',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='mainsitemodels',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
