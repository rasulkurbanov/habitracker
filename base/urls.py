from django.urls import path
from .views import TaskCreate, TaskDelete, TaskUpdate, TasksList, TaskDetail

urlpatterns = [
    path('', TasksList.as_view(), name='tasks'),
    path('task-create', TaskCreate.as_view(), name='task-create'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task-detail'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete')
]
