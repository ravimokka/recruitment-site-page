from django.urls import path
from . import views

urlpatterns = [

    path('',views.Homepage, name='Homepage'),
    path('login',views.Login, name='Login'),
    path('index',views.Index, name='Index'),
    path('view_profile',views.View_Profile, name='View_Profile'),
    # path('test',views.index, name='base'),
    # url(r'^countries/$',views.get_countries, name='Homepage'),
    # url(r'^domains/$',views.get_domains, name='Homepage'),
    # url(r'^organisations/$',views.get_organisations, name='Homepage'),
    # url(r'^co_state_data/$',views.get_add_country_state_datalist, name='Homepage'),
    # url(r'^add_new_cou/$',views.add_new_countries, name='Homepage'),
    # url(r'^sam/$',views.get_country_domains, name='Homepage'),

]