from django.urls import path
from . import views
from .views import CustomPasswordChangeView

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history,
         name='order_history'),
    path('accounts/password/change/',
         CustomPasswordChangeView.as_view(),
         name='account_change_password'),
]
