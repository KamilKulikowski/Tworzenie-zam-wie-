from django.db import models
import json, random, datetime


class Item(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    code = models.CharField(max_length=50, default=str(random.randint(0, 99)))
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'({self.pk}) {self.name}'


class Order(models.Model):
    customer = models.IntegerField(default=0)
    taken_by = models.IntegerField(default=0)
    date = models.DateField(default=datetime.date.today)
    code = models.CharField(max_length=50, default=str(random.randint(0, 99)))
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    products = models.CharField(max_length=200, default="")

    def __str__(self):
        return f'({self.pk})'

    def set_list(self, x):
        self.products = json.dumps(x)

    def get_list(self):
        return json.loads(self.products)
