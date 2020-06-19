from django.shortcuts import render
from django.http import HttpResponse
from apps.message.models import Post
# Create your views here.
def search(request,loginuser):
    result=[]
    if request.method == 'POST':
        content = request.POST.get('content')
        if len(content)>0:
            results = Post.objects.filter(title__contains=content)
            for i in results:
                result.append(i.id)
    context={'result': result,'user':loginuser}
    return render(request, 'index.html', context)