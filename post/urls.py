from django.urls import path
from .views import post_list_view,post_detail_page,post_create,post_update,post_delete
urlpatterns = [
    path('',post_list_view,name='list'),
    path('create/',post_create,name='post-create'),
    path('detail/<slug:slug>/',post_detail_page,name='post-detail'),
    path('update/<slug:slug>/',post_update,name='post-update'),
    path('delete/<slug:slug>/',post_delete,name='post-delete'),
]