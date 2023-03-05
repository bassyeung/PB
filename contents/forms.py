from django import forms  
from contents.models import Content  
class Contentform(forms.ModelForm):  
    class Meta:  
        model = Content
        fields = "__all__"  


#fields = ('eid','face','good','hire_date','eemail')