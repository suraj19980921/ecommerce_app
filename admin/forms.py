from django import forms
from main import models


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'

