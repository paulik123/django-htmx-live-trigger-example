from django.core.management.base import BaseCommand, CommandError
from exampleapp.models import Notification
from django_htmx_live_trigger import trigger


class Command(BaseCommand):
	def add_arguments(self, parser):
		parser.add_argument("description")

	def handle(self, *args, **options):
		notification = Notification(description=options['description'])
		notification.save()

		trigger("all", "new-notification")