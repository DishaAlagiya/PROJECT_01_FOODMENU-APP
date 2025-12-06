from . import views
from django.views.decorators.cache import cache_page
from django.urls import path
app_name = 'food'
urlpatterns = [

    #path('',cache_page(60*2) (views.index), name='index'),        #cache as URL Level
    path('', views.index, name='index'),
   # path('', views.IndexClassView.as_view(), name='index'),
    path('<int:id>/', views.detail, name='detail'),
    #path('<int:pk>/',views.Detail.as_view(), name='detail'),
    path('add/',views.create_item, name='itemform'),
    #path('add/',views.ItemCreateView.as_view(), name='itemform'),
    #path('update/<int:id>/',views.update_item, name='update_item'),
    path('update/<int:pk>/',views.ItemUpdate.as_view(), name='update_item'),
    path('delete/<int:id>/',views.delete_item, name='delete_item'),
    #path('delete/<int:pk>/',views.ItemDelete.as_view(), name='delete_item'),
]
