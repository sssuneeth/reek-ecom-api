from rest_framework import serializers

from reek.models import Item, ItemImage, ItemSize, Category, BasketItem, Basket, SavedItem, ShippingAddress
from accounts.models import User



#ItemImage serializer
class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = '__all__'

#ItemSize serializer
class ItemSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSize
        fields = '__all__'

#Category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

#ItemSerializer
class ItemSerializer(serializers.ModelSerializer):

    #images serializing
    item_images = ItemImageSerializer(many=True)
    #sizes serializing
    item_sizes = ItemSizeSerializer(many=True)
    #category serializing
    category = CategorySerializer(many=False)

    #item serializing
    class Meta:
        model = Item
        fields = '__all__'

#Cats serializer
class CatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

#User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name','phone', 'pic', 'password']
        extra_kwargs = {
            'password': { 'write_only' : True}
        }

    #Override create method
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

#Basket serializer
class BasketSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField(source = 'get_total', read_only = True)
    total_price = serializers.IntegerField(source = 'get_total_price', read_only = True)
    discount = serializers.IntegerField(source = 'get_discount', read_only = True)
    discount_price = serializers.IntegerField(source = 'get_discounted_price', read_only = True)
    
    class Meta:
        model = Basket
        fields = ['id', 'user', 'complete', 'total', 'total_price', 'discount', 'discount_price']

#basket item serilaizer
class BasketItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=False)
    total = serializers.IntegerField(source = 'get_item_total', read_only = True)
    class Meta:
        model = BasketItem
        fields = ['id', 'basket', 'item', 'size', 'quantity', 'total']

#Saved items serializer
class SavedItemSerliazer(serializers.ModelSerializer):
    total = serializers.IntegerField(source = 'get_total', read_only = True)
    real_total = serializers.IntegerField(source = 'get_real_total', read_only = True)

    #Item serialiing
    item = ItemSerializer(many=False)
    class Meta:
        model = SavedItem
        fields = ['id', 'user', 'item', 'size', 'quantity', 'total', 'real_total']


# Shipping address serializer
class ShippingAddressSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ['address', 'address2', 'city', 'landmark', 'zipcode']