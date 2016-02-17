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
from ..models.group_models import Group
from ..models.ispit_models import Ekzamen, Predmet, Prepad

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Views for Groups

# def ispit_list(request):
# 	return render(request, 'students/ispit_list.html', {})



def ispit_list(request):
	ispit = Ekzamen.objects.all()

	# try to order groups list
	
	order_by = request.GET.get('order_by', '')
	
	if order_by == '':
		order_by = 'birthday'
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
	if order_by in ('birthday', 'predmet_name', 'prepad_name', 'student_group'):
		ispit = ispit.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			ispit = ispit.reverse()

	# paginate ispit
	paginator = Paginator(ispit, 5)
	page = request.GET.get('page')
	try:
		ispit = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		ispit = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver
		# last page of results.
		ispit = paginator.page(paginator.num_pages)


	return render(request, 'students/ispit_list.html',
		{'ispit': ispit, 'st_def' : st_def})

def ispit_add(request):
	return HttpResponse('<h1>ispit Add Form</h1>')
def ispit_edit(request, sid):
	return HttpResponse('<h1>Edit ispit %s</h1>' % sid)
def ispit_delete(request, sid):
	return HttpResponse('<h1>Delete ispit %s</h1>' % sid)


