# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

#admin interface

from .models import Book

#register Book to show it at the admin site
admin.site.register(Book)