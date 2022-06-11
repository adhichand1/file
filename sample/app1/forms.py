from django import forms

class studentform(forms.Form):
    roll=forms.IntegerField()
    name=forms.CharField(max_length=50)
    age=forms.IntegerField()