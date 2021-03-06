"""studentsdb URL Configuration

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
from django.contrib import admin



from .settings import MEDIA_ROOT, DEBUG




urlpatterns = [
	# Students urls
	url(r'^$', 'students.views.students_views.students_list', name='home'),
	url(r'^students/add/$', 'students.views.students_views.students_add',
		name='students_add'),
	url(r'^students/(?P<sid>\d+)/edit/$',
		'students.views.students_views.students_edit',
		name='students_edit'),
	url(r'^students/(?P<sid>\d+)/delete/$',
		'students.views.students_views.students_delete',
		name='students_delete'),

	# Groups urls
	url(r'^groups/$', 'students.views.groups_views.groups_list', name='groups'),
	url(r'^groups/add/$', 'students.views.groups_views.groups_add',
		name='groups_add'),
	url(r'^groups/(?P<gid>\d+)/edit/$',
		'students.views.groups_views.groups_edit',
		name='groups_edit'),
	url(r'^groups/(?P<gid>\d+)/delete/$',
		'students.views.groups_views.groups_delete',
		name='groups_delete'),

	# jornal urls
	url(r'^journal/$', 'students.views.journal_views.journal_list', name='journal'),
	
	# ispit urls
	url(r'^ispit/$', 'students.views.ispit_views.ispit_list', name='ispit'),
	url(r'^ispit/(?P<sid>\d+)/edit/$',
		'students.views.ispit_views.ispit_edit',
		name='ispit_edit'),
	url(r'^ispit/add/$', 'students.views.ispit_views.ispit_add',
		name='ispit_add'),

	

    url(r'^admin/', admin.site.urls),
]


if DEBUG:
	# serve files from media folder
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
			'document_root': MEDIA_ROOT}))
	