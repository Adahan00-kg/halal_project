# Generated by Django 5.1.6 on 2025-03-02 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes_title', models.CharField(max_length=150)),
                ('status', models.CharField(blank=True, choices=[('Завершено', 'Завершено'), ('Отправлено', 'Отправлено'), ('Запрошены данные', 'Запрошены данные'), ('В процессе', 'В процессе'), ('На рассмотрении', 'На рассмотрении')], max_length=25, null=True)),
                ('date', models.DateField()),
            ],
        ),
    ]
