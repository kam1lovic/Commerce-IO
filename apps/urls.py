from django.urls import include, path

urlpatterns = [
    path('users/', include('users.urls')),
    path('shop/', include('shops.urls')),
]
