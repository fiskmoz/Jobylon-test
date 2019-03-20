from django import forms

# Defined custom form to import text from a textarea. 
# Also enforces the max lenght of 1000 if the form is to be valid.
class MessageForm(forms.Form):
    message = forms.CharField(label='', max_length=1000, 
    widget=forms.Textarea(attrs= {'id': 'message_form', 'maxlength': '1000', 'class': 'container' , 'placeholder' : 'Write a message...', 'style': 'width:80%; height: 100px'}))