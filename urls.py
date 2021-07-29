from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('instructions/', views.instructions, name='instructions'),
    path('part_1/', views.part_1_View, name='part_1'),
    path('part_2/', views.part_2_View, name='part_2'),
    path('part_3/', views.part_3_View, name='part_3'),
    path('processing', views.processing, name='processing'),
    path('results', views.results, name='results'),
    path('all', views.all, name='all'),
]