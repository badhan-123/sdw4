from django import forms 

class contactForm(forms.Form):
    name=forms.CharField(label='urname ')
    file=forms.FileField()
    email=forms.EmailField()
    age=forms.IntegerField()
    weight=forms.FloatField()
    payment=forms.DecimalField()
    schedule=forms.DateTimeField()
    addon=[('r','raita'),('p','payesh'),('d','doi')]
    extra=forms.ChoiceField(choices=addon)
    menu=[('r','rice'),('p','parata'),('b','biriyani')]
    order=forms.MultipleChoiceField(choices=menu)


class PasswordValidationProject(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
    con_password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data= super().clean()
        val_pass=self.cleaned_data['password']
        val_conpass=self.cleaned_data['con_password']
        val_name=self.cleaned_data['name']
        if val_conpass!=val_pass:
            raise forms.ValidationError("pass dont match")
        if len(val_name<15):
            raise forms.ValidationError("name too short")

