# Generated by Django 3.2.18 on 2023-02-21 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('gender', models.CharField(blank=True, choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=1, null=True)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('district', models.CharField(choices=[('calicut', 'CALICUT'), ('kannur', 'KANNUR'), ('ernakulam', 'ERNAKULAM')], max_length=20)),
            ],
        ),
    ]
