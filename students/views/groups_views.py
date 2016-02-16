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



# # Views for Groups
# def groups_list(request):
# 	groups = (
# 		{'id': 1,
# 		 'groups_name': u'МтМ-21',
# 		 'star_name': u'Ячменев Олег'},
# 		{'id': 2,
# 		 'groups_name': u'МтМ-22',
# 		 'star_name': u'Онов Дмитро'},
# 		{'id': 3,
# 		 'groups_name': u'МтМ-23',
# 		 'star_name': u'Чамин Степан'},
# 	)	
# 	return render(request, 'students/groups_list.html',
# 		{'groups': groups})


# from ..models import Group
from ..models.group_models import Group
from ..models.student_models import Student


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def groups_list(request):
	groups = Group.objects.all()

	# try to order groups list
	
	order_by = request.GET.get('order_by', '')
	
	if order_by == '':
		order_by = 'title'
		st_def = '1'
	else:
		st_def ='0'	
    #	комент
		# получаем в GET запросе параметр order_by, когда пользователь щелкнет по ссылке 
		#  <a href={% url "home" %}?order_by=last_name>Фамилия&uarr;</a> 
		# GET вернет нам в order_by - last_name or first_name or ticket
		# параметр запроса сразу за знаком ?
		# если пользователь не щелкал по ссылке, то order_by - пустой, 
		# и мы присваиваем ему значение 'last_name'
		# это мы устанавливаем сотрировку вывода по умолчанию по этому полю
	if order_by in ('title', 'leader', 'id'):
		groups = groups.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			groups = groups.reverse()

	# paginate groups
	paginator = Paginator(groups, 3)
	page = request.GET.get('page')
	try:
		groups = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		groups = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver
		# last page of results.
		groups = paginator.page(paginator.num_pages)


	return render(request, 'students/groups_list.html',
		{'groups': groups, 'st_def' : st_def})

	
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