
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,get_user_model,logout
from submission.models import mailerSubmission


def index(request):
	context = {}
	if request.POST:
		obj = mailerSubmission(name = request.POST.get('name'),
			email = request.POST.get('email'),
			number = request.POST.get('phone')
			)
		obj.save()
		if request.FILES.get('template'):
			obj.template = request.FILES.get('template')
			obj.save()
		return redirect('submission/'+str(obj.id))
	return render(request, "index/index.html", context)


def view_submission(request, id):
	obj = mailerSubmission.objects.filter(id = id)
	if obj.first():
		obj = obj.first()
		print(obj.number)
		context = {
			"desc" : obj
		}
		return render(request, "submission/view_submission.html", context)
	else:
		return redirect('/')