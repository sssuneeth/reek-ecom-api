from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify

from accounts.models import User


# Category model
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)
    rocking_now = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-id']

# Item model


class Item(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(null=True, blank=True)
    rating = models.FloatField(default=0, blank=True)
    real_price = models.IntegerField()
    offer_price = models.IntegerField()
    discount = models.IntegerField(null=True, blank=True)
    description = models.TextField()

    # override save method
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)[:30]
        self.discount = 100 * \
            (self.real_price - self.offer_price) / self.real_price
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

# Image model for Item


class ItemImage(models.Model):
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name='item_images')
    image = models.ImageField(upload_to='item_images')

    def __str__(self):
        return f'{self.image}'

# Sizes for Item


class ItemSize(models.Model):
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name='item_sizes')
    size_s = models.BooleanField(default=False, blank=True)
    size_m = models.BooleanField(default=False, blank=True)
    size_l = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'{self.item}'


# Basket model
class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.email} - {self.complete}'

    @property
    def get_total(self):
        basketitems = BasketItem.objects.filter(basket=self)
        total = sum([item.get_item_total for item in basketitems])

        return total

    @property
    def get_discount(self):
        basketitems = BasketItem.objects.filter(basket=self)
        total_offer_price = sum(
            [item.get_total_offer_price for item in basketitems])
        total_real_price = sum(
            [item.get_total_real_price for item in basketitems])
        try:
            discount = 100 * (total_real_price - total_offer_price) / total_real_price
        except ZeroDivisionError:
            discount = 0

        return discount

    @property
    def get_discounted_price(self):
        basketitems = BasketItem.objects.filter(basket=self)
        total_offer_price = sum([item.get_total_offer_price for item in basketitems])
        total_real_price = sum([item.get_total_real_price for item in basketitems])
        discounted_price = total_real_price - total_offer_price

        return discounted_price

    @property
    def get_total_price(self):
        basketitems = BasketItem.objects.filter(basket=self)
        total = sum([item.get_total_real_price for item in basketitems])

        return total


#Basket signal for creating basket in user creation time
def create_basket_address(sender, instance, created, **kwargs):
    if created:
        Basket.objects.create(user = instance, complete = False)
        ShippingAddress.objects.create(user = instance)

post_save.connect(create_basket_address, sender = User)

# basket items
class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    size = models.CharField(max_length=5, default='M', blank=True)
    quantity = models.IntegerField(default=1)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.item.title}'

    @property
    def get_item_total(self):
        total = self.item.offer_price * self.quantity
        return total

    @property
    def get_total_real_price(self):
        total = self.item.real_price * self.quantity
        return total

    @property
    def get_total_offer_price(self):
        total = self.item.offer_price * self.quantity
        return total

# saved items


class SavedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=10, default='M')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.item.title

    @property
    def get_total(self):
        total = self.item.offer_price * self.quantity
        return total


    @property
    def get_real_total(self):
        total = self.item.real_price * self.quantity
        return total


# shiping address
class ShippingAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    zipcode = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.user.email} - {self.address}'

#payment model
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    basket = models.OneToOneField(Basket, on_delete=models.CASCADE)
    address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.email} - {self.is_paid}'