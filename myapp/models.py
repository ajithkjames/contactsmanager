from django.db import models
from django import forms
from django.utils.encoding import python_2_unicode_compatible
GENDER_CHOICES = (
    (0, 'Male'),
    (1, 'Female'),
    (2, 'Other')
)



class contract(models.Model):
    from_date=models.DateField()
    to_date=models.DateField()
    list_size=models.IntegerField()
    max_emails=models.IntegerField()

   
@python_2_unicode_compatible  # For Python 3.4 and 2.7
class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    contract_details=models.ForeignKey(contract, default='', on_delete=models.CASCADE)
    def __str__(self):
       return self.first_name

class Members_contact(models.Model):
    member=models.ForeignKey(Member, default='', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    email = models.EmailField()
    

    def __str__(self):
       return self.first_name

class Group(models.Model):
    member=models.ForeignKey(Member, default='', on_delete=models.CASCADE)
    group_code = models.CharField(unique=True,primary_key=True,max_length=30)
    group_name = models.CharField(max_length=30)
    group_description = models.CharField(max_length=100)
    members=models.ManyToManyField(Members_contact)

    def __str__(self):
       return self.group_name

class EmailForm(forms.Form):
    
      subject = forms.CharField(max_length=255)
      message = forms.CharField()
      groups = forms.CharField()
  
class ContactForm(forms.Form):
    
    member=forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    dob = forms.DateTimeField()
    gender = forms.CharField()
    email = forms.EmailField()

class GroupForm(forms.Form):

    member=forms.CharField()
    group_code = forms.CharField()
    group_name = forms.CharField()
    group_description = forms.CharField()
    members = forms.CharField()
    
class MemberForm(forms.Form):
    
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    contract_details = forms.CharField()
    