from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    path('', views.index, name='blog_index'),  # name='blog_index' 这是反向查询名 打开网页就是127.0.0.1:8000/blog/
    path('<int:blog_id>/', views.detail, name='blog_detail'), # 打开网页点击了条目1 就是127.0.0.1:8000/blog/1
    path('<int:category_id>/category/', views.category, name='blog_category'),
    path('<int:tag_id>/tag/', views.tag, name='blog_tag'),
    path('search/', views.search, name='blog_search'),
    path('<int:year>/<int:month>/archives/', views.archives, name='blog_archives'),
    path('<int:comment_id>/reply/', views.reply, name='comment_reply')
]