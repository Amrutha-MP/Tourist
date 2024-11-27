from django.urls import path
from tourapp import views

urlpatterns=[
    path('adminpage/',views.admin,name="adminpage"),
    path('add_category/',views.add_category,name="add_category"),
    path('save_category/',views.Save_category,name="save_category"),
    path('view_category/',views.view_category,name="view_category"),
    path('edit_category/<int:cat_id>/',views.edit_category,name="edit_category"),
    path('update_category/<int:cat_id>/',views.update_category,name="update_category"),
    path('delete_category//<int:cat_id>/',views.delete_category,name="delete_category"),
    path('add_package/',views.add_package,name="add_package"),
    path('save_package/',views.save_package,name="save_package"),
    path('view_package/',views.view_package,name="view_package"),
    path('edit_package/<int:pack_id>/',views.edit_package,name="edit_package")
]