from django.shortcuts import render
from exampleapp.models import Notification


def index(request):
	context = {
		"notifications": Notification.objects.order_by("-id")[:10]
	}

	if "HX-Request" in request.headers:
		return render(request, 'django_htmx_live_trigger_example/index.html#notifications', context)

	return render(request, 'django_htmx_live_trigger_example/index.html', context)