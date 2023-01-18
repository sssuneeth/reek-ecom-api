from django.contrib import admin
from .models import Item, ItemImage, ItemSize, Category, Basket, BasketItem, SavedItem, ShippingAddress, Payment

#### Inlines
#Item image inline
class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 0

#Item size inline
class ItemSizeInline(admin.TabularInline):
    model = ItemSize
    extra = 0

#### Admin Models
#Item admin
class AdminItem(admin.ModelAdmin):
    inlines = [ItemImageInline, ItemSizeInline]
    list_display = ['id', 'title', 'rating', 'real_price', 'offer_price', 'discount']
    list_filter = ['category', 'rating']
    search_fields = ['title']
    # exclude = ('slug', 'rating', 'discount', )
    readonly_fields = ['slug', 'discount']

admin.site.register(Item, AdminItem)

#ItemImage admin
class AdminItemImage(admin.ModelAdmin):
    list_display = ['id', 'item', 'image']
    list_filter = ['item']
    search_fields = ['item']

admin.site.register(ItemImage, AdminItemImage)

#ItemSize admin
class AdminItemSize(admin.ModelAdmin):
    list_display = ['id', 'item', 'size_s', 'size_m', 'size_l']
    list_filter = ['size_s', 'size_m', 'size_l']
    search_fields = ['item']

admin.site.register(ItemSize, AdminItemSize)

#Category admin
class AdminCategory(admin.ModelAdmin):
    list_display = [ 'title', 'slug']
admin.site.register(Category, AdminCategory)

#basket
class AdminBasket(admin.ModelAdmin):
    list_display = ['user', 'complete']
    list_filter = ['complete']
admin.site.register(Basket, AdminBasket)

#Basket item
class AdminBasketItem(admin.ModelAdmin):
    list_display = ['basket', 'item', 'size', 'quantity']
    list_filter = ['size']
admin.site.register(BasketItem, AdminBasketItem)

#Saved items
class AdminSavedItem(admin.ModelAdmin):
    list_display = ['user', 'item', 'size', 'quantity']
    list_filter = ['size']
admin.site.register(SavedItem, AdminSavedItem)

#Shipping address
admin.site.register(ShippingAddress)

#payment
admin.site.register(Payment)