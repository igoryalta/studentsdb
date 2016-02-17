# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Ekzamen(models.Model):
	"""Ekzamen Model"""

	class Meta(object):
		verbose_name = u"Экзамен"
		verbose_name_plural = u"Экзамен"
	
	predmet_name = models.ForeignKey('Predmet',
		verbose_name=u"Название предмета",
		blank=False,
		null=True,
		on_delete=models.PROTECT)

	prepad_name = models.ForeignKey('Prepad',
		verbose_name=u"Преподователь",
		blank=False,
		null=True,
		on_delete=models.PROTECT)

	birthday = models.DateField(
		blank=False,
		verbose_name=u"Дата экзамена",
		null=True)

	student_group = models.ForeignKey('Group',
		verbose_name=u"Група",
		blank=False,
		null=True,
		on_delete=models.PROTECT)

	def __unicode__(self):
		return u"%s (%s %s) %s %s" % (self.predmet_name, self.prepad_name.first_name, self.prepad_name.last_name, self.student_group, self.birthday)




class Predmet(models.Model):
	"""Predmet Model"""

	class Meta(object):
		verbose_name = u"Предмет"
		verbose_name_plural = u"Предмет"
	
	predmet_name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Название предмета")

	def __unicode__(self):
		return u"%s" % (self.predmet_name)



class Prepad(models.Model):
	"""Prepad Model"""

	class Meta(object):
		verbose_name = u"Преподователь"
		verbose_name_plural = u"Преподователь"

	first_name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Ім'я")

	last_name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Прізвище")

	def __unicode__(self):
		return u"%s %s" % (self.first_name, self.last_name)



