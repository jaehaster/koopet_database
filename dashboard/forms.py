from django import forms
from .models import Report, Associate

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('associate', 'item_list', 'total_amount', 'atax_published', 'completed', )

class AssociateForm(forms.ModelForm):
    class Meta:
        model = Associate
        fields = ('name', 'associate_type', 'person_in_charge', 'main_items', 'bank', 'account_number', 'bank_owner', 'phone_number', 'email_address', 'web_address', 'social_security_number')
