from django import forms


class ProcessForm(forms.Form):
    input1 = forms.CharField(widget=forms.Textarea)


    output1 = forms.CharField(widget=forms.Textarea, required=False)


    # input2 = forms.CharField(max_length=1000)
    # output2 = forms.CharField(widget=forms.Textarea)
    # output3 = forms.CharField(widget=forms.Textarea)
