from django.urls import path
from .import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes.as_view()),
    path('items/', views.getItems.as_view()),
    path('gog-items/', views.getGOGItems.as_view()),
    path('categories/', views.getCategories.as_view()),
    path('categories/<slug:slug>/', views.getCatsItems.as_view()),
    path('basketitems/', views.getBasketItems.as_view()),
    path('basket/', views.getBasket.as_view()),
    path('basket/add/', views.addBasket.as_view()),
    path('basket/remove/', views.removeBasket.as_view()),
    path('saved/', views.getSavedItems.as_view()),
    path('saved/add/', views.addSaved.as_view()),
    path('saved/remove/', views.removeSaved.as_view()),
    path('addtocart/', views.addToCart.as_view()),
    path('saveforlater/', views.saveForLater.as_view()),
    path('orders/', views.getOrders.as_view()),
    path('getshippingaddress/', views.getShippingAddress.as_view()),

    #simple jwt paths
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #auth paths
    path('register/', views.RegisterView.as_view()),

    #user paths
    path('user/', views.getUser.as_view()),
    path('editprofile/', views.editProfile.as_view()),
    path('guestuser/', views.GuestUser.as_view()),

    #payment
    path('checkout/', views.PaymentView.as_view()),
]
