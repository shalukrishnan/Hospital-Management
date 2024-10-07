from django import forms
from .models import Booking
class DateInput(forms.DateInput):
    input_type ='date' 

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields ='__all__'




        widgets = {
            'booking_date' : DateInput(),
        }

        labels = {
            'p_name' :"Patient Name",
            'p_phone' :"Contact Number",
            'p_email'  :"Email",
            'doc_name'  : "Doctor Name",
            'booking_date':"Booking Date",
            'booked_slot' :'Booking Time',
            'booked_on':'Booked on',
        }




        
        