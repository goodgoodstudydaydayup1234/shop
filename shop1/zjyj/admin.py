from django.contrib import admin
from .models import Cpu,Gq


class CpuAdmin(admin.ModelAdmin):
    list_display = ['cname', 'cbrand', 'cmodel', 'cseries', 'ccore_num', 'cprice']
    list_filter = ['cbrand', 'ccore_num']
    search_fields = ['cbrand', 'ccore_num']
    list_per_page = 3


admin.site.register(Cpu, CpuAdmin)


class GqAdmin(admin.ModelAdmin):
    list_display = ['gname', 'gbrand', 'gmodel', 'gcolor', 'gcache', 'ginterface', 'gtype', 'gsize', 'gprice']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 3


admin.site.register(Gq, GqAdmin)

