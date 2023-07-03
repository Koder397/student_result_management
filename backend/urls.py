from django.urls import path

from backend.views import dashboard, login, staff_logout, TaskList, TaskUpdate, TaskDelete, TaskCreate

urlpatterns = [
    path('login', login, name='staff_login'),
    path('logout', staff_logout, name='staff_logout'),
    path('table/', TaskList.as_view(), name='task_list'),
    path('table/<pk>/task_update', TaskUpdate.as_view(), name='task_update'),
    path('table/<pk>/task_delete', TaskDelete.as_view(), name='task_delete'),
    path('create', TaskCreate.as_view(), name='task_create'),
    path('', dashboard, name='dashboard'),
]