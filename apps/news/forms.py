from news.models import News
from perms.forms import TendenciBaseForm
from django import forms
from tinymce.widgets import TinyMCE

class NewsForm(TendenciBaseForm):

    body = forms.CharField(required=False,
        widget=TinyMCE(attrs={'style':'width:100%'}, 
        mce_attrs={'storme_app_label':News._meta.app_label, 
        'storme_model':News._meta.module_name.lower()}))
        
    class Meta:
        model = News
        fields = (
        'headline',
        'slug',
        'summary',
        'body',
        'source',
        'website',
        'release_dt',
        'timezone',
        'first_name',
        'last_name',
        'phone',
        'fax',
        'email',
        'tags',
        'allow_anonymous_view',
        'allow_user_view',
        'allow_user_edit',
        'syndicate',
        'status',
        'status_detail',
        'user_perms',
        )
      
    def __init__(self, user=None, *args, **kwargs): 
        self.user = user
        super(NewsForm, self).__init__(user, *args, **kwargs)
        if self.instance.pk:
            self.fields['body'].widget.mce_attrs['app_instance_id'] = self.instance.pk
        else:
            self.fields['body'].widget.mce_attrs['app_instance_id'] = 0        
        
        
        