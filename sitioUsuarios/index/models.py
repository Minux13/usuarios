from __future__ import unicode_literals
#from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

import exifread
from PIL import Image
#from aroba.settings import MEDIA_ROOT


class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    """lastname = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    time_register = models.DateTimeField(auto_now_add=True, auto_now=False)
    time_actualization = models.DateTimeField(auto_now_add=False, auto_now=True)"""

    def __unicode__(self): #Python 3 __str__
        return self.user



class File(models.Model):

	class Meta:
        	verbose_name = ("Documento")
        	verbose_name_plural = ("Documentos")

	#proyecto = models.ForeignKey(Proyecto, related_name='proyecto')
	#image = models.ImageField(null=False, blank=False, upload_to='images/', default='')
	user = models.OneToOneField(User, null=False, blank=False)
	pdf = models.FileField(null=False, blank=False, upload_to='pdfs/', default='')
	#file_path = ""

	"""@staticmethod
	def _get_dict_exif(url):
		# Abre la imagen grabada y le cambia el tamanio
		image = Image.open(url)
		if 'exif' in image.info:
			exif = image.info['exif']
			print exif
		else:
			exif = ""
		return exif

	def savePdf(self, file_path, **kwargs):
		# Graba la imagen al llegar
		super(File, self).save()

		if not self.pdf.path.endswith(('.pdf', '.PDF')):
			return 0

		if not self.pdf:
			return 0

		path = file_path
		image = Image.open(path)
		folder = MEDIA_ROOT + '/images/'
		exif = self._get_dict_exif(path)

		if image.size[0] < 2550:
			# (width, height) = imagen.size
			size = (2550, 3507)
			image = image.resize(size, Image.ANTIALIAS)
		image.save(self.image.path, exif=exif)
		super(Imagen, self).save()
		"""

	#def saveImage(self, file_path, **kwargs):
		# Graba la imagen al llegar
	#	super(File, self).save()

	#	if not self.image.path.endswith(('.png', '.jpg', '.jpeg', '.JPG', '.JPEG', '.PNG')):
	#		return 0

	#	if not self.image:
	#		return 0







"""class Usuarios_registrado(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    time_register = models.DateTimeField(auto_now_add=True, auto_now=False)
    time_actualization = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self): #Python 3 __str__
        return self.nombre

class Userprofile(models.Model):
    user = models.Forenkey(User, on_delete=models.CASCADE)
    documents = models.Field(upload_tp= documentos/)

    def __unicode__(self): #Python 3 __str__
        return self.user

"""
