# Generated by Django 3.2.18 on 2023-02-22 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankingapp', '0007_alter_detail_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='subd',
            field=models.CharField(blank=True, choices=[('option1-1', 'Thamarassery')], max_length=20, null=True),
        ),
    ]
