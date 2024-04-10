from django.forms import ModelForm, ValidationError
from django.contrib.auth import get_user_model

class SignUpForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['phone_number', ]
        
    def clean_phone_number(self):
        user_list = get_user_model()
        phone_number = self.cleaned_data['phone_number']
        if user_list.objects.filter(phone_number=phone_number).exists():
            raise ValidationError('Phone Number already registered on website.')
        if len('phone_number') != 11 and 'phone_number'[0:1] != '09':
            raise ValidationError('Please enter a correct phone number.')
        return phone_number
