from django.contrib import admin
from django.urls import path
from SimonsWorld import view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", view.index)
    path('home', view.index),
    path('travel', view.second),
    path('contact',view.connect_with_me),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


