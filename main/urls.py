from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
        path('', views.Home.as_view(), name='home'),
        path('item/<int:pk>', views.ShowItem.as_view(), name="show_item"),
        path('items/<int:pk>', views.ItemsList.as_view(), name="items"),
        path('add_item/', views.AddItem.as_view(), name="add_items"),
        path('update_item/<int:pk>',views.UpdateItem.as_view(), name="update_item"),
        path('delete_item/<int:pk>',views.DeleteItem.as_view(), name="delete_item"),
        path('create_shop/',views.CreateShop.as_view(), name="create_shop"),
        path('shop_items/',views.ShopItems.as_view(), name="shop_items"),
        path('delete_shop/<int:pk>',views.DeleteShop.as_view(), name="delete_shop"),
        path('add_to_cart/<int:pk>',views.AddtoCart.as_view(), name="addtocart"), 
        path('update_cart/<int:pk>',views.UpdateCart.as_view(), name="update_cart"),
        path('cart/',views.ShowCart.as_view(), name="cart"),
        path('delete_cart/<int:pk>',views.DeleteCart.as_view(), name="delete_cart"),
        path('create_orders', views.CreateOrders.as_view(), name="create_order"),
        path('orders/', views.ShowOrders.as_view(), name="orders"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)