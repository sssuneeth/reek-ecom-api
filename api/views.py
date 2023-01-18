from rest_framework.response import Response
from rest_framework.views import APIView

#import Item serilizer
from .serializers import ItemSerializer, CatsSerializer, UserSerializer, BasketItemSerializer, BasketSerializer, SavedItemSerliazer, ShippingAddressSerilaizer

#import Items model
from reek.models import Item, Category, BasketItem, Basket, SavedItem, ShippingAddress, Payment

from accounts.models import User


#Get all routes
class getRoutes(APIView):
    def get(self, request):
        routes = [
            '/api/',
            '/api/items/',
            '/api/gog-items/',
            '/api/categories/',
            '/api/user/',
            '/api/token/',
            '/api/token/refresh/',
            'and more routes...'
        ]
        return Response(routes)

#Get all items
class getItems(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)

        return Response(serializer.data)

#Get GOG items
class getGOGItems(APIView):
    def get(self, request):
        items = Item.objects.all().order_by('-discount')[:4]
        serializer = ItemSerializer(items, many=True)

        return Response(serializer.data)

#GEt all cats
class getCategories(APIView):
    def get(self, request):
        cats = Category.objects.all()
        serializer = CatsSerializer(cats, many=True)

        return Response(serializer.data)

# get cat items
class getCatsItems(APIView):
    def get(self, request, slug):
        items = Item.objects.filter(category__slug = slug)
        serializer = ItemSerializer(items, many = True)

        return Response(serializer.data)

#Register
class RegisterView(APIView):
    def post(self, request):
        serilizer = UserSerializer(data=request.data, many=False)
        serilizer.is_valid(raise_exception=True)
        serilizer.save()

        return Response(serilizer.data)


#getBasket
class getBasket(APIView):
    def get(self, request):
        user = request.user
        basket = Basket.objects.filter(user = user, complete = False).first()
        serializer = BasketSerializer(basket, many=False)

        return Response(serializer.data)

#getBasketItems
class getBasketItems(APIView):
    def get(self, request):
        user = request.user
        # basket = Basket.objects.filter(user = user, complete = False).first()
        basketItem = BasketItem.objects.filter(basket__user = request.user, basket__complete = False)
        serializer = BasketItemSerializer(basketItem, many=True)

        return Response(serializer.data)

#addBasket
class addBasket(APIView):
    def post(self, request):
        user = request.user
        data = request.data
        
        item = Item.objects.filter(id = data['item_id']).first()
        basket = Basket.objects.filter(user = user, complete = False).first()
        basket_item, created = BasketItem.objects.get_or_create(basket = basket, item = item)
        basket_item.size = str(data['size']).upper()
        basket_item.quantity = data['quantity']
        basket_item.save()
        
        return Response({
            'status': 200,
            'statusText': 'OK',
            'text': 'Item added to basket'
        })

#removeBasket
class removeBasket(APIView):
    def post(self, request):
        data = request.data
        
        basket_item = BasketItem.objects.filter(id = data['id']).first()
        basket_item.delete()

        return Response({
            'status': 200,
            'statusText': 'OK',
            'text': 'Item removed from basket'
        })

#getSavedItems
class getSavedItems(APIView):
    def get(self, request):
        user = request.user
        saved_item = SavedItem.objects.filter(user = user)
        serializer = SavedItemSerliazer(saved_item, many = True)

        return Response(serializer.data)

#addSaved
class addSaved(APIView):
    def post(self, request):
        user = request.user
        data = request.data

        item = Item.objects.filter(id = data['item_id']).first()
        saved_item, created = SavedItem.objects.get_or_create(user = user, item = item)
        saved_item.size = str(data['size']).upper()
        saved_item.quantity = data['quantity']
        saved_item.save()

        return Response({
            'status': 200,
            'statusText': 'OK',
            'text': 'Item added to saved'
        })

#removeSaved
class removeSaved(APIView):
    def post(self, request):
        data = request.data
        print(data)

        saved_item = SavedItem.objects.filter(id = data['id']).first()
        saved_item.delete()

        return Response({
            'status': 200,
            'statusText': 'OK',
            'text': 'Item added to saved'
        })

#addToCart
class addToCart(APIView):
    def post(self, request):
        data = request.data
        user = request.user

        saved_item = SavedItem.objects.filter(id = data['id']).first()
        saved_item.delete()
        item = Item.objects.filter(id = data['item_id']).first()
        basket = Basket.objects.filter(user = user, complete = False).first()
        basket_item, created = BasketItem.objects.get_or_create(basket = basket, item = item)
        basket_item.size = data['size']
        basket_item.quantity = data['quantity']
        basket_item.save()

        return Response({
            'status': 200,
            'statusText': 'OK',
            'text': 'Item added to cart from saved'
        })

#saveForLater
class saveForLater(APIView):
    def post(self, request):
        user = request.user
        data = request.data

        basket_item = BasketItem.objects.filter(id = data['id']).first()
        basket_item.delete()
        item = Item.objects.filter(id = data['item_id']).first()
        saved_item, created = SavedItem.objects.get_or_create(user = user, item = item)
        saved_item.size = data['size']
        saved_item.quantity = data['quantity']
        saved_item.save()

        return Response({
            'status': 200,
            'statusText': 'OK',
            'text': 'Item saved for later from basket'
        })


#Get user info
class getUser(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user, many = False)

        return Response(serializer.data)

#Get orders
class getOrders(APIView):
    def get(self, request):
        basket_items = BasketItem.objects.filter(basket__complete = True, basket__user = request.user)
        serializer = BasketItemSerializer(basket_items, many = True)

        return Response(serializer.data)

# edit profile
class editProfile(APIView):
    def post(self, request):
        user = request.user
        data = request.data

        curUser = User.objects.filter(id = user.id).first()
        curUser.name = data['newName']
        curUser.email = data['newEmail']
        curUser.phone = data['newPhone']
        curUser.save()

        serializer = UserSerializer(curUser, many=False)
        return Response(serializer.data)

# get shipping address for the user
class getShippingAddress(APIView):
    def get(self, request):
        address_obj = ShippingAddress.objects.filter(user = request.user).first()
        serializer = ShippingAddressSerilaizer(address_obj, many = False)
        
        return Response(serializer.data)

#payment view
class PaymentView(APIView):
    def post(self, request):
        user = request.user
        data = request.data
        print(data, user)

        basket = Basket.objects.filter(user = user, complete = False).first()
        basket.complete = True
        basket.save()
        Basket.objects.create(user = user, complete = False)

        shipping_address = ShippingAddress.objects.filter(user = user).first()
        shipping_address.address = data['address1']
        shipping_address.address2 = data['address2']
        shipping_address.city = data['city']
        shipping_address.landmark = data['landmark']
        shipping_address.zipcode = int(data['zipcode'])

        shipping_address.save()

        payment_obj = Payment.objects.create(
            user = user,
            basket = basket,
            address = shipping_address,
            is_paid = False
        )

        return Response('Order placed successfully')