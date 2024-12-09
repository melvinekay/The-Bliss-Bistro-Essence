"""
URL configuration for BlissBistro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BlissBistroApp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index', views.index, name='index'),
    path('', views.home, name='home'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('specials/', views.specials, name='specials'),
    path('events/', views.events, name='events'),
    path('gallery/', views.gallery, name='gallery'),
    path('chefs/', views.chefs, name='chefs'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('showb/', views.showB, name='showb'),
    path('showc/', views.showC, name='showc'),
    path('delete/<int:id>', views.delete),
    path('deleteorder/<int:id>', views.deleteorder, name='deleteorder'),
    path('deleteorder/all', views.delete_all_orders_view, name='delete_all_orders'),
    path('editorder/all', views.edit_all_orders_view, name='edit_all_orders'),
    path('updateorder/all', views.update_all_orders_view, name='update_all_orders'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('editorder/<int:id>', views.editorder, name='editorder'),
    path('update/<int:id>', views.update, name='update'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logincont/', views.logincont, name='logincont'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('subscribe/', views.starter, name='starter'),
    path('summary/', views.summary_view, name='summary'),
    path('order/', views.order_view, name='order'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('clearsession/', views.clear_session_view, name='clear_session'),
]
