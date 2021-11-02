from django import http
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.aggregates import Max, Min, Sum
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView
from main import models
from django.views.generic import ListView
from admin import forms
from django.contrib import messages
from datetime import date
from django.core.paginator import Paginator

# Create your views here.

class Dashboard(LoginRequiredMixin, ListView):
    model = models.Item
    template_name = 'admin/dashboard.html'
    context_object_name = 'items'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(Dashboard,self).get_context_data(**kwargs)
        context['users'] = models.User.objects.all()
        context['shops'] = models.Shop.objects.all()
        context['category'] = models.Category.objects.all()
        context['carts'] = models.Cart.objects.all()
        context['orders'] = models.Order.objects.all()
        return context


class UsersList(ListView, LoginRequiredMixin):
    model = models.User
    template_name = 'admin/users_list.html'
    paginated_by = 10
    context_object_name = "users"
    login_url = 'login'

class DeleteUser(DeleteView, LoginRequiredMixin):
    model = models.User
    template = "/admin/users_list.html"
    success_url = "/admin/users_list/"
    login_url = 'login'

    def delete(self, request, *args, **kwargs):
        # the Post object
        self.object = self.get_object()
        delete_user = self.object.delete()
        if(delete_user):
            messages.add_message(request,messages.SUCCESS,'Deleted Successfully')
        else:
            messages.add_message(request,messages.ERROR,'Unable to delete')
        success_url = self.get_success_url()
        return http.HttpResponseRedirect(success_url)
       

class ShopsList(ListView, LoginRequiredMixin):
    model = models.Shop
    template_name = 'admin/shops_list.html'
    paginate_by = 10
    context_object_name = "shops"
    login_url = 'login'

class DeleteShop(DeleteView, LoginRequiredMixin):
    model = models.Shop
    success_url = '/admin/shops_list/'
    login_url = 'login'
    
    def delete(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, 'Deleted Successfully')
        return super().delete(request, *args, **kwargs)

class ItemsList(ListView, LoginRequiredMixin):
    model = models.Item
    template_name = 'admin/items_list.html'
    paginate_by = 10
    context_object_name = "items"
    login_url = 'login'

class DeleteItem(DeleteView, LoginRequiredMixin):
    model = models.Item
    success_url = '/admin/items_list/'
    login_url = 'login'

    def delete(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, 'Deleted Successfully')
        return super().delete(request, *args, **kwargs)


class CategoriesList(ListView, LoginRequiredMixin):
    model = models.Category
    template_name = 'admin/category_list.html'
    paginate_by = 10
    context_object_name = "categories"
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.AddCategoryForm
        return context

class AddCategory(CreateView, LoginRequiredMixin):
    model = models.Category
    form_class = forms.AddCategoryForm
    template_name = 'admin/category_list.html'
    success_url = '/admin/category_list'
    login_url = 'login'

class DeleteCategory(DeleteView, LoginRequiredMixin):
    model = models.Category
    success_url = '/admin/category_list/'
    login_url = 'login'

    def delete(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, 'Deleted Successfully')
        return super().delete(request, *args, **kwargs)

class CartsList(ListView, LoginRequiredMixin):
    model = models.Cart
    template_name = 'admin/carts_list.html'
    context_object_name = "carts"
    paginate_by = 10
    login_url = 'login'

class DeleteCart(DeleteView, LoginRequiredMixin):
    model = models.Cart
    success_url = '/admin/carts_list/'
    login_url = 'login'

    def delete(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, 'Deleted Successfully')
        return super().delete(request, *args, **kwargs)
    

class OrdersList(ListView, LoginRequiredMixin):
    model = models.Order
    template_name = 'admin/orders_list.html'
    context_object_name = "orders"
    paginate_by = 10
    login_url = 'login'

class DeleteOrder(DeleteView, LoginRequiredMixin):
    model = models.Order
    success_url = '/admin/orders_list/'
    login_url = 'login'

    def delete(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, 'Deleted Successfully')
        return super().delete(request, *args, **kwargs)

class Sales(ListView, LoginRequiredMixin):
    model = models.Order
    template_name = 'admin/sales_report_list.html'
    login_url = 'login'
    
    
   
   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = models.Category.objects.all()
        sales_report_list = []
        report = {}
        today = date.today()
        
        for category in categories:
            report['category'] = category.category_name
            report = models.Order.objects.filter(category = category.id, purchase_date__month= today.month,
                                                 purchase_date__year= today.year ).aggregate(total_sales = Sum('total_price'),
                                                                                   total_quantity_sold = Sum('quantity'),
                                                                                   max_purchased = Max('quantity'),
                                                                                   min_purchased = Min('quantity'))
   
            report['max_purchased_item'] = models.Order.objects.filter(quantity = report['max_purchased'] , category = category)
            report['min_purchased_item'] = models.Order.objects.filter(quantity = report['min_purchased'], category = category)                      
            
            sales_report_list.append(report)
        
        paginator = Paginator(sales_report_list, 5)

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['is_paginated'] = True
        
        '''context['sales_reports'] = sales_report_list'''
        return context