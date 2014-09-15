from django.core.management.base import BaseCommand, CommandError
from apps.product.models import DiscountCode, Part
from apps.files.models import ProductList
from Myton_Django.populate import populate_product_by_files

class Command(BaseCommand):
	def handle(self, *args, **options):
		try:
			product = ProductList.objects.filter(synced=False).latest('created_on')
			# import pdb; pdb.set_trace() 
			f = open("static/media/"+str(product.file_upload))
			populate_product_by_files(f, product.supplier)
			product.synced = True
			product.save()
		except:
			pass

		