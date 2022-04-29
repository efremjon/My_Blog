from unicodedata import name
from django.urls import path

from .views import HomeViews,DetielView,AddPost,UpdatePost,DeletePost,AddCatagory,CatagorView,likeView
urlpatterns = [
    path('',HomeViews.as_view(),name="home"),
    path('article/<int:pk>/',DetielView.as_view(),name="detile"),
    path('addpost/',AddPost.as_view(),name="add_post"),
    path('article/update/<int:pk>/',UpdatePost.as_view(),name="update"),
    path('article/<int:pk>/remove/',DeletePost.as_view(),name="delete"),
    path('addCatagory/',AddCatagory.as_view(),name="add_catagory"),
    path('catagory/<int:id>/',CatagorView,name="catagory"),
    path('like_post/<int:post_id>/', likeView,name='like_post')
]
