from django.urls import path
from .views import *

urlpatterns = [

   path('', News.as_view(), name='news_page'),
   path('<int:pk>', NewsDetail.as_view(), name='news'),
   path('search/', NewsSearch.as_view(), name='news_search'),
   path('create/', PostCreate.as_view(), name='news_create'),
   path('<int:pk>/edit/', PostEdit.as_view(), name='news_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
  ]

