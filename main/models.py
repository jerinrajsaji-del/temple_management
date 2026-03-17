from django.db import models
from django.contrib.auth.models import User

class Temple(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='temples/', blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    admin_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_temples')

    def __str__(self):
        return self.name


class Pooja(models.Model):
    temple = models.ForeignKey(Temple, on_delete=models.CASCADE)
    pooja_name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='poojas/', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pooja_name} - {self.temple.name}"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    devotee_name = models.CharField(max_length=200)
    temple = models.ForeignKey(Temple, on_delete=models.CASCADE)
    pooja = models.ForeignKey(Pooja, on_delete=models.CASCADE)
    date = models.DateField()
    nakshatra = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.devotee_name} - {self.pooja.pooja_name}"