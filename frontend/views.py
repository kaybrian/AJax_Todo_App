from django.shortcuts import render


def List(request):
    context = {}
    return render(request,'frontend/index.html',context)