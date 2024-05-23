from django.urls import path
from .views import *

app_name = 'projects'


urlpatterns = [
    path('project/<slug:project_detail_slug>/', project_detail, name='project_detail'),
    path('search/', search, name='search'),
    path('filter_fetch/', filter_fetch),
    path('', home, name='home'),
]
