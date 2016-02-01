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


# Views for Students
def students_list(request):
	return render(request, 'students/students_list.html', {})
def students_add(request):
	return HttpResponse('<h1>Student Add Form</h1>')
def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)
def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)
# Views for Groups
def groups_list(request):
	return HttpResponse('<h1>Groups Listing</h1>')
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