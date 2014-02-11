# A Django template tag for creating inline CSS

**Package name: inline_css**

A simple wrapper around [Pynliner](https://github.com/rennat/pynliner) to generate inline CSS in a Django template. Ideal for sending HTML email.


### Installation

Add 'inline_css' to INSTALLED_APPS


### Requirements

- [Pynliner](https://github.com/rennat/pynliner) >= 0.5.0


### Usage

	{% load inline_css %}
	{% inline_css %}
		<style>h1 { color:#ffcc00; }</style>
		<h1>Hello World!</h1>
	{% endinline_css %}


### Output

	<h1 style="color: #fc0">Hello World!</h1>

