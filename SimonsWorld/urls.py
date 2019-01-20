from django.contrib import admin
from django.urls import path
from SimonsWorld import view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", view.index),
    path("about/",view.about),
    path("contact/",view.contact),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


