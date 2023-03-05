from django import forms  
from channels.models import Channel  
class ChannelForm(forms.ModelForm):  
    class Meta:  
        model = Channel  
        fields = ('title','link','description','start_date','icon','banner','video','category','status','tag')
        
        
        
#fields = "__all__"  
#fields = ('eid','face','good','hire_date','eemail')