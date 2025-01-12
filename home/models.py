# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Calendar(models.Model):

    #__Calendar_FIELDS__
    fyear = models.IntegerField(null=True, blank=True)
    period = models.IntegerField(null=True, blank=True)
    office_hours = models.IntegerField(null=True, blank=True)
    vac_days = models.IntegerField(null=True, blank=True)
    working_hours = models.IntegerField(null=True, blank=True)

    #__Calendar_FIELDS__END

    class Meta:
        verbose_name        = _("Calendar")
        verbose_name_plural = _("Calendar")


class Cc(models.Model):

    #__Cc_FIELDS__
    description = models.TextField(max_length=255, null=True, blank=True)
    code = models.IntegerField(null=True, blank=True)

    #__Cc_FIELDS__END

    class Meta:
        verbose_name        = _("Cc")
        verbose_name_plural = _("Cc")



#__MODELS__END
