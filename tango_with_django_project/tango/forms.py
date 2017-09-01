from django import forms
from tango.models import Category,Page,UserProfile
from django.contrib.auth.models import User
class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,help_text='Please enter a category name.')
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)

    class Meta:
        model = Category #与模型关联
        fields = ('name',)
class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,help_text='Please enter the title of the page.')
    url = forms.URLField(max_length=200,help_text='Please enter the URL of the page')
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    category = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label=None)

    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Page
        fields = ('title','url','views','category')
        #exclude = ('category',)
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
        return cleaned_data
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','email','password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website','picture')