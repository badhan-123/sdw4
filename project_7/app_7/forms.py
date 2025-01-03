from django import forms
from app_7.models import StudentModel
class StudentForm(forms.ModelForm):
    class Meta:
        model= StudentModel
        fields= '__all__'
        labels= {
            'name':"Student Name",
            'roll':"Student Roll"
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'btn-primary'}),
            'roll':forms.PasswordInput()
            
        }

        help_texts={
            'name':"write name"
        }
        error_messages={
            'name':{'required':'ur name' }
            }