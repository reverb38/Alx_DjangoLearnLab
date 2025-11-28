from django.contrib import admin
from django.urls import path, include  # include lets us add app URLs

urlpatterns = [
    path('admin/', admin.site.urls),                # default admin
    path('', include('relationship_app.urls')),    # include app URLs
]
