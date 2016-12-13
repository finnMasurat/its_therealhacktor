from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login_page, name='login'),
    url(r'^home', views.home, name='home'),
    url(r'^changeEmail', views.change_email, name='changeEmail'),
    url(r'^changePassword', views.change_password, name='changePassword'),
    url(r'^logout', views.logout_view, name='logout'),
]
