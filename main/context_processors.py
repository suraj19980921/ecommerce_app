from main import models


def galobal_data(request):
   categories = models.Category.objects.all()
   cart_count = 0
   if request.user.is_authenticated:
         cart_count = models.Cart.objects.filter(user = request.user).count()
   
   context = {"categories":categories,
              "cart_count":cart_count}
   return context