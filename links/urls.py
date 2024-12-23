from django.urls import path

from . import views


app_name = 'links'

urlpatterns = [
    path('', views.UserLinksListView.as_view(), name='user_links_list'),
    path('create/', views.CreateLinkView.as_view(), name='create_link'),
    path('top/', views.TopUserLinksView.as_view(), name='top_links'),
    path('delete/<int:link_id>/', views.DeleteUserLinkView.as_view(), name='delete_link'),
    path('complaint/', views.CreateComplaintView.as_view(), name='create_complaint'),
    path('<str:short_link>/', views.redirect_to_link, name='redirect_to_link'),
]
