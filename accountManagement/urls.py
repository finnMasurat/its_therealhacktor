from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login_page, name='login'),
    url(r'^home', views.home, name='home'),
    url(r'^changeEmail', views.change_email_view, name='changeEmail'),
    url(r'^changePassword', views.change_password_view, name='changePassword'),
    url(r'^logout', views.logout_view, name='logout'),
]
