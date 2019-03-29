from django import forms
from .models import Message

# Defined custom form to import text from a textarea. 
# Also enforces the max lenght of 1000 if the form is to be valid.
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['Message']
        labels = {
            'Message': '',
        }
        widgets = {
            'Message' : forms.Textarea(attrs= {'id': 'message_form', 'maxlength': '1000', 'class': 'container' , 'placeholder' : 'Write a message...', 'style': 'width:80%; height: 100px'}),
        }
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['Message'].initial = ''
        