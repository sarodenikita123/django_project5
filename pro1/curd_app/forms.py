from django import forms
from .models import Hotel


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.NumberInput(),
            "booking_date_time": forms.DateInput(),
            "aadhar_no": forms.NumberInput(),
            "type": forms.RadioSelect()
        }