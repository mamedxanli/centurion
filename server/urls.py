#Django native imports
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import edit

# Import from our apps
from server import views

urlpatterns = [
    url(r'^$', login_required(views.ServerHardwareCreate.as_view()), name='server_hw_create'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(views.ServerHardwareUpdate.as_view()), name='server_hw_edit'),
    url(r'^list$', login_required(views.ServerHardwareList.as_view()), name='server_hw_list'),
    url(r'^sold_list$', login_required(views.ServerHardwareSoldList.as_view()), name='server_hw_sold_list'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(views.ServerHardwareDelete.as_view()), name='server_hw_delete'),
    url(r'^(?P<pk>\d+)/$', login_required(views.ServerHardwareDetail.as_view()), name='server_hw_detail'),
              ]