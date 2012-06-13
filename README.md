# Django template tag for creating inline CSS using Pynliner

**Package name: inline_css**

Django template tag to generate inline CSS for any HTML it surrounds. 


### Installation

Add 'inline_css' to INSTALLED_APPS


### Requirements

- [Pynliner](https://github.com/rennat/pynliner)


### Usage
	
	{% load inline_css %}
	{% inline_css %} 
		<style>h1 { color:#ffcc00; }</style>
		<h1>Hello World!</h1>
	{% endinline_css %} 


### Output
	
	<h1 style="color: #fc0">Hello World!</h1>
	
