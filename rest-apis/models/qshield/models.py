#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'CYX'

from orm import Model
from field import StringField, IntegerField, FloatField

class Tables(Model):
    __table__ = '*'
    __path__ = '*'

class Rankings(Model):
    __table__ = 'RANKINGS'
    __path__ = 'outsourced/RANKINGS'

    pageURL = StringField()
    pageRank = IntegerField()
    avgDuration = IntegerField()

class Uservisits(Model):
    __table__ = 'USERVISITS'
    __path__ = 'outsourced/USERVISITS'

    sourceIP = StringField()
    destURL = StringField()
    visitDate = StringField()
    adRevenue = FloatField()
    userAgent = StringField()
    countryCode = StringField()
    languageCode = StringField()
    searchWord = StringField()
    duration = IntegerField()
