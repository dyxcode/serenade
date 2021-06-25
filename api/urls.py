from django.urls import re_path
from . import views

urlpatterns = [
    re_path('^image/$', views.ImageView.as_view()),
    re_path('^music/$', views.MusicView.as_view()),
    re_path('^video/$', views.VideoView.as_view()),
    re_path('^file/$', views.FileView.as_view()),
    re_path('^blog/$', views.BlogView.as_view()),
]