#Django native imports
from django.db import models
from django.urls import reverse, reverse_lazy
from django.db.models import Sum

# Import from our apps

def save_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/clothes/<code>/<filename>
    return '{0}/{1}/{2}'.format("network_hw", instance.code, filename)

class NetworkHardware(models.Model):
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100, default=None)

    # Model
    code = models.IntegerField("Kod", primary_key=True)
    brand = models.CharField("Brend", max_length=20, default=None)
    model = models.CharField("Model", max_length=50)
    serial_number = models.CharField("Seriya Nömrəsi", max_length=50, default=None)
    category = models.CharField("Kateqoriya", max_length=30, default=None)
    description = models.TextField("Təsvir", max_length=500, default=None)
    purchase_price = models.DecimalField("Alış qiməti", decimal_places=2, max_digits=10)
    selling_price = models.DecimalField("Satış qiyməti", decimal_places=2, max_digits=10)
    quantity = models.IntegerField("Ədəd", default=1)
    image = models.FileField("Şəkil",blank=True, default=None, upload_to=save_directory_path)
    sold = models.BooleanField("Satılıb", default=False)
    inventory = models.BooleanField("Inventar", default=False)
    
    def __str__(self):
        return " {} ".format(self.code)

    def get_absolute_url(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('network_hw_edit', args=[str(self.pk)])

    def get_detail(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('network_hw_detail', args=[str(self.pk)])

    def get_delete(self):
        """
        Handy way of getting the url of the object to its delete view page
        """
        return reverse('network_hw_delete', args=[str(self.pk)])

    def get_class(self):
        """
        Handy way of getting the class of the object for the html templates
        """
        class_name = "Şəbəkə avadanlığı"
        return class_name
    
    def get_amount_in_stock(self):
        amount = 0
        qs = NetworkHardware.objects.filter(sold='False')
        for item in qs:
            amount = amount + item.selling_price*item.quantity
        return amount

    def get_number_of_items_in_stock(self):
        number = 0
        qs = NetworkHardware.objects.filter(sold='False')
        for item in qs:
            number = number + item.quantity
        return number

    class Meta:
        verbose_name_plural = "Şəbəkə avadanlıqları"
