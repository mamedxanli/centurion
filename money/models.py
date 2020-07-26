#Django native imports
from django.db import models
from django.urls import reverse, reverse_lazy
from datetime import datetime

# Import from our apps
from network.models import NetworkHardware

class Money(models.Model):
    # Timestamps
    date = models.DateTimeField("Tarix")
    amount = models.DecimalField("Məbləğ", decimal_places=2, max_digits=10)
    description = models.TextField("Təsvir", max_length=500, default=None)
    incoming = models.BooleanField("Mədaxil", default=False)
    
    #This class should be done as abstract possibly?
    #Another option is to override amount in the derived class
    
    def __str__(self):
        return " {} ".format(self.date)

    def get_absolute_url(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('money_edit', args=[str(self.pk)])

    def get_detail(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('money_detail', args=[str(self.pk)])

    def get_delete(self):
        """
        Handy way of getting the url of the object to its delete view page
        """
        return reverse('money_delete', args=[str(self.pk)])

    def get_class(self):
        """
        Handy way of getting the class of the object for the html templates
        """
        class_name = "Pul"
        return class_name

    def get_money_for_month(self):
        qs = Money.objects.filter(date__month = datetime.now().month, date__year = datetime.now().year)
        money_amount = 0
        for item in qs:
            money_amount = money_amount + item.amount
        return money_amount

    def get_total_stock(self):
        qs = NetworkHardware.objects.filter(sold=False, inventory=False)
        total_stock_value = 0
        for item in qs:
            total_stock_value = total_stock_value + item.selling_price*item.quantity
        return total_stock_value
    
    def get_purchase_price_stock(self):
        qs = NetworkHardware.objects.filter(sold=False, inventory=False)
        total_purchase_price_value = 0
        for item in qs:
            total_purchase_price_value = total_purchase_price_value + item.purchase_price*item.quantity
        return total_purchase_price_value

    class Meta:
        verbose_name_plural = "Money"
    
