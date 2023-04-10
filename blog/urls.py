from django.urls import path
from  blog import views

app_name = 'blog'


urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:post_id>', views.blog_detalle, name='blog_Detalle')

]