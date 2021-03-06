from django.conf.urls import url
from django.views.generic import TemplateView

from .views import HomeView
from .views.config import RecalboxConfigFormView
from .views.logs import LogsView
from .views.bios import BiosListView
from .views.roms import SystemsListView, RomListView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    
    url(r'^bios/$', BiosListView.as_view(), name='bios'),
    
    url(r'^config/$', RecalboxConfigFormView.as_view(), name='config'),
    
    url(r'^logs/$', LogsView.as_view(), name='logs'),
    
    url(r'^systems/$', SystemsListView.as_view(), name='roms-systems'),
    url(r'^systems/roms/(?P<system>\w+)/$', RomListView.as_view(), name='roms-list'),
]