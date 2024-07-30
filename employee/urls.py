from django.urls import path
from .views import EmployeeCreateView, EmployeeListView, EmployeeDetailView

urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('employees/create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
]