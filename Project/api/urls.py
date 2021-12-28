from django.urls import path, include
from .views import HelloView, TagDetail, TagList,overview,SnippetList,SnippetDetail

urlpatterns = [
    path('snippet' , SnippetList.as_view()),
    path('snippet/<int:pk>' , SnippetDetail.as_view()),
    path('tag' , TagList.as_view()),
    path('tag/<int:pk>' , TagDetail.as_view()),
    path('', overview),
]
