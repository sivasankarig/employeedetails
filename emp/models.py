# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


@python_2_unicode_compatible 
class Employee(models.Model):
    emp_name = models.CharField(max_length=200)
    emp_email= models.CharField(max_length=200)
    pub_date = models.DateTimeField('datecreated')
    def __str__(self):
        return self.emp_name
        
