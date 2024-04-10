# Django two step SignUp/SignIn authentication model with SMS

This repo contains a **CustomUserModel** for authenticating users with SMS API. Users can signup and login with a verification code validation that is sent to their mobile phone through SMS. 

This repo only contains API for [MeliPayamak](https://www.melipayamak.com/) system using *send message via base number* or so-called *message by patterns* method. 

*since i don't have access to other sms service providers , please update the verification code send function based on the API for your provider.*

## Initializing in the project
Clone **users** directory in your project and add it to `installed apps`. Remember to do it before making any migration, so custom user model could be applied properly. 
Install requirements.txt , you might need to install other modules based on the API of your SMS provider platform. 

## Configuration 
Configure your SMS provider API parameters in **setting.py** :
```
# SMS Provider API 
SMS_API = {
    'username' : env('username'),
    'password' : env('password'),
    'bodyId' : env('bodyId'),
}
# Custom User Model
AUTH_USER_MODEL = 'users.CustomUser'
```
`bodyId` is the id for pattern messages using base number, get it from your SMS provider panel. 
The API for sms service provider setup is in `users/api_sms.py`. The model is based on *MeliPayamk provider* , then update it based on the documentations and guides from your provider.  

Views for Signup, Login, Verify Signup and Verify Login has been added, `users/views.py`. you can customize the templates in `users/templates/users/`. 

