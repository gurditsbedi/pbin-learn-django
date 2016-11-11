from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^psub/$', views.formSubmit, name='formSubmit'),
    url(r'^verr/$', views.verr, name='verr'), #verr -> Validation Error
    url(r'^(?P<slug>[a-zA-Z0-9]{5,})/$', views.paste, name='paste')
]

