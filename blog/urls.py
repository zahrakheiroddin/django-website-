from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
# post views
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail'),
    path('danestani/', views.news, name='news'),
    path('<int:id>/<slug:slug>/', views.news_detail,name='news_detail'),

]
