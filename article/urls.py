from django.urls import path
# 引入views.py

from . import views
app_name = 'article'

urlpatterns = [
    path('article-list/', views.article_list, name='article_list'),
]
