# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.shortcuts import render_to_response, get_object_or_404, render

class FlatPageView(TemplateView):
	template_name = 'layout.html'
	
