# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class UserInfo(models.Model): #stores additional info not in built-in User model
	SIDE_CHOICES = (('A', 'A'), ('B', 'B'), ('N', 'Not on side'))
	ROLE_CHOICES = (('S', 'Spectator'), ('D', 'Debater'), ('M', 'Moderator'))

	user = models.ForeignKey(User, unique=True)
	current_side = models.CharField(max_length = 1, choices = SIDE_CHOICES, default = 'N')
	current_role = models.CharField(max_length = 1, choices = ROLE_CHOICES, default = 'S')

class DailyDebate(models.Model):
	STATUS_CHOICES = (('N', 'Not started'),('O', 'Open'),('V', 'In voting'),('C', 'Complete'))

	start_date = models.DateTimeField(auto_now_add = True)
	topic = models.TextField()
	status = models.CharField(max_length = 1, choices = STATUS_CHOICES, default = 'N')
	is_current_debate = models.BooleanField(default = False)

class Argument(models.Model):
	SIDE_CHOICES = (('A', 'A'), ('B', 'B'))

	isActive = models.BooleanField(default = True)
	isReported = models.BooleanField(default = False)
	reasonForBeingReported = models.TextField()
	reportedDate = models.DateTimeField(auto_now = True)

	author = models.ForeignKey(User, on_delete = models.CASCADE)
	#may want to change to SET_NULL if desired post deletion behavior is to preserve the post unless an admin is the one who deletes it
	side = models.CharField(max_length = 1, choices = SIDE_CHOICES)
	parent_debate = models.ForeignKey('DailyDebate', on_delete = models.CASCADE)
	initial_post_date = models.DateTimeField(auto_now_add = True)
	last_edited_date = models.DateTimeField(auto_now = True)
	content = models.TextField()
	source = models.URLField()

class Comment(models.Model):
	SIDE_CHOICES = (('A', 'A'), ('B', 'B'))

	isActive = models.BooleanField(default = True)
	isReported = models.BooleanField(default = False)
	reasonForBeingReported = models.TextField()
	reportedDate = models.DateTimeField(auto_now = True)


	parent_post = models.ForeignKey(Argument)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	side = models.CharField(max_length = 1, choices = SIDE_CHOICES)
	parent_debate = models.ForeignKey('DailyDebate', on_delete = models.CASCADE)
	initial_post_date = models.DateTimeField(auto_now_add = True)
	last_edited_date = models.DateTimeField(auto_now = True)
	content = models.TextField()
	source = models.URLField()

    
class Rubric(models.Model):
    post = models.ForeignKey(Argument)
    
    understand_topic = models.IntegerField()
    respectful = models.IntegerField()
    logical = models.IntegerField()
    accurate_info = models.IntegerField()
    convincing = models.IntegerField()
    total = models.IntegerField()
    
    grader = models.ForeignKey(User)