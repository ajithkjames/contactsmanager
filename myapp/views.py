from django.shortcuts import render_to_response
from myapp.models import Member,Members_contact,Group,contract
from django.shortcuts import render_to_response
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
from django import forms
from django.template import RequestContext
import django_excel as excel
import pyexcel.ext.xls
import pyexcel.ext.xlsx
import pyexcel.ext.ods
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from models import EmailForm
from models import ContactForm
from models import MemberForm



#form for uploading exel file
class UploadFileForm(forms.Form):
    file = forms.FileField()



def members(request):
	return render_to_response('members.html',{'members': Member.objects.all() },RequestContext(request))

def contact(request):
    return render_to_response('contact.html',RequestContext(request, {'members': Member.objects.all() }))


def member(request, member_id):
	return render_to_response('member.html', {'member': Member.objects.get(id=member_id),
        'members_contact': Members_contact.objects.filter(member_id=member_id),
        'groups':Group.objects.filter(member=member_id)})

def email(request, member_id):
    return render_to_response('email.html',RequestContext(request,  {
        'groups':Group.objects.filter(member=member_id)}))
    
def import_data(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
       
        if form.is_valid():
            request.FILES['file'].save_book_to_database(
                models=[Members_contact],
                
                mapdicts=[
                    {"dob": "dob","email": "email","first_name": "first_name",
          "gender": "gender","id": "id","last_name": "last_name","member_id": "member_id"}]
            )

            return HttpResponse("OK", status=200)

        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render_to_response(
        'upload_form.html',
        {
            'form': form,
            'title': 'Import excel data into database ',
            'header': 'Please upload the exel file:'
        },
        context_instance=RequestContext(request))


def download(request, file_type):
    sheet = excel.pe.Sheet(data)
    return excel.make_response(sheet, file_type)

    
def download_as_attachment(request, file_type, file_name):
    return excel.make_response_from_array(data, file_type, file_name=file_name)


def export_data(request, atype):
    if atype == "sheet":
        return excel.make_response_from_a_table(
            Members_contact, 'xls', file_name="sheet")
    elif atype == "book":
        return excel.make_response_from_tables(
            [Question, Choice1], 'xls', file_name="book")
    elif atype == "custom":
        question = Question.objects.get(slug='ide')
        query_sets = Choice1.objects.filter(question=question)
        column_names = ['choice1_text', 'id', 'votes']
        return excel.make_response_from_query_sets(
            query_sets,
            column_names,
            'xls',
            file_name="custom"
        )
    else:
        return HttpResponseBadRequest("Bad request. please put one of these \
                                      in your url suffix: sheet, book or custom")

def sendmail(request):
    
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            groupcode=form.cleaned_data['groups']
            mem_list = Group.objects.filter(group_code=groupcode).values_list('members__pk', flat=True)
            members = Members_contact.objects.filter(id__in=mem_list)
            for mem in members:
                recipient= mem.email
                send_mail(subject, message, "Ajith", [recipient])
                return HttpResponseRedirect('/thankyou/') 
            
        else:
            return render_to_response('my_template.html', {'form': form})
            return HttpResponseRedirect('/members/all')
    else:
            return HttpResponseRedirect('/email/') 

def contact(request):
    return render_to_response('contact.html',RequestContext(request, {'members': Member.objects.all() }))
def add_member(request):
    return render_to_response('addmember.html',RequestContext(request, {'contract': contract.objects.all() }))

def addcontact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            member = form.cleaned_data['member']
            first_name = form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            dob = form.cleaned_data['dob']
            gender = form.cleaned_data['gender']
            email=form.cleaned_data['email']
            print member
            mem=Member.objects.filter(id=member)[0]
            new_contact=Members_contact.objects.create(member =mem,first_name =first_name,last_name=last_name,dob =dob,gender =gender,email=email)
         
            return HttpResponse("OK New contact added ", status=200)
        else:
            return render_to_response('my_template.html', {'form': form})
            
    else:
            return HttpResponseRedirect('/members/all/')


def group_contacts(request, group_code):
    mem_list = Group.objects.filter(group_code=group_code).values_list('members__pk', flat=True)
    grp = Group.objects.filter(group_code=group_code)
    mid=grp[0].member_id
    # mem=Member.objects.filter(id__in=mem_list)
    members = Members_contact.objects.filter(id__in=mem_list)
    
    return render_to_response('groupcontacts.html',{'members':members ,'group':grp,'member_id':mid,'group_code':group_code})


def memberadd(request):
    
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            
            first_name = form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            contract_details = form.cleaned_data['contract_details']
            con=contract.objects.filter(id=contract_details)[0]
            new_member=Member.objects.create(first_name =first_name,last_name=last_name,email=email,contract_details=con)
          
            return HttpResponse("OK New User is added", status=200)
           
        else:
            return render_to_response('my_template.html', {'form': form})
            
    else:
            return HttpResponseRedirect('/members/all/')


