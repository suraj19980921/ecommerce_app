from django import forms
from main import models


class CreateShopForm(forms.ModelForm):
    class Meta:
        model = models.Shop
        fields = ['shop_name']
        widgets = {'shop_name': forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter Your Shop Name"})}

class ItemForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = '__all__'
        widgets = {
                    'item_name' : forms.TextInput(attrs={"class":"form-control", "id":"item_name"}), 
                    'category': forms.Select(attrs={"id":"item_category"})
                    
        }

        exclude = ["shop"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item_image'].widget = forms.FileInput(attrs={'class': 'form-control',  "id":"item_image"})
        self.fields['item_price'].widget = forms.NumberInput(attrs={'class': 'form-control',  "id":"item_price"})
        self.fields['item_description'].widget = forms.Textarea(attrs={'class': 'form-control',  "id":"item_description"})
       

class UpdateItemForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = '__all__'
        widgets = {
                    'item_name' : forms.TextInput(attrs={"class":"form-control", "id":"update_item_name"}), 
                    'category': forms.Select(attrs={"id":"update_item_category"})
                    
        }

        exclude = ["shop"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item_image'].widget = forms.FileInput(attrs={'class': 'form-control',  "id":"update_item_image"})
        self.fields['item_price'].widget = forms.NumberInput(attrs={'class': 'form-control',  "id":"update_item_price"})
        self.fields['item_description'].widget = forms.Textarea(attrs={'class': 'form-control',  "id":"update_item_description"})



            



           