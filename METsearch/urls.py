
from django.contrib import admin
from django.urls import path
from home.views import*
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home,name ='home'),
    path('',index,name ='index'),
    path('allbus',allbus,name ='Allbus'),
    path('addBuses',addBuses,name ='addBuses'),
    path('register', register_request, name='register'),
    path('signup/',signup_view, name='signup'),
    path('login/',login_view, name='login'),
    path('logout',logout_view, name='logout'),
    path('route/',bus_route,name='add_route'),
    path('stopage/',bus_stopage,name='add_stopage'),
    path('busdetails/<int:pk>',bus_details,name='bus_details'),
    
    
    # path('password-change',password_change_view, name='password_change'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='home/password_reset_form.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='home/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='home/password_reset_confirm.html',success_url ='/login'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='home/password_reset_complete.html'),name='password_reset_complete'),
    path('change/',auth_views.PasswordChangeView.as_view(template_name='home/password_change.html',success_url ='/login'),name='password_change'),
    # path('change/',auth_views.PasswordChangeView.as_view(template_name='home/password_change.html')
    

]
