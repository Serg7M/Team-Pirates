from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class ProjectImage(models.Model):
    project = models.ForeignKey("Project", on_delete=models.PROTECT, related_name="project_image", verbose_name="Проект:")
    image = models.ImageField(upload_to="images/%Y/%m/%d", blank=True, verbose_name="Фотография:")

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
    project = models.ForeignKey("Project", on_delete=models.PROTECT, verbose_name="Проект:", related_name="project_video")
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


class ProjectPresentations(models.Model):
    project = models.ForeignKey("Project", on_delete=models.PROTECT, verbose_name="Проект:", related_name="project_presentation")
    presentation = models.FileField(upload_to='presentation/%Y/%m/%d', blank=True, verbose_name='Презентация')

    def __str__(self):
        return self.project.name

    class Meta:
        verbose_name = "Презентация"
        verbose_name_plural = "Презентации"


class Category(models.Model):
    category = models.CharField(max_length=40, verbose_name='Название категории')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['category']


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
    photo = models.ImageField(upload_to="images/%Y/%m/%d", verbose_name="Фотография для карточки:")
    category = models.ForeignKey(to="Category", on_delete=models.PROTECT, verbose_name="Категория проекта")
    name_team = models.CharField(max_length=20, blank=True, verbose_name='Название команды')
    team = models.TextField(max_length=100, blank=True, verbose_name='Состав команды')
    task = models.TextField(max_length=600, blank=True, verbose_name='Задача')
    solution = models.TextField(max_length=800, blank=True, verbose_name='Решение')
    technologies = models.ManyToManyField(to='Technologies', verbose_name='Используемые технологии')
    description = models.TextField(max_length=1200, verbose_name='Описание')
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
        ordering = ['name', ]
