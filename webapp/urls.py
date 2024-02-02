from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contacts/', views.contacts, name="contacts"),
    path('login/', views.login_create, name="login"),
    path('login_store', views.login_store),
    path('user_logout/', views.user_logout ),
    path('announcement_form/', views.create_announcement, name="create_announcement"),
    path('announcement/<int:pk>/edit/', views.announcement_edit, name='announcement_edit'),
    path('announcement/<int:pk>/delete/', views.announcement_delete, name='announcement_delete'),
    path('announcement_detail/<int:pk>', views.announcement_detail, name="announcement_detail"),
    path('announcement_list/', views.announcement_list, name="announcement_list"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('resident_form/', views.register_resident, name="register_resident"),
    path('resident/<int:pk>/edit/', views.resident_edit, name='resident_edit'),
    path('resident/<int:pk>/delete/', views.resident_delete, name='resident_delete'),   
    path('resident_detail/<int:pk>', views.resident_detail, name="resident_detail"),
    path('resident_list/', views.resident_list, name="resident_list"),
]

