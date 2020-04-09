from django.db import models

# Create your models here.


import random,os


def get_filename_ext(filepath):
	base_name=os.path.basename(filepath)
	name ,ext=os.path.splitext(base_name)
	return name ,ext

def upload_image_path(instance,filename):
	new_filename=random.randint(1,13516546431654)
	name ,ext=get_filename_ext(filename)
	final_filename='{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
	return "local/b2b/logo/{final_filename}".format(
		new_filename=new_filename,
		final_filename=final_filename
		)

class mailerSubmission(models.Model):
	name = models.CharField(max_length = 255, null = True, blank=True)
	email = models.EmailField(null = True, blank=True)
	number = models.CharField(max_length= 255, null = True, blank=True)
	template = models.FileField(upload_to = upload_image_path, null = True, blank = True)


	def __str__(self):
		return self.name
