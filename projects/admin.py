from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    list_display_links = ('category',)
    search_fields = ['category', ]


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'views')
    list_display_links = ('name', 'views')
    prepopulated_fields = {"slug": ("name",)}


class TechnologiesAdmin(admin.ModelAdmin):
    list_display = ('technology',)
    list_display_links = ('technology',)
    ordering = ['technology', ]
    search_fields = ['technology', ]


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    readonly_fields = ('id', 'image_tag',)
    extra = 1


class TeamInline(admin.TabularInline):
    model = Team
    list_display = ('name', 'post',)
    extra = 1


class ProjectVideoInline(admin.TabularInline):
    model = ProjectVideo
    readonly_fields = ('id',)
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'name_team')
    list_display_links = ('name', 'name_team')
    search_fields = ['name', ]
    autocomplete_fields = ['technologies', 'category']
    inlines = [ProjectImageInline, ProjectVideoInline, TeamInline]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Technologies, TechnologiesAdmin)
