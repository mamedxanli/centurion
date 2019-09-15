#Django native imports
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views import generic

# Import from our apps
from money.forms import MoneyInForm, MoneyOutForm
from money.models import MoneyIn, MoneyOut


class MoneyInCreate(generic.CreateView):
    model = MoneyIn
    form_class = MoneyInForm   
    template_name = 'money/money_in_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user.username
        obj.save()
        messages.success(self.request, _('Item successfully created'))
        return HttpResponseRedirect('list')

class MoneyOutCreate(generic.CreateView):
    model = MoneyOut
    form_class = MoneyOutForm   
    template_name = 'money/money_out_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user.username
        obj.save()
        messages.success(self.request, _('Item successfully created'))
        return HttpResponseRedirect('list')


class MoneyInList(generic.ListView):
    """
    List view for the items
    """
    model = MoneyIn
    template_name = 'money/money_in_list.html'
    paginate_by = 50

class MoneyOutList(generic.ListView):
    """
    List view for the items
    """
    model = MoneyOut
    template_name = 'money/money_out_list.html'
    paginate_by = 50


class MoneyInDetail(generic.DetailView):
    """
    Detail view for a single server. This view is shown on the webpage 
    when user clicks on a single server in "Server list" page
    """

    model = MoneyIn
    template_name = 'money/money_in_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(MoneyInDetail, self).get(request, *args, **kwargs)

class MoneyOutDetail(generic.DetailView):
    """
    Detail view for a single server. This view is shown on the webpage 
    when user clicks on a single server in "Server list" page
    """

    model = MoneyOut
    template_name = 'money/money_out_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(MoneyOutDetail, self).get(request, *args, **kwargs)


class MoneyInDelete(generic.DeleteView):
    model = MoneyIn
    success_url = reverse_lazy('money_in_list')

class MoneyOutDelete(generic.DeleteView):
    model = MoneyOut
    success_url = reverse_lazy('money_out_list')


class MoneyInUpdate(generic.UpdateView):
    """
    Update view for server edit page. Upon clicking "Edit" button on the
    item view page, user will be able to update a server by utilising
    this view.
    """

    model = MoneyIn
    form_class = MoneyInForm
    template_name_suffix = '_update_form'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        #if not request.user.is_authenticated():
        #    return HttpResponseRedirect(reverse('login', args=(request.user.id,)))
        return super(MoneyInUpdate, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        If the form is valid, save the associated model
        """
        obj = form.save(commit=False)
        obj.created_by = self.request.user.username
        obj.save()
        messages.success(self.request, _('Item successfully updated'))
        return render(self.request, 'money/money_in_update_form.html', {'form': form})

class MoneyOutUpdate(generic.UpdateView):
    """
    Update view for server edit page. Upon clicking "Edit" button on the
    item view page, user will be able to update a server by utilising
    this view.
    """

    model = MoneyOut
    form_class = MoneyOutForm
    template_name_suffix = '_update_form'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        #if not request.user.is_authenticated():
        #    return HttpResponseRedirect(reverse('login', args=(request.user.id,)))
        return super(MoneyOutUpdate, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        If the form is valid, save the associated model
        """
        obj = form.save(commit=False)
        obj.created_by = self.request.user.username
        obj.save()
        messages.success(self.request, _('Item successfully updated'))
        return render(self.request, 'money/money_out_update_form.html', {'form': form})