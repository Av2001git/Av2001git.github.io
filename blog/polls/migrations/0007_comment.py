# Generated by Django 4.0.4 on 2022-05-12 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_remove_contact_email_remove_contact_massig'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('massig', models.TextField()),
            ],
        ),
    ]
