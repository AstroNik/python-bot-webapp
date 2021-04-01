from django.db import models

# Create your models here.


class User(models.Model):
    uid = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Billing(models.Model):
    uid = models.ForeignKey(User.uid, on_delete=models.SET_NULL=True)
    card_number = models.CharField(max_length=16)
    card_holder = models.CharField(max_length=25)
    expiry = models.CharField(max_length=4)
    cvv = models.CharField(max_length=4)
    billing_cycle = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.billing_cycle


class Purchases(models.Model):
    uid = models.ForeignKey(User.uid, on_delete=models.SET_NULL=True)
    item_purchased = models.CharField(max_length=100)
    price = models.DecimalField()

    def __str__(self):
        return self.item_purchased


class Bots(models.Model):
    uid = models.ForeignKey(User.uid, on_delete=models.SET_NULL=True)
    active_bots = models.IntegerField()

    def __str__(self):
        return self.active_bots


class BestBuy(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=25)
    cvv = models.CharField(max_length=4)

    def __str__(self):
        return self.email


class Amazon(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.email


class Accounts(models.Model):
    uid = models.ForeignKey(User.uid, on_delete=models.SET_NULL=True)
    bestbuy = models.ForeignKey(BestBuy, on_delete=models.SET_NULL, null=True)
    amazon = models.ForeignKey(Amazon, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.uid

