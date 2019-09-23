#Django native imports
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views import generic

# Import from our apps
from server.forms import ServerHardwareForm
from server.models import ServerHardware


class ServerHardwareCreate(generic.CreateView):
    model = ServerHardware
    form_class = ServerHardwareForm   
    template_name = 'server/server_hw_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user.username
        obj.save()
        messages.success(self.request, _('Item successfully created'))
        return HttpResponseRedirect('list')


class ServerHardwareUpdate(generic.UpdateView):
    """
    Update view for server edit page. Upon clicking "Edit" button on the
    item view page, user will be able to update a server by utilising
    this view.
    """

    model = ServerHardware
    form_class = ServerHardwareForm
    template_name = 'server/server_hw_update_form.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        #if not request.user.is_authenticated():
        #    return HttpResponseRedirect(reverse('login', args=(request.user.id,)))
        return super(ServerHardwareUpdate, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        If the form is valid, save the associated model
        """
        obj = form.save(commit=False)
        obj.created_by = self.request.user.username
        obj.save()
        messages.success(self.request, _('Item successfully updated'))
        return render(self.request, 'server/server_hw_update_form.html', {'form': form})


class ServerHardwareList(generic.ListView):
    """
    List view for the items
    """
    model = ServerHardware
    template_name = 'server/server_hw_list.html'
    paginate_by = 50
    
    def get_queryset(self):
        qs = ServerHardware.objects.all()
        return qs.order_by('-code')
    
class ServerHardwareSoldList(generic.ListView):
    model = ServerHardware
    template_name = 'server/server_hw_sold_list.html'
    paginate_by = 50

    def get_queryset(self):
        qs = ServerHardware.objects.filter(sold=True)
        return qs.order_by('code')

class ServerHardwareDetail(generic.DetailView):
    """
    Detail view for a single server. This view is shown on the webpage 
    when user clicks on a single server in "Server list" page
    """

    model = ServerHardware
    template_name = 'server/server_hw_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(ServerHardwareDetail, self).get(request, *args, **kwargs)


class ServerHardwareDelete(generic.DeleteView):
    model = ServerHardware
    success_url = reverse_lazy('server_hw_list')
