from django.http import HttpResponse


def sad(request, name):
	return HttpResponse(f'Nobody likes you, {name}!')


def happy(request, name, times):
	response = '<br>'.join(times * [f'You are great, {name} :)'])
	return HttpResponse(response)
