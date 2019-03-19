from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(label='', max_length=1000, 
    widget=forms.Textarea(attrs= {'id': 'message_form', 'maxlength': '1000', 'class': 'container' , 'placeholder' : 'Write a message...', 'style': 'width:80%; height: 100px'}))