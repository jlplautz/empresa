from django.urls import imclude, path


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]

