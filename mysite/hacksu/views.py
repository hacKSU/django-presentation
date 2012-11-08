from django.shortcuts import render_to_response
from hacksu.models import Member, Project

def index(request):
    members = Member.objects.all()
    projects = Project.objects.all()
    return render_to_response('hacksu/index.html', {'members': members, 'projects': projects})
