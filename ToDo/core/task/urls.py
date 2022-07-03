from django.urls import path
from . import views

urlpatterns =[path('create/',views.CreateTask.as_view(),name='create_new_Task'),
              path('list/',views.TasksList.as_view(),name='tasks_list'),
              path('done/<int:pk>/',views.ChangeToDone.as_view(),name='change_task_status_done'),
              path('update/<int:pk>/',views.UpdateTask.as_view(),name='update_task'),
              path('delete/<int:pk>/',views.DeleteTAsk.as_view(),name='delete_task'),


]