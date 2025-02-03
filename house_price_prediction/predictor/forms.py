from django import forms

class HousePriceForm(forms.Form):
    bedrooms = forms.FloatField(label="Bedrooms")
    bathrooms = forms.FloatField(label="Bathrooms")
    sqft_living = forms.FloatField(label="Sqft Living Area")
    sqft_lot = forms.FloatField(label="Sqft Lot Size")
    floors = forms.FloatField(label="Floors")
