from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    list_display_links = ('category',)


class TechnologiesAdmin(admin.ModelAdmin):
    list_display = ('technology',)
    list_display_links = ('technology',)
    ordering = ['technology', ]
    search_fields = ['technology', ]


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    readonly_fields = ('id', 'image_tag',)
    extra = 1


class ProjectPresentationsInline(admin.TabularInline):
    model = ProjectPresentations
    readonly_fields = ('id',)
    extra = 1


class ProjectVideoInline(admin.TabularInline):
    model = ProjectVideo
    readonly_fields = ('id',)
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'category', 'team', 'name_team')
    list_display_links = ('name', 'category', 'team', 'name_team')
    search_fields = ['technologies', ]
    autocomplete_fields = ['technologies', ]
    inlines = [ProjectImageInline, ProjectVideoInline, ProjectPresentationsInline]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Technologies, TechnologiesAdmin)
