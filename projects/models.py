from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django_ckeditor_5.fields import CKEditor5Field


class ProjectImage(models.Model):
    project = models.ForeignKey("Project", on_delete=models.PROTECT, verbose_name="Проект")
    image = models.ImageField(upload_to="images/%Y/%m/%d", blank=True, verbose_name="Фотография")

    def __str__(self):
        return self.project.name

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


class ProjectVideo(models.Model):
    project = models.ForeignKey("Project", on_delete=models.PROTECT, verbose_name="Проект",)
    video = models.URLField(blank=True, default='https://www.youtube.com/embed/', verbose_name='Видео', help_text='https://www.youtube.com/embed/ ДОЛЖНО СТОЯТЬ ВНАЧАЛЕ ВМЕСТО https://www.youtube.com/')

    def __str__(self):
        return self.project.name

    def video_tag(self, obj):
        if obj.video:
            return format_html('<a href="{}">Link to video</a><video height="200px" controls><source src="{}" type="video/mp4"></video>'.format(obj.video.url, obj.video.url))
    video_tag.short_description = 'Video'

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название тега')
    views = models.PositiveBigIntegerField(default=0, verbose_name="Количество просмотров")
    slug = models.SlugField(max_length=75, unique=True, verbose_name='Слаг тега')

    def clean(self):
        super().clean()
        if self.pk:  # Проверяем, что объект уже сохранен в базе данных (имеет первичный ключ)
            original = self.__class__.objects.get(pk=self.pk)  # Получаем исходный объект из базы данных
            if self.name != original.name:
                while Tag.objects.filter(slug=self.slug).exists():
                    last_letter_slug = self.slug[-1]
                    try:
                        last_letter_slug_int = int(last_letter_slug)
                        last_letter_slug_int += 1
                        self.slug = self.slug[:-1] + str(last_letter_slug_int)
                    except ValueError:
                        self.slug += '2'
        else:
            while Tag.objects.filter(slug=self.slug).exists():
                last_letter_slug = self.slug[-1]
                try:
                    last_letter_slug_int = int(last_letter_slug)
                    last_letter_slug_int += 1
                    self.slug = self.slug[:-1] + str(last_letter_slug_int)
                except ValueError:
                    self.slug += '2'

    def get_absolute_url(self):
        return reverse('projects:tag_detail', kwargs={"tag_detail_slug": self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ['name']


class Category(models.Model):
    category = models.CharField(max_length=40, verbose_name='Название категории')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['category']


class Team(models.Model):
    project = models.ForeignKey(to="Project", on_delete=models.PROTECT, verbose_name="Проект")
    name = models.CharField(max_length=40, verbose_name='Имя фамилия')
    post = models.CharField(max_length=30, blank=True, verbose_name='Должность')
    description = models.TextField(max_length=150, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to="images/%Y/%m/%d", blank=True, verbose_name="Фотография")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Участник команды"
        verbose_name_plural = "Участники команды"
        ordering = ['name']


class Technologies(models.Model):
    technology = models.CharField(max_length=40, verbose_name='Название Технологии')

    def __str__(self):
        return self.technology

    class Meta:
        verbose_name = "Технология"
        verbose_name_plural = "Технологии"
        ordering = ['technology']


class Project(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название проекта')
    slug = models.SlugField(max_length=75, unique=True, verbose_name='Слаг проекта')
    photo = models.ImageField(upload_to="images/%Y/%m/%d", verbose_name="Фотография для карточки")
    category = models.ManyToManyField(to="Category", verbose_name="Категория проекта")
    tag = models.ForeignKey(to="Tag", on_delete=models.PROTECT, verbose_name="Тег проекта")
    name_team = models.CharField(max_length=20, blank=True, verbose_name='Название команды')
    technologies = models.ManyToManyField(to='Technologies', verbose_name='Используемые технологии')
    description = models.TextField(max_length=120, verbose_name='Описание')
    long_description = CKEditor5Field('Описание', config_name='extends', blank=True)
    hackaton = models.CharField(max_length=40, verbose_name='Хакатон')
    hackaton_place = models.SmallIntegerField(verbose_name='Занятое место в хакатоне')
    git_link = models.URLField(blank=True, verbose_name='Ссылка на репозиторий')

    def clean(self):
        super().clean()
        if self.pk:  # Проверяем, что объект уже сохранен в базе данных (имеет первичный ключ)
            original = self.__class__.objects.get(pk=self.pk)  # Получаем исходный объект из базы данных
            if self.name != original.name:
                while Project.objects.filter(slug=self.slug).exists():
                    last_letter_slug = self.slug[-1]
                    try:
                        last_letter_slug_int = int(last_letter_slug)
                        last_letter_slug_int += 1
                        self.slug = self.slug[:-1] + str(last_letter_slug_int)
                    except ValueError:
                        self.slug += '2'
        else:
            while Project.objects.filter(slug=self.slug).exists():
                last_letter_slug = self.slug[-1]
                try:
                    last_letter_slug_int = int(last_letter_slug)
                    last_letter_slug_int += 1
                    self.slug = self.slug[:-1] + str(last_letter_slug_int)
                except ValueError:
                    self.slug += '2'

    def get_absolute_url(self):
        return reverse('projects:project_detail', kwargs={"project_detail_slug": self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ['name']
