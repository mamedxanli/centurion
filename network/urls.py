#Django native imports
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import edit

# Import from our apps
from network import views

urlpatterns = [
    url(r'^$', login_required(views.NetworkHardwareCreate.as_view()), name='network_hw_create'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(views.NetworkHardwareUpdate.as_view()), name='network_hw_edit'),
    url(r'^list$', login_required(views.NetworkHardwareList.as_view()), name='network_hw_list'),
    url(r'^inventory_list$', login_required(views.NetworkHardwareInventoryList.as_view()), name='network_hw_inventory_list'),
    url(r'^sold_list$', login_required(views.NetworkHardwareSoldList.as_view()), name='network_hw_sold_list'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(views.NetworkHardwareDelete.as_view()), name='network_hw_delete'),
    url(r'^(?P<pk>\d+)/$', login_required(views.NetworkHardwareDetail.as_view()), name='network_hw_detail'),
              ]
