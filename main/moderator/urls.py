from django.urls import path

from . import views

urlpatterns = [
    path('login_m', views.show_login_m, name="login_m"),
    path('moderator_page', views.show_moderator_page, name="moderator_page"),
    path('register_resident_m', views.show_register_resident_m, name="register_resident_m"),
    path('remove_resident_m/<int:pk>', views.ResidentDeleteViewModerator.as_view(), name="remove_resident_m"),
    path('register_flat_m', views.show_register_flat_m, name="register_flat_m"),
    path('remove_flat_m/<int:pk>', views.FlatDeleteView.as_view(), name="remove_flat_m"),
    path('edit_resident_m/<int:pk>', views.ResidentUpdateViewModerator.as_view(), name="edit_resident_m"),
    path('edit_flat_m/<int:id>', views.FlatUpdateView.as_view(), name="edit_flat_m"),
    path('flats_list_m', views.show_flats_list_m, name="flats_list_m"),
    path('residents_list_m', views.show_residents_list_m, name="residents_list_m"),
    path('choose_table_m', views.show_choose_table_m, name="choose_table_m"),
    path('choose_table_m/export_residents_info_m', views.export_residents_info_m, name="export_residents_info_m"),
    path('choose_table_m/export_flats_info_m', views.export_flat_info_m, name="export_flats_info_m"),
    path('choose_table_m/import_residents_m', views.import_residents_m, name="import_residents_m"),
    path('choose_table_m/import_flats_m', views.import_flats_m, name="import_flats_m")
]