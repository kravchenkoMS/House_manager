from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.open_mainpage, name='main_page'), # головна сторінка
    path('resident/', include('resident.urls')),
    path('moderator/', include('moderator.urls'))
]
