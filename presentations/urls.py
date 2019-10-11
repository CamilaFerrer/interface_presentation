from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PresentationCreate.as_view(), name='presentation-new'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.PresentationUpdate.as_view(), name='presentation-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.PresentationDelete.as_view(), name='presentation-delete'),
    url(r'^(?P<pk>[0-9]+)/view/$', views.presentation_view, name='presentation-view'),
]

urlpatterns += [
    url(r'^(?P<pk>[0-9]+)/slides/$', views.SlideCreate.as_view(), name='slides-view'),
    url(r'^(?P<pk>[0-9]+)/new-slide/$', views.SlideCreate.as_view(), name='slide-new'),
    url(r'^(?P<pk>[0-9]+)/update-slide/$', views.SlideUpdate.as_view(), name='slide-update'),
    url(r'^(?P<pk>[0-9]+)/delete-slide/$', views.SlideDelete.as_view(), name='slide-delete'),
    url(r'^(?P<pk>[0-9]+)/preview/$', views.slide_preview, name='slide-preview'),
]
