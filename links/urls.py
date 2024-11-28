from django.urls import path

from . import views


app_name = 'links'

urlpatterns = [
    path('', views.UserLinksListView.as_view(), name='user_links_list'),
    path('<str:short_link>/', views.redirect_to_link, name='redirect_to_link'),
    path('create/', views.CreateLinkView.as_view(), name='create_link'),
]
