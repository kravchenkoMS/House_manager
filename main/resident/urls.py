from django.urls import path

from . import views

urlpatterns = [
    path('login_r', views.show_login_r, name="login_r"),
    path('<int:resident_id>/choose_table_r', views.show_choose_table_r, name="choose_table_r"),
    path('<int:resident_id>/resident_page', views.show_resident_page, name="resident_page"),
    path('register_resident', views.show_register_r, name="register_resident"),
    path('<int:resident_id>/remove_resident', views.ResidentDeleteView.as_view(), name="remove_resident"),
    path('<int:resident_id>/edit_resident', views.ResidentUpdateView.as_view(), name="resident_update")
]

# todo: додати необхідні розділи