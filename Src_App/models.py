from django.db import models



class Brother(models.Model):

    name = models.CharField(max_length=100, verbose_name="Brother's Name")
    age = models.FloatField(null=True, verbose_name="Brother's Age (optional)")
    about = models.TextField(verbose_name='About Brother (optional)', null=True)
    img = models.ImageField(verbose_name="Brother's Image", null=False, upload_to='brothers')

    def __str__(self):

        return self.name 


class Art_Work(models.Model):   

    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='arts', default='', blank=False)

    def __str__(self):

        return self.title


class Layout(models.Model):

    title = models.CharField(max_length=2000, default='Design and Layout')
    header_img = models.ImageField(upload_to='layout', null=False, verbose_name='Header Image')
    gardens_img = models.ImageField(upload_to='layout', null=False, verbose_name='Gardens Link Image')
    artwork_img = models.ImageField(upload_to='layout', null=False, verbose_name='Artwork Link Image')
    brothers_img = models.ImageField(upload_to='layout', null=False, verbose_name='Brothers Link Image')
    retreat_center_img = models.ImageField(upload_to='layout', null=False, verbose_name='Retreat Center Link Image')
    lady_heading = models.CharField(max_length=100, verbose_name='Lady of Mepkin Page Heading')
    lady_img = models.ImageField(upload_to='layout', null=False, verbose_name='Lady of Mepkin Image')
    lady_text = models.TextField(verbose_name='About Lady of Mepkin')
    cemetry_heading = models.CharField(max_length=100, verbose_name="Lauren's Cemetry Heading")
    cemetry_img = models.ImageField(upload_to='layout', null=False, verbose_name="Lauren's Cemetry Image")
    cemetry_text = models.TextField(verbose_name="About Lauren's Cemetry")

    

# Psalm91@123