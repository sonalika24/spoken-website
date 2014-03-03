from django.conf.urls import patterns, url
from events import views
urlpatterns = patterns('',
	#url(r'^$', views.state, name='state'),
	url(r'states/$', views.state, name='states'),
	url(r'states/new/$', views.new_state, name='new_state'),
	url(r'states/(\d+)/edit/$', views.edit_state, name='edit_state'),
	url(r'update-district/$', views.update_district, name='update_district'),
	url(r'check-district/$', views.check_district, name='check_district'),
	url(r'update-location/$', views.update_location, name='update_location'),
	url(r'update-college/$', views.update_college, name='update_college'),
	
    url(r'roles/rp/$', views.roles_rp, name='roles_rp'),
    url(r'roles/rp/new/$', views.new_roles_rp, name='new_roles_rp'),
	url(r'roles/rp/(\d+)/edit/$', views.edit_roles_rp, name='edit_roles_rp'),
    
    url(r'ac/$', views.ac, name='ac'),
    url(r'ac/new/$', views.new_ac, name='new_ac'),
    url(r'ac/(\d+)/edit/$', views.edit_ac, name='edit_ac'),
    
    url(r'organiser/(?P<status>\w+)/$', views.rp_organiser, name='rp_organiser'),
    url(r'organiser/active/(?P<code>\w+)/(?P<userid>\d+)/$', views.rp_organiser_confirm, name='rp_organiser_confirm'),
    url(r'organiser/block/(?P<code>\w+)/(?P<userid>\d+)/$', views.rp_organiser_block, name='rp_organiser_block'),
    
    url(r'organiser/request/(?P<username>\w+)/$', views.organiser_request, name='organiser_request'),
    url(r'organiser/(?P<username>\w+)/edit/$', views.organiser_edit, name='organiser_edit'),
    url(r'organiser/view/(?P<username>\w+)/$', views.organiser_view, name='organiser_view'),
    
    url(r'invigilator/(?P<status>\w+)/$', views.rp_invigilator, name='rp_invigilator'),
    url(r'invigilator/active/(?P<code>\w+)/(?P<userid>\d+)/$', views.rp_invigilator_confirm, name='rp_invigilator_confirm'),
    url(r'invigilator/block/(?P<code>\w+)/(?P<userid>\d+)/$', views.rp_invigilator_block, name='rp_invigilator_block'),
    
    url(r'invigilator/request/(?P<username>\w+)/$', views.invigilator_request, name='invigilator_request'),
    url(r'invigilator/(?P<username>\w+)/edit/$', views.invigilator_edit, name='invigilator_edit'),
    url(r'invigilator/view/(?P<username>\w+)/$', views.invigilator_view, name='invigilator_view'),
    
    url(r'dept/$', views.dept, name='dept'),
    url(r'dept/new/$', views.new_dept, name='new_dept'),
	url(r'dept/(\d+)/edit/$', views.edit_dept, name='edit_dept'),
	
    url(r'workshop/request/$', views.workshop_request, name='workshop_request'),
    
    #Ajax 
    url(r'ajax-ac-state/$', views.ajax_ac_state, name='ajax_ac_state'),
    url(r'ajax-ac-location/$', views.ajax_ac_location, name='ajax_ac_location'),
    url(r'ajax-ac-pincode/$', views.ajax_ac_pincode, name='ajax_ac_pincode'),
    url(r'ajax-district-collage/$', views.ajax_district_collage, name='ajax_district_collage'),
    #url(r'add$', views.add_contact, name='add_contact'),
    #url(r'edit/(\d+)$', views.edit_contact, name='edit_contact'),   
    #url(r'delete/(\d+)$', views.delete_contact, name='delete_contact'),
)