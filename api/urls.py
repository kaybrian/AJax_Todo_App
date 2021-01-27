from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview,name="apioverview"),
    path('task-list/',views.tasklist,name='task-list')
]



