from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'hello'

urlpatterns = [
    #/hello/
    path('', views.IndexView.as_view(), name="index"),

    #/hello/712/
    path('<pk>/',views.DetailView.as_view(), name='detail'),

    #hello/album/add/
    path('album/add/',views.AlbumCreate.as_view(), name='album-add'),

    #hello/album/2/
    path('album/<pk>/',views.AlbumUpdate.as_view(), name='album-update'),

    #hello/album/2/delete
    path('album/<pk>/delete/',views.AlbumDelete.as_view(), name='album-delete'),

    #/hello/register/
    path('user/register/', views.UserFormView.as_view(), name="register"),
]
