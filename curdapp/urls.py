from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentList.as_view(), name='student_list'),
    path('view/<int:pk>', views.StudentView.as_view(), name='student_view'),
    path('new', views.StudentCreate.as_view(), name='student_new'),
    path('view/<int:pk>', views.StudentView.as_view(), name='student_view'),
    path('edit/<int:pk>', views.StudentUpdate.as_view(), name='student_edit'),
    path('delete/<int:pk>', views.StudentDelete.as_view(), name='student_delete')

]