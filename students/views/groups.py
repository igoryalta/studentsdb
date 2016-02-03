# -*- coding: utf-8 -*-

from django.shortcuts import render
 
# Create your views here.
from django.http import HttpResponse

# def students_list(request, sid):
# 	try:
# 		sid = int(sid)
# 	except ValueError:
# 		raise Http404
# 	else:	
# 		return HttpResponse('<h1>Hello Word</h1>')


# Views for Groups
def groups_list(request):
	groups = (
		{'id': 1,
		 'groups_name': u'МтМ-21',
		 'star_name': u'Ячменев Олег'},
		{'id': 2,
		 'groups_name': u'МтМ-22',
		 'star_name': u'Онов Дмитро'},
		{'id': 3,
		 'groups_name': u'МтМ-23',
		 'star_name': u'Чамин Степан'},
	)	
	return render(request, 'students/groups_list.html',
		{'groups': groups})
	
def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')
def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)
def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)


# from django.shortcuts import render

# def students_list(request):
# 	return render(request, 'demo.html', {})


# from django.http import HttpResponse
# from django.template import RequestContext, loader
# def students_list(request):
# template = loader.get_template('demo.html')
# context = RequestContext(request, {})
# return HttpResponse(template.render(context))