from django import forms


class ProcessForm(forms.Form):
    input1 = forms.CharField(widget=forms.Textarea)
    input2 = forms.CharField(widget=forms.Textarea)
    input3 = forms.CharField(widget=forms.Textarea)

    output1 = forms.CharField(widget=forms.Textarea)
    output2 = forms.CharField(widget=forms.Textarea)
    output3 = forms.CharField(widget=forms.Textarea)
