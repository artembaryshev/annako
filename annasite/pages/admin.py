# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from pages.models import AbstractPage, SiteNavigation

admin.site.register([AbstractPage, SiteNavigation])
# admin.site.register(SiteNavigation)
