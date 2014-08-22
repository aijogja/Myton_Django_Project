from django.core.management.base import BaseCommand, CommandError
from apps.product.models import DiscountCode, Part

class Command(BaseCommand):
	def handle(self, *args, **options):
		part = Part.objects.filter(weight=None)
		for p in part:
			pa = Part.objects.get(pk=p.pk)
			pa.weight = 1
			pa.save()

			print pa.part_number + ' weight ' + str(pa.weight)