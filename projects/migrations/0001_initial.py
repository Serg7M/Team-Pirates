# Generated by Django 5.0.6 on 2024-05-25 18:26

import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=40, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название тега')),
                ('views', models.PositiveBigIntegerField(default=0, verbose_name='Количество просмотров')),
                ('slug', models.SlugField(max_length=75, unique=True, verbose_name='Слаг тега')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technology', models.CharField(max_length=40, verbose_name='Название Технологии')),
            ],
            options={
                'verbose_name': 'Технология',
                'verbose_name_plural': 'Технологии',
                'ordering': ['technology'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название проекта')),
                ('slug', models.SlugField(max_length=75, unique=True, verbose_name='Слаг проекта')),
                ('photo', models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='Фотография для карточки')),
                ('name_team', models.CharField(blank=True, max_length=20, verbose_name='Название команды')),
                ('description', models.TextField(max_length=120, verbose_name='Описание')),
                ('long_description', django_ckeditor_5.fields.CKEditor5Field(blank=True, verbose_name='Описание')),
                ('hackaton', models.CharField(max_length=40, verbose_name='Хакатон')),
                ('hackaton_place', models.SmallIntegerField(verbose_name='Занятое место в хакатоне')),
                ('git_link', models.URLField(blank=True, verbose_name='Ссылка на репозиторий')),
                ('category', models.ManyToManyField(to='projects.category', verbose_name='Категория проекта')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.tag', verbose_name='Тег проекта')),
                ('technologies', models.ManyToManyField(to='projects.technologies', verbose_name='Используемые технологии')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/%m/%d', verbose_name='Фотография')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.project', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='ProjectVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.URLField(blank=True, default='https://www.youtube.com/embed/', help_text='https://www.youtube.com/embed/ ДОЛЖНО СТОЯТЬ ВНАЧАЛЕ ВМЕСТО https://www.youtube.com/', verbose_name='Видео')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.project', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Имя фамилия')),
                ('post', models.CharField(blank=True, max_length=30, verbose_name='Должность')),
                ('description', models.TextField(blank=True, max_length=150, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/%m/%d', verbose_name='Фотография')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.project', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Участник команды',
                'verbose_name_plural': 'Участники команды',
                'ordering': ['name'],
            },
        ),
    ]
