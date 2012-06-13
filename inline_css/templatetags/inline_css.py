# -*- coding: utf-8 -*-
# By David Moss
# Requires Pynliner https://github.com/rennat/pynliner

from django.template import Library
from django import template
import pynliner

register = Library()

@register.filter
def do_inline_css(parser, token):
	nodelist = parser.parse(('endinline_css',))
	parser.delete_first_token()
	return InlineCSSNode(nodelist)

class InlineCSSNode(template.Node):
	def __init__(self, nodelist):
		self.nodelist = nodelist
	def render(self, context):
		# Encode entities to ascii &#000; style as Pynliner seems to choke otherwise
		output = self.nodelist.render(context).encode('ascii', 'xmlcharrefreplace')
		return pynliner.Pynliner().from_string(output).run()

inline_css = register.tag("inline_css", do_inline_css)