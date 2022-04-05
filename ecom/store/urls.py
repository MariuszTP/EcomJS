from django.urls import path
from . import views

#from .views import UpdateItem

urlpatterns = [


    path('ms', views.mainstore, name="mainstore"),
    path('store/', views.store, name="store"),
    path('storejs', views.storejs, name="storejs"),
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('updateitem/', views.updateItem, name="updateitem"),
    path('store1', views.store1, name="store1")
    

]