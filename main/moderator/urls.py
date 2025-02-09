from django.urls import path

from . import views

urlpatterns = [
    path('login_m', views.show_login_m, name="login_m"),
    path('moderator_page', views.show_moderator_page, name="resident_page"),
    path('register_resident_m', views.show_register_resident_m, name="register_resident_m"),
    path('remove_resident_m', views.ResidentDeleteViewModerator.as_view(), name="remove_resident_m"),
    path('remove_flat_m', views.FlatDeleteView.as_view(), name="remove_flat_m"),
    path('edit_resident_m', views.ResidentUpdateViewModerator.as_view(), name="resident_update_m"),
    path('edit_flat_m', views.FlatUpdateView.as_view(), name="edit_flat_m"),
    path('choose_table_m', views.show_choose_table_m, name="choose_table_m")
]