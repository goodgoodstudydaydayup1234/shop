from django.shortcuts import render
from django.http import HttpResponse
from .models import Cpu, Gq


def index(request):
    # return HttpResponse('首页')
    return render(request, 'shop1/index.html', {'username': 'xcy'})


def list(request):
    cpulist = Cpu.objects.all()
    return render(request, 'shop1/list.html', {'cpulist': cpulist})
    # return HttpResponse('列表页')


def detail(request, id):
    cpu = Cpu.objects.get(pk=id)
    return render(request, 'shop1/detail.html', {'cpu': cpu})
    # return HttpResponse('详情页'+str(id))
