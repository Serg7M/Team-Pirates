from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    list_display_links = ('category',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'views')
    list_display_links = ('name', 'views')
    prepopulated_fields = {"slug": ("name",)}


class HackatonAdmin(admin.ModelAdmin):
    list_display = ('hackaton',)
    list_display_links = ('hackaton',)


class TechnologiesAdmin(admin.ModelAdmin):
    list_display = ('technology',)
    list_display_links = ('technology',)
    ordering = ['technology', ]
    search_fields = ['technology', ]


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    readonly_fields = ('id', 'image_tag',)
    extra = 1


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'post',)
    list_display_links = ('name', 'post',)
    search_fields = ['name', ]


class ProjectVideoInline(admin.TabularInline):
    model = ProjectVideo
    readonly_fields = ('id',)
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'category', 'name_team')
    list_display_links = ('name', 'category', 'name_team')
    search_fields = ['technologies', ]
    autocomplete_fields = ['technologies', 'team']
    inlines = [ProjectImageInline, ProjectVideoInline]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Technologies, TechnologiesAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Hackaton, HackatonAdmin)
