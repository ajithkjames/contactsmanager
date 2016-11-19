"""contact_manager URL Configuration


The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.conf.urls import url
from django.contrib import admin
import myapp.views
from django.views.generic import TemplateView
import settings

urlpatterns =[
   url(r'^$', myapp.views.members),
  url(r'^admin/', include(admin.site.urls)),
  url(r'^members/', include('myapp.urls')),
  url(r'^import/', myapp.views.import_data, name="import"),
  url(r'^export/(.*)', myapp.views.export_data, name="export"),
  url(r'^send/$', myapp.views.sendmail),
  url(r'^email/member/(?P<member_id>\d+)/$', myapp.views.email, name="email"),
  url(r'^thankyou/$', TemplateView.as_view(template_name='thankyou.html'), name='thankyou'),
  url(r'^placement/$', TemplateView.as_view(template_name='placement.html'), name='placement'),
  url(r'^addcontact/$', myapp.views.addcontact),
  url(r'^contact/$', myapp.views.contact),
  url(r'^member/$', myapp.views.add_member),
  url(r'^memberadd/$', myapp.views.memberadd),
  url(r'^groupcontacts/group/(?P<group_code>\d+)/$', myapp.views.group_contacts),
]
