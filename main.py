# coding: utf-8
# Copyright 2014 erpreciso
#
# MyOutdoorPlanner app

import webapp2
import jinja2
import os
import json
import urllib
import logging
import re

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
        autoescape = True)

class MainHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class Page(MainHandler):
	def get(self):
		self.render("backbone.html")

app = webapp2.WSGIApplication([
    ("/", Page),
], debug=True)
