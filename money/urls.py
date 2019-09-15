#Django native imports
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import edit

# Import from our apps
from money import views

urlpatterns = [
    url(r'^moneyin$', login_required(views.MoneyInCreate.as_view()), name='money_in_create'),
    url(r'^moneyinedit/(?P<pk>\d+)/$', login_required(views.MoneyInUpdate.as_view()), name='money_in_edit'),
    url(r'^moneyinlist$', login_required(views.MoneyInList.as_view()), name='money_in_list'),
    url(r'^moneyindelete/(?P<pk>\d+)/$', login_required(views.MoneyInDelete.as_view()), name='money_in_delete'),
    url(r'^moneyin(?P<pk>\d+)/$', login_required(views.MoneyInDetail.as_view()), name='money_in_detail'),
    url(r'^moneyout$', login_required(views.MoneyOutCreate.as_view()), name='money_out_create'),
    url(r'^moneyoutedit/(?P<pk>\d+)/$', login_required(views.MoneyOutUpdate.as_view()), name='money_out_edit'),
    url(r'^moneyoutlist$', login_required(views.MoneyOutList.as_view()), name='money_out_list'),
    url(r'^moneyoutdelete/(?P<pk>\d+)/$', login_required(views.MoneyOutDelete.as_view()), name='money_out_delete'),
    url(r'^moneyout(?P<pk>\d+)/$', login_required(views.MoneyOutDetail.as_view()), name='money_out_detail'),
              ]