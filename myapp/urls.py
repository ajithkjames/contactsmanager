from django.conf.urls import url
from django.contrib import admin
import myapp.views
from django.views.generic import TemplateView

urlpatterns = [
   
	url(r'^all/$', myapp.views.members),
	url(r'^member/(?P<member_id>\d+)/$', myapp.views.member),
	url(r'^import/', myapp.views.import_data, name="import"),
	url(r'^export/(.*)', myapp.views.export_data, name="export"),
	

]