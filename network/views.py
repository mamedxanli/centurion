#Django native imports
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views import generic

# Import from our apps
from network.forms import NetworkHardwareForm
from network.models import NetworkHardware


class NetworkHardwareCreate(generic.CreateView):
    model = NetworkHardware
    form_class = NetworkHardwareForm   
    template_name = 'network/network_hw_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user.username
        obj.save()
        messages.success(self.request, _('Item successfully created'))
        return HttpResponseRedirect('list')


class NetworkHardwareUpdate(generic.UpdateView):
    """
    Update view for server edit page. Upon clicking "Edit" button on the
    item view page, user will be able to update a server by utilising
    this view.
    """

    model = NetworkHardware
    form_class = NetworkHardwareForm
    #template_name_suffix = '_update_form'
    template_name = 'network/network_hw_update_form.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        #if not request.user.is_authenticated():
        #    return HttpResponseRedirect(reverse('login', args=(request.user.id,)))
        return super(NetworkHardwareUpdate, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        If the form is valid, save the associated model
        """
        obj = form.save(commit=False)
        obj.created_by = self.request.user.username
        obj.save()
        messages.success(self.request, _('Item successfully updated'))
        return render(self.request, 'network/network_hw_update_form.html', {'form': form})


class NetworkHardwareList(generic.ListView):
    """
    List view for the items
    """
    model = NetworkHardware
    template_name = 'network/network_hw_list.html'
    paginate_by = 50
    
    def get_queryset(self):
        qs = NetworkHardware.objects.filter(sold=False,inventory=False)
        return qs.order_by('code')
    
class NetworkHardwareSoldList(generic.ListView):
    model = NetworkHardware
    template_name = 'network/network_hw_sold_list.html'
    paginate_by = 50

    def get_queryset(self):
        qs = NetworkHardware.objects.filter(sold=True)
        return qs.order_by('code')


class NetworkHardwareInventoryList(generic.ListView):
    model = NetworkHardware
    template_name = 'network/network_hw_inventory_list.html'
    paginate_by = 50

    def get_queryset(self):
        qs = NetworkHardware.objects.filter(inventory=True)
        return qs.order_by('code')

class NetworkHardwareDetail(generic.DetailView):
    """
    Detail view for a single server. This view is shown on the webpage 
    when user clicks on a single server in "Server list" page
    """

    model = NetworkHardware
    template_name = 'network/network_hw_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(NetworkHardwareDetail, self).get(request, *args, **kwargs)


class NetworkHardwareDelete(generic.DeleteView):
    model = NetworkHardware
    success_url = reverse_lazy('network_hw_list')
