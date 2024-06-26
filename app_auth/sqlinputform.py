from django import forms

class SqlInputForm(forms.Form):    
    sql = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 25,
            'id': 'sql-input',
            'spellcheck': 'false',
            'wrap': 'off',
            'required': 'true',
            
        })
        ,label=""
    )
    
    def __init__(self, *args, **kwargs):
        initial_text = kwargs.pop('initial_text', '')  # Get initial_text from kwargs or default to empty string
        super().__init__(*args, **kwargs)
        self.fields['sql'].initial = initial_text    
    
    