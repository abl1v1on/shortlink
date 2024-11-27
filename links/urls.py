from django.urls import path

from . import views


app_name = 'links'

urlpatterns = [
    path('', views.UserLinksListView.as_view(), name='user_links_list'),
]
