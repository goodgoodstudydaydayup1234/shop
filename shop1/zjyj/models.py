from django.db import models


class Cpu(models.Model):
    cname = models.CharField(max_length=255)
    cbrand = models.CharField(max_length=255)
    cseries = models.CharField(max_length=255)
    ccore_num = models.CharField(max_length=255)
    cmodel = models.CharField(max_length=255)
    cprice = models.IntegerField()
    # cimage = models.ImageField()

    def __str__(self):
        return self.cname


class Gq(models.Model):
    gname = models.CharField(max_length=255)
    gbrand = models.CharField(max_length=255)
    gmodel = models.CharField(max_length=255)
    gcolor = models.CharField(max_length=255)
    gcache = models.CharField(max_length=255)
    ginterface = models.CharField(max_length=255)
    gtype = models.CharField(max_length=255)
    gsize = models.CharField(max_length=255)
    gprice = models.IntegerField()

    def __str__(self):
        return self.gname

