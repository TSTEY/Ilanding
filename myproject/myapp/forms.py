from django import forms
from . import models

class HeaderForm(forms.ModelForm):
    class Meta:
        model = models.Header
        fields = ['name','address']
    
class BlockOneForm(forms.ModelForm):
    class Meta:
        model = models.BlockOne
        fields = ['name_1','name_2','button_1','button_2']
    
class BlockTwoForm(forms.ModelForm):
    class Meta:
        model = models.BlockTwo
        fields = ['name','text']
    
class BlockThreeForm(forms.ModelForm):
    class Meta:
        model = models.BlockThree
        fields = ['name','text']
    
class BlockFourForm(forms.ModelForm):
    class Meta:
        model = models.BlockFour
        fields = ['name','text','button']
    
class BlockFiveForm(forms.ModelForm):
    class Meta:
        model = models.BlockFive
        fields = ['imges','name','profession','text']
    
class BlockSixForm(forms.ModelForm):
    class Meta:
        model = models.BlockSix
        fields = ['number','name']
    
class BlockSevenForm(forms.ModelForm):
    class Meta:
        model = models.BlockSeven
        fields = ['name','text']
    
class BlockEightForm(forms.ModelForm):
    class Meta:
        model = models.BlockEight
        fields = ['name','text','text_2','text_3','text_4']
    
class BlockNineForm(forms.ModelForm):
    class Meta:
        model = models.BlockNine
        fields = ['name','text']
    
class BlockTenForm(forms.ModelForm):
    class Meta:
        model = models.BlockTen
        fields = ['name','text','button']
    
class FooterForm(forms.ModelForm):
    class Meta:
        model = models.Footer
        fields = ['name_1','name_2','name_3','name_4']
    
    
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class CustomUserCreationUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password')
        
        def clean_password2(self):
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')
            
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError("Пароли не совпадают.")
            if len(password1) < 6:
                raise forms.ValidationError("Пароль должен быть длиной не менее 6 символов.")
            # Добавьте свои проверки, если нужно
            return password2