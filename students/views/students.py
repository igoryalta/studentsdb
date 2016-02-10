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


# Views for Students
# def students_list(request):
# 	return render(request, 'students/students_list.html', {})

# def students_list(request):
# 	students = (
# 		{'id': 1,
# 		 'first_name': u'Віталій',
# 		 'last_name': u'Подоба',
# 		 'ticket': 235,
# 		 'image': 'img/1.jpg'},
# 		{'id': 2,
# 		 'first_name': u'Корост',
# 		 'last_name': u'Андрій',
# 		 'ticket': 2123,
# 		 'image': 'img/2.jpg'},
# 		{'id': 3,
# 		 'first_name': u'Остов',
# 		 'last_name': u'Степан',
# 		 'ticket': 2123,
# 		 'image': 'img/3.jpg'},
# 	)
# 	return render(request, 'students/students_list.html',
# 		{'students': students})

from ..models import Student


def students_list(request):
	students = Student.objects.all()


	# try to order students list
	
	# reverse = ''

	order_by = request.GET.get('order_by', '')
	
	if order_by == '':
		order_by = 'last_name'
		st_def = '1'
	else:
		st_def ='0'	
	# получаем в GET запросе параметр order_by, когда пользователь щелкнет по ссылке 
	#  <a href={% url "home" %}?order_by=last_name>Фамилия&uarr;</a> 
	# GET вернет нам в order_by - last_name or first_name or ticket
	# параметр запроса сразу за знаком ?
	# если пользователь не щелкал по ссылке, то order_by - пустой, и мы присваиваем ему значение 'last_name'
	# это мы устанавливаем сотрировку вывода по умолчанию по этому полю


	if order_by in ('last_name', 'first_name', 'ticket', 'id'):
		students = students.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			students = students.reverse()

	return render(request, 'students/students_list.html',
		{'students': students, 'st_def' : st_def})

def students_add(request):
	return HttpResponse('<h1>Student Add Form</h1>')
def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)
def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)



# from django.shortcuts import render

# def students_list(request):
# 	return render(request, 'demo.html', {})


# from django.http import HttpResponse
# from django.template import RequestContext, loader
# def students_list(request):
# template = loader.get_template('demo.html')
# context = RequestContext(request, {})
# return HttpResponse(template.render(context))