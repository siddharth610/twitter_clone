from django.shortcuts import render

# Create your views here.
tweets = [{'name':'Siddharth', 'text':'This is my first tweet'},{'name':'Paras', 'text':'This is my Second tweet'}]





def home(request):
    context = {'tweets': tweets}
    return render(request,'feed/home.html',context)
