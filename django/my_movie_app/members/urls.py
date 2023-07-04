# from django.urls import path
# from . import views

# urlpatterns = [
#     path('members/', views.members, name='members'),
# ]

from django.contrib import admin
from django.urls import path

from my_movie_app import view as movieViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mypage' , movieViews.mypagefunction),
]
