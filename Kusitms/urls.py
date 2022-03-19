from django.urls import path
from . import views #뷰에 있는 모든 함수 가져오기.
app_name = 'Kusitms'

urlpatterns = [
    path('',view = views.post_list, name = 'list'), #/posts
    path('<int:pk>/', view=views.post_detail, name = 'detail'), #/posts/1
    path('create/', view= views.post_create, name = 'create'),
    path('<int:pk>/delete', view=views.post_delete, name = 'delete'),
    path('<int:pk>/update', view = views.post_update, name = 'update'),
]