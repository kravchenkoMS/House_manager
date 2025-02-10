from django.urls import path

from . import views

urlpatterns = [
    path('login_r', views.show_login_r, name="login_r"),
    path('register_resident', views.show_register_r, name="register_resident"),
    path('<int:resident_id>/resident_page', views.show_resident_page, name="resident_page"),
    path('<int:resident_id>/flats_list_m', views.show_flats_list_r, name="flats_list_r"),
    path('<int:resident_id>/residents_list_m', views.show_residents_list_r, name="residents_list_r"),
    path('<int:resident_id>/remove_resident', views.ResidentDeleteView.as_view(), name="remove_resident"),
    path('<int:resident_id>/edit_resident', views.ResidentUpdateView.as_view(), name="resident_update"),
    path('<int:resident_id>/choose_table_r', views.show_choose_table_r, name="choose_table_r"),
    path('<int:resident_id>choose_table_r/residents_with_cars', views.export_residents_with_cars, name="residents_with_cars"),
    path('<int:resident_id>choose_table_r/residents_with_pets', views.export_residents_with_pets, name="residents_with_pets"),
    path('<int:resident_id>choose_table_r/residents_info', views.export_residents_info, name="residents_info"),
    path('<int:resident_id>choose_table_r/flats_info', views.export_flat_info, name="flats_info"),
]