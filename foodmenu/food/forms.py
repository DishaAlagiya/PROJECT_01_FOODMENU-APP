from django import forms
from .models import item

class itemform(forms.ModelForm):
    class Meta:
        model=item
        fields=['item_name','item_price','item_desc','item_image']
        widgets = {
            'item_name': forms.TextInput(attrs={'placeholder':'eg. vadapav','required':True}),
            'item_price': forms.NumberInput(attrs={'placeholder':'9.50','required':True}),
            'item_desc': forms.TextInput(attrs={'placeholder':'eg. butter vadapav','required':True}),
            'item_image': forms.URLInput(attrs={'placeholder':'eg.https://www.google.com/','required':False})
        }

    def clean_item_price(self):
        price = self.cleaned_data['item_price']
        if price < 0:
            raise forms.ValidationError("Price cannot be negative ")
        return price
    
    def clean(self):
        cleaned = super().clean()
        name = cleaned.get('item_name')
        desc = cleaned.get("item_desc")
        if name and desc and name.lower() in desc.lower():
            self.add_error('item_desc', 'Description should not contain the item name')
        return cleaned