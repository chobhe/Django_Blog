from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import Blog, Blog_storage
from main.forms import CreateNewBlogStorage
import PIL
from django.contrib.auth.models import User


# Create your views here.
#place to handle various webpages

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user) #tells us who's using our website, charliehe if I'm using it or anonymous user when used in an incognito tab
    #return HttpResponse('<h1>Hello World</h1>')  #string of HTML code
    my_context = {
    'key': 'value',
    'word': 12345
    }

    return render(request,'home.html', my_context)

#define function then import views to work with urls
#urls in the website urls.py
def index(request, id):
    ls = Blog_storage.objects.get(id = id)
    x = ''
    #whenever we get a server post request it comes back with a dictionary with {name: value} for every input and button, request.POST is a dictionary
    if request.method == 'POST':
        print(request.POST)
        if request.user.is_anonymous == False:
            if request.POST.get('done?'):
                for blogz in ls.blog_set.all():
                    if request.POST.get('c'+str(blogz.id)):
                        blogz.read = True
                    else:
                        blogz.read = False
                    blogz.save()

            elif request.POST.get('New Article'):
                title = request.POST.get('title')
                author = request.POST.get('author')
                txt = request.POST.get('article')
                prev = request.POST.get('preview')
                img = request.FILES.get('img')
                print(img)
                #if we press the New Article Button we need to get the values from all the entries and fields to put into our object

                if len(title) > 2 and len(author) > 2 and len(txt) > 5 and len(prev) > 5 and img != '':

                    ls.blog_set.create(title = title, author = author, preview = prev, entry = txt, im = img)

                elif len(title) > 2 and len(author) > 2 and len(txt) > 5 and len(prev) > 5:
                    ls.blog_set.create(title = title, author = author, preview = prev, entry = txt)

                else:
                    print('invalid')
        else:
            x = 'to save changes into the database please login'


    return render(request, 'blog.html', {'ls':ls, 'x':x})


def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def create(request, *args, **kwargs):
    if request.method == 'POST':
        form = CreateNewBlogStorage(request.POST) #request.POST is a response that is going to contain a dictionary with all the Id's of all the attributes of our input

        if form.is_valid():
            title = form.cleaned_data['title']
            t = Blog_storage(title = title)
            t.save()
            request.user.blog_storage.add(t)

        return HttpResponseRedirect('/%i' %t.id)



    elif request.method == 'GET':
        form = CreateNewBlogStorage()
    return render(request, 'create.html', {'form':form})


def view(request):
    ls = Blog_storage.objects.all()
    return render(request, 'view_dividers.html',{'ls':ls})





def article(request, id):
    ls = Blog.objects.get(id = id)
    return render(request, 'article.html', {'ls': ls})
