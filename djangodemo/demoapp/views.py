from django.shortcuts import render, render_to_response

def home_page_view(request, template_name="home.html"):
	return render_to_response(template_name)