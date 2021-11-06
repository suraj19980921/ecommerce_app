
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic.base import  View
from django.views.generic.edit import DeleteView, ModelFormMixin, UpdateView
from main import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from main import forms
from django.http import JsonResponse
from django.db.models import Sum
import datetime
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages 





# Create your views here.

class Home(ListView):
    model = models.Item
    template_name = 'main/home.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = models.Category.objects.all()
        items_list = []

        for category in categories:
            filterd_items = models.Item.objects.filter(category = category.id)[:5]
            items_list.append(filterd_items)

        context['items'] = items_list
        print(items_list)
        return context


class ShowItem(DetailView):
    model = models.Item
    template_name = 'main/item_page.html'
    context_object_name = 'item_details'
    

    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        data = self.get_context_data(object=self.object)
        if request.is_ajax():
            context={
                        "item_id":data['item_details'].id,
                        "item_name":data['item_details'].item_name,
                        "item_image":str(data['item_details'].item_image),
                        "item_price":data['item_details'].item_price,
                        "item_category":str(data['item_details'].category.id),
                        "item_description":data['item_details'].item_description,
            }
            return JsonResponse(context)
        return self.render_to_response(data)
        


class ItemsList(LoginRequiredMixin,ListView):
    template_name = 'main/items_list.html'
    context_object_name = 'items_list'
    paginate_by = 10
    login_url = 'login'
    def get_queryset(self):
        return models.Item.objects.filter(category=self.kwargs['pk'])

class AddItem(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    template_name = 'main/shop_items.html'
    form_class = forms.ItemForm
    success_url = '/shop_items/'
    success_message = 'New Item Added Successfully'
    login_url = 'login'
    
    def form_valid(self, form):
        for value in self.request.user.shop_set.all():
            shop_id = value.id
        form.instance.shop = models.Shop.objects.get(id = shop_id)
        return super().form_valid(form)

   
class UpdateItem(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model = models.Item
    form_class = forms.ItemForm
    template_name = 'main/shop_items.html'
    success_url = '/shop_items/'
    success_message = 'Item Updated Successfully'
    login_url = 'login'

class DeleteItem(SuccessMessageMixin,LoginRequiredMixin,DeleteView):
    model= models.Item
    template_name = 'main/shop_items.html'
    success_url = '/shop_items/'
    success_message = 'Item Deleted Successfully'
    login_url = 'login' 

    def delete(self, request,*args, **kwargs):
        messages.add_message(request,messages.SUCCESS, 'Successfully Deleted')
        return super().delete(request, *args, **kwargs)


class CreateShop(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    model = models.Shop
    form_class = forms.CreateShopForm
    template_name = 'main/shop.html'
    success_url = '/shop_items'
    success_message = 'Shop created Successfully'
    login_url = 'login'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ShopItems(LoginRequiredMixin,ListView):
    template_name = 'main/shop_items.html'
    paginate_by = 10
    context_object_name = "shop_items"
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_form'] = forms.UpdateItemForm
        context['item_form'] = forms.ItemForm
        return context


    def get_queryset(self):
            for value in self.request.user.shop_set.all():
                shop_id = value.id
            shop_items = models.Item.objects.filter(shop= shop_id)
            return shop_items


class DeleteShop(LoginRequiredMixin,DeleteView):
    model = models.Shop
    success_url = "/"
    login_url = 'login'

    def delete(self, request,*args, **kwargs):
        messages.add_message(request,messages.SUCCESS, 'Shop Deleted  Successfully')
        return super().delete(request, *args, **kwargs)


class AddtoCart(LoginRequiredMixin,View):
    login_url = 'login'
   
    def get(self, request, **arg):
        item = models.Item.objects.get(pk = arg['pk'] )
        models.Cart.objects.create(user= self.request.user, item_id = item, quantity=1, total_amount=item.item_price)
        messages.add_message(request, messages.SUCCESS, 'succesfully added to cart')
        return redirect('cart')

class ShowCart(LoginRequiredMixin,View):
    login_url = 'login'
    
    def get(self, request):
        cart_items = models.Cart.objects.filter(user=request.user).order_by("-id")
        total_price = models.Cart.objects.filter(user=request.user).aggregate(total= Sum('total_amount'))
        quantity = models.Cart.objects.filter(user=request.user).aggregate(total= Sum('quantity'))
        context = {"cart_items":cart_items,
                   "total_price":total_price,
                   "quantity":quantity}
        
        
        
        return render(request, 'main/cart.html', context)


class UpdateCart(LoginRequiredMixin,View):
    login_url = 'login'
    
    def post(self, request, pk):
    
        cart_id = pk
        product_quantity = request.POST.get('data')
        cart = models.Cart.objects.get(id=cart_id)
        total_amount = float(cart.item_id.item_price)*float(product_quantity) 
        models.Cart.objects.filter(id = cart_id).update(quantity = product_quantity, total_amount = total_amount )
        price = models.Cart.objects.filter(user=request.user).aggregate(total= Sum('total_amount'))
        quantity = models.Cart.objects.filter(user=request.user).aggregate(total= Sum('quantity'))
        context = {
                'quantity' : str(quantity['total']),
                'total_price' : str(price['total'])
        }
        return JsonResponse(context)


class DeleteCart(LoginRequiredMixin,DeleteView):
    model = models.Cart
    success_url = '/cart/'
    login_url = 'login'


class CreateOrders(LoginRequiredMixin,View):
    login_url = 'login'
    
    def post(self,request):
      
      user = request.user
      carts = models.Cart.objects.all()
      shipping_address = request.POST.get('shipping_address')
      pincode =request.POST.get('pincode')
      mobile_no = request.POST.get('mobile_no')

      for cart in carts:
        order =  models.Order.objects.create(user_id = user, item_id = cart.item_id,
                                             category = cart.item_id.category,
                                              quantity=cart.quantity,
                                              shop_id = models.Shop.objects.get(id=cart.item_id.shop.id),
                                              shipping_address = shipping_address,
                                              pincode = pincode, mobile_no= mobile_no,
                                              purchase_date = datetime.datetime.now(),
                                              total_price=cart.total_amount)
    
      if(order):
          models.Cart.objects.all().delete()
          messages.add_message(request,messages.SUCCESS,'Odered Successfully')
      
      return HttpResponseRedirect('/orders')
        

class ShowOrders(LoginRequiredMixin,ListView):
    model = models.Order
    template_name = 'main/orders.html'
    context_object_name = 'orders'
    login_url = 'login'
    paginate_by = 10
    

    def get_queryset(self):
        return models.Order.objects.filter(user_id = self.request.user).order_by('-purchase_date')
