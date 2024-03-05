from django.db import models

# the data you want to present, usually data from a database.
# visible to developer only
# data is created in objects, called Models, and is actually tables in a database.


class Brand(models.Model):
    brand = models.CharField(max_length=200, default="0", null=False, unique=True)
    year = models.IntegerField(default="0", null=True)
    owner_name = models.CharField(max_length=200, default="0", null=True)
    employees = models.IntegerField(default="0", null=True)
    country = models.CharField(max_length=200, default="0", null=True)

    def __str__(self):
        return self.brand


class Cars(models.Model):
    name = models.CharField(max_length=200, default='')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    description = models.CharField(max_length=500, default='')
    review = models.CharField(max_length=500, default='')
    price = models.IntegerField(default="0")

    def __str__(self):
        return str(self.brand) + ' ' + self.name


class Customers(models.Model):
    name_of_customer = models.CharField(max_length=200)
    year_of_birth = models.IntegerField(default="0")
    address = models.CharField(max_length=500, default="0")
    gender = models.CharField(max_length=100, default="0")
    phone = models.IntegerField(default="0")

    def __str__(self):
        return str(self.name_of_customer)


class CarsSold(models.Model):
    customers_id = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name="customers_id")
    cars_id = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name="cars_id")
    date = models.DateField(default="2000-12-20")
    amount = models.IntegerField(default="0")

    def __str__(self):
        return str(self.customers_id) + " " + str(self.cars_id)