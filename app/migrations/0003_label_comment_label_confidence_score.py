# Generated by Django 4.0.4 on 2022-06-14 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_catalogue_updated_alter_label_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='comment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='label',
            name='confidence_score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
