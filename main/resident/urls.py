from django.urls import path

from . import views

urlpatterns = [
    path('login_r', views.show_login_r, name="login_r"),
    path('register_resident_r', views.show_register_resident_r, name="register_resident_r"),
    path('<int:resident_id>/resident_page', views.show_resident_page, name="resident_page"),
    path('<int:resident_id>/flats_list_r', views.show_flats_list_r, name="flats_list_r"),
    path('<int:resident_id>/residents_list_r', views.show_residents_list_r, name="residents_list_r"),
    path('remove_resident_r/<int:pk>/', views.ResidentDeleteView.as_view(), name="remove_resident_r"),
    path('edit_resident_r/<int:pk>/', views.ResidentUpdateView.as_view(), name="edit_resident_r"),
    path('<int:resident_id>/choose_table_r', views.show_choose_table_r, name="choose_table_r"),
    path('choose_table_r/residents_with_cars', views.export_residents_with_cars, name="export_residents_with_cars"),
    path('choose_table_r/residents_with_pets', views.export_residents_with_pets, name="export_residents_with_pets"),
    path('choose_table_r/residents_info', views.export_residents_info, name="export_residents_info"),
    path('choose_table_r/flats_info', views.export_flat_info, name="export_flats_info"),
    path('choose_table_r/rented_flats', views.export_rented_flats, name="export_bought_flats")
]