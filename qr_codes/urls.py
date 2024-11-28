from django.urls import path

from . import views


app_name = 'qr_codes'

urlpatterns = [
    path('', views.UserQRCodesListView.as_view(), name='user_qr_codes_list'),
    path('create/', views.CreateQRCodeView.as_view(), name='create_qr_code'),
    path('delete/<int:qr_id>/', views.DeleteUserQRCodeView.as_view(), name='delete_qr_code')
]
