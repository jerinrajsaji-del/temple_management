from django.db import models

class Temple(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Pooja(models.Model):
    temple = models.ForeignKey(Temple,on_delete=models.CASCADE)
    pooja_name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.pooja_name


class Booking(models.Model):
    user_name = models.CharField(max_length=200)
    temple = models.ForeignKey(Temple, on_delete=models.CASCADE)
    pooja = models.ForeignKey(Pooja, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.user_name