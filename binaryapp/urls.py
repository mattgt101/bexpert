from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ),
    path('about/', views.about),
    path('event/', views.event),
    path('faq/', views.faq),
    path('contact/', views.contact),
    path('signup/', views.signup),
    path('login/', views.login),
    path('account/', views.account),
    path('profile/', views.profile),
    path('verification/', views.verification),
    path('upgrade/', views.upgrade),
    path('fund/', views.fund),
    path('admin/', views.admin),
    path('edit/', views.edit),
    path('site/', views.site),

]
