from django.forms import ModelForm, ValidationError
from django.contrib.auth import get_user_model
# import random 
# from .utils import send_verification_code

class RegistrationForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['phone_number', ]
        
    def clean_phone_number(self):
        user_list = get_user_model()
        phone_number = self.cleaned_data['phone_number']
        # if User.objects.filter(phone_number=phone_number).exists():
        if user_list.objects.filter(phone_number=phone_number).exists():
            raise ValidationError('Phone Number already registered on website.')
        return phone_number

    # def save(self, commit=False):
    #     user = super().save(commit=False)
    #     verification_code = str(random.randint(100000, 999999))  # Generate 6-digit verification code
    #     user.verification_code = verification_code
    #     user.save()
    #     send_verification_code(user.phone_number, verification_code)  # Send code using helper function
    #     return user
