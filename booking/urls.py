from booking import views
from django.urls import include, path

urlpatterns = [
    path('admin/', views.rooms_list),
    include('booking.urls', namespace='booking'),
]
