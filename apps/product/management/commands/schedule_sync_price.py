from django.core.management.base import BaseCommand, CommandError
from apps.product.models import DiscountCode, Part
from apps.files.models import ProductList
from Myton_Django.populate import populate_product_by_files
from django.conf import settings
import os

class Command(BaseCommand):
	def handle(self, *args, **options):
		try:
			productlist = ProductList.objects.filter(synced=False)[:1]
			for product in productlist:
				fullpath = os.path.join(settings.MEDIA_ROOT,str(product.file_upload))		
				f = open(fullpath)
				#import pdb; pdb.set_trace() 
				populate_product_by_files(f, product.supplier)
				product.synced = True
				product.save()
		except Exception as e:
			print '%s (%s)' % (e.message, type(e))
			pass

		