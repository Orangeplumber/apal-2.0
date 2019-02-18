from django.db import models

class Pack(models.Model):
	pack_name=models.CharField(max_length=20)
	pack_price=models.PositiveIntegerField(default=10)
	fruit_pic=models.ImageField(upload_to='offer/', verbose_name='Fruit Photo')
	stock=models.PositiveIntegerField(default=0)



# shell script to upload a file
# from django.core.files import File
# f = File(open(os.path.join(IMPORT_DIR, 'fotos', photo), 'r'))
# p = Photo(name=f.name, image=f, parent=supply.supply_ptr)
# name = str(uuid1()) + os.path.splitext(f.name)[1]
# p.image.save(name, f)
# p.save()