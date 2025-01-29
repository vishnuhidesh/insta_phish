from django.urls import path
from .views import login_page, view_captured_data  # Ensure this line is correct

urlpatterns = [
    path('', login_page, name='login'),
    path('captured/', view_captured_data, name='captured_data'),
]
