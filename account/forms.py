from django import forms
from .models import User
from Product.models import Product,Special
from django.contrib.auth.forms import UserCreationForm
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
class ProfileForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        user=kwargs.pop('user')
        super(ProfileForm,self).__init__(*args,**kwargs)
        self.fields['username'].help_text=False
        self.fields['email'].help_text=False
        if not user.is_superuser:
            self.fields['username'].disabled=True
            self.fields['email'].disabled=True
            self.fields['is_author'].disabled=True
            self.fields['is_seller'].disabled=True
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','is_author','is_seller']
class ShirtForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        user=kwargs.pop('user')
        super(ShirtForm,self).__init__(*args,**kwargs)
        self.fields['product'].queryset=Product.objects.shirt().filter(seller=user)

    class Meta:
        model=Special
        fields=['count','sizeshirt','product'
         # ,"price"
          ]
class ShoseForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        user=kwargs.pop('user')
        super(ShoseForm,self).__init__(*args,**kwargs)
        self.fields['product'].queryset=Product.objects.shose().filter(seller=user)
    class Meta:
        model=Special
        fields=['count','sizeshose','product'
         # ,"price"
        ]
class PantsForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        user=kwargs.pop('user')
        super(PantsForm,self).__init__(*args,**kwargs)
        self.fields['product'].queryset=Product.objects.pants().filter(seller=user)

    class Meta:
        model=Special
        fields=['count','sizepants','product','seller_2'
         # ,"price"
        ]
# shose
# pants
# shirt
# headgear
# manto
    
 
 
 
 
 