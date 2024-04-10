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
        return phone_number
