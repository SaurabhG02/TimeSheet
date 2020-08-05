from django import forms
from django.core.exceptions import ValidationError
from .models import TimeSheet
from bootstrap_datepicker_plus import DatePickerInput

class DateInput(forms.DateInput):
    input_type = 'date'


class TimeSheetForm(forms.ModelForm):
    my_default_errors = {
    'required': 'Attach client approved time sheet',}


    attachment= forms.FileField(error_messages=my_default_errors)
    # attachment = forms.FileField(error_messages={'required': 'Please let us know what to call you!'})
    

    class Meta:
        model = TimeSheet
        fields = ['date','time','attachment']
        widgets = {'date': DateInput()}

    

        

    # my_default_errors = {'required': 'This field is ','invalid': 'Enter a valid '}

    # attachment = forms.FileField(error_messages={'required': 'Please enter your name'})
    
    


#     # def clean_time(self):
#     #     data = self.cleaned_data['time']
#     #     if (data>=0 and data<=24):
#     #         return data
#     #     else:
#     #         return ValidationError("Time should be in between 0 to 24")