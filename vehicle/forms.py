from django import forms

from vehicle.models import Parts

class PartsForm(forms.ModelForm):
    class Meta:
        model = Parts
        fields = (
            'name',
            'manufactuer',
            'quantity',
        )
    
    def clean(self, *args, **kwargs):
        cleaned_data = super(PartsForm, self).clean(*args, **kwargs)
        if cleaned_data['quantity'] > 10:
            raise forms.ValidationError('Quantity must be less than 10')
        return cleaned_data
    
    def clean_manufactuer(self):
        if not self.cleaned_data['manufactuer'] == 'Hyundai':
            raise forms.ValidationError('Manufacturer must be Hyundai')
        return self.cleaned_data['manufactuer']