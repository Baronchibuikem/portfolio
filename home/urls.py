from django.urls import path
from home.views import home

urlpatterns = [
    # this renders the create_medical_record view which is a form for users to fill
    path('', home, name='home'),
]