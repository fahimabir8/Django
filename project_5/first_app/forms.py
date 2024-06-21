from django import forms
from django.core import validators
class contactForm(forms.Form):
    name = forms.CharField(label='Full Name', help_text='Text should be at least 50 characters', required= True, error_messages={'required': 'Please enter your name.'},widget= forms.Textarea(attrs= {'id':'text_area','placeholder': 'Enter Name'}))
    email = forms.EmailField(label ='User Email')
    age = forms.CharField(widget=forms.NumberInput)
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput(attrs= {'type':'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    CHOICES = [('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=CHOICES, widget= forms.RadioSelect)
    TOPPINGS = [('C','Cheese'),('M','Mushrooms'),('P','Pepperoni')]
    pizza = forms.MultipleChoiceField(choices=TOPPINGS, widget= forms.CheckboxSelectMultiple)
    
# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
    
#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError("Name should be atleast 10 characters")
#     #     return valname    
        
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("Your email is missing .com")
#     #     return valemail           
    
#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 10:
#             raise forms.ValidationError("Name should contain at least 10 characters")
        
#         if '.com' not in valemail:
#             raise forms.ValidationError("Your email is missing .com")
        
class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput,validators=[validators.MinLengthValidator(10,message='Name must contain 10 characters')])
    email = forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message='Enter a valid Email')])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(45,message="age must be less than 45"),validators.MinValueValidator(20,message="age must be greater than 20")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],message='File extension must be ended with .pdf' )])
    
class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password'] 
        val_conpass = self.cleaned_data['confirm_password'] 
        val_name = self.cleaned_data['name']
        
        if val_conpass != val_pass:
            raise forms.ValidationError("Password doesn't match")
        if len(val_name) < 10:
            raise forms.ValidationError("Name must be at least 10 characters")