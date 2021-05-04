from django.shortcuts import render

# Create your views here.
def homeview(request):
    ctx ={'title':'welcome'}
    return render(request,'index.html',context= ctx)


