from django import forms
from home.models import Blog, Subscription


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class SubscriptionForm(forms.ModelForm):
    your_email = forms.EmailField(required=True, label=False, widget=forms.TextInput(
        attrs={'type': 'email', 'id': 'email', "placeholder": "Email", 'autofocus': 'true'}))

    class Meta:
        model = Subscription
        fields = ('your_email', )


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
