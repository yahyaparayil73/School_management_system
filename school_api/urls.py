from django.urls import path
from . import views
app_name = 'school_api'
urlpatterns = [
    path('add_student',views.addStudent,name = 'add_student'),
    path('view_student',views.viewStudent,name = 'view_student'),
    path('update_student/<int:student_id>',views.updateStudent,name = 'update_student'),
    path('delete_student/<int:student_id>',views.deleteStudent,name = 'delete_student'),

]
