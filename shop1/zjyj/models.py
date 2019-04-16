from django.db import models


class Cpu(models.Model):
    cname = models.CharField(max_length=255, verbose_name='名字')
    cbrand = models.CharField(max_length=255, verbose_name='品牌')
    cseries = models.CharField(max_length=255, verbose_name='系列')
    ccore_num = models.CharField(max_length=255, verbose_name='核数')
    cmodel = models.CharField(max_length=255, verbose_name='型号')
    cprice = models.IntegerField(verbose_name='价格')
    # cimage = models.URLField(verbose_name='图片')

    def __str__(self):
        return self.cname


class Gq(models.Model):
    gname = models.CharField(max_length=255, verbose_name='名字')
    gbrand = models.CharField(max_length=255, verbose_name='品牌')
    gmodel = models.CharField(max_length=255, verbose_name='型号')
    gcolor = models.CharField(max_length=255, verbose_name='颜色')
    gcache = models.CharField(max_length=255, verbose_name='缓存')
    ginterface = models.CharField(max_length=255, verbose_name='接口')
    gtype = models.CharField(max_length=255, verbose_name='类型')
    gsize = models.CharField(max_length=255, verbose_name='尺寸')
    gprice = models.IntegerField(verbose_name='价格')
    # gimage = models.URLField(verbose_name='图片')

    def __str__(self):
        return self.gname

