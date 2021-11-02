from django.urls import path
from admin import views

urlpatterns=[
            
            path('dashboard/', views.Dashboard.as_view(), name="dashboard"),
            path('delete_user/<int:pk>', views.DeleteUser.as_view(), name="delete_user"),
            path('users_list/', views.UsersList.as_view(), name="users_list"),
            path('shops_list/', views.ShopsList.as_view(), name="shops_list"),
            path('delete_shop/<int:pk>', views.DeleteShop.as_view(), name="delete_shop"),
            path('items_list/', views.ItemsList.as_view(), name="items_list"),
            path('delete_item/<int:pk>', views.DeleteItem.as_view(), name="delete_item"),
            path('category_list/', views.CategoriesList.as_view(), name="category_list"),
            path('add_category/', views.AddCategory.as_view(), name="add_category"),
            path('delete_category/<int:pk>', views.DeleteCategory.as_view(), name="delete_category"),
            path('carts_list/', views.CartsList.as_view(), name="carts_list"),
            path('delete_cart/<int:pk>', views.DeleteCart.as_view(), name="delete_cart"),
            path('orders_list/', views.OrdersList.as_view(), name="orders_list"),
            path('delete_order/<int:pk>', views.DeleteOrder.as_view(), name="delete_order"),
            path('sales/', views.Sales.as_view(), name="sales_report_list"),
    ]
