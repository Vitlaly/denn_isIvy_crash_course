
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
               path('', views.home, name='home'),
               path('products/', views.products, name='products'),
               path('customer/<str:id_customer>/', views.customer, name='customer'),

               path('create_order/<str:pk>/', views.create_order, name='create_order'),
               path('update_order/<str:pk>/', views.update_order, name='update_order'),
               path('delete_order/<str:pk>/', views.delete_order, name='delete_order'),

               path('register/', views.register, name='register'),
               path('login_page/', views.login_page, name='login'),
               path('logout/', views.logout_user, name='logout'),

               path('user/', views.user_page, name='user_page'),
               path('account/', views.account_settings, name='account'),

               path('reset_password/',
                    auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
                    name='reset_password'),

               path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),
                    name='password_reset_done'),

               path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'),
                    name='password_reset_confirm'),

               path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'),
                    name='password_reset_complete'),

               ]

# auth_views.PasswordChangeView.as_view() - submit email form
#
# auth_views.PasswordResetDoneView.as_view() - Email sent success message
#
# auth_views.PasswordResetConfirmView.as_view() - link to password Rest form in email
#
# auth_views.PasswordResetView.as_view() - Password succesfully changed message
