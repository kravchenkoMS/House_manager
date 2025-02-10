from django.urls import path

from . import views

urlpatterns = [
    path('login_m', views.show_login_m, name="login_m"),
    path('moderator_page', views.show_moderator_page, name="moderator_page"),
    path('register_resident_m', views.show_register_resident_m, name="register_resident_m"),
    path('remove_resident_m', views.ResidentDeleteViewModerator.as_view(), name="remove_resident_m"),
    path('register_flat_m', views.show_register_flat_m, name="register_flat_m"),
    path('remove_flat_m', views.FlatDeleteView.as_view(), name="remove_flat_m"),
    path('edit_resident_m', views.ResidentUpdateViewModerator.as_view(), name="resident_update_m"),
    path('edit_flat_m', views.FlatUpdateView.as_view(), name="edit_flat_m"),
    path('flats_list_m', views.show_flats_list_m, name="flats_list_m"),
    path('residents_list_m', views.show_residents_list_m, name="residents_list_m"),
    path('choose_table_m', views.show_choose_table_m, name="choose_table_m"),
    path('choose_table_m/export_residents_info', views.export_residents_info_m, name="export_residents_info"),
    path('choose_table_m/export_flats_info', views.export_flat_info_m, name="export_flats_info"),
    path('choose_table_m/import_residents', views.import_residents, name="import_residents"),
    path('choose_table_m/import_flats', views.import_flats, name="import_flats")
]