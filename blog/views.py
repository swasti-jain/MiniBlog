# from curses.ascii import HT
from weakref import ref
from django.shortcuts import render,HttpResponseRedirect
from numpy import full
# from django.contrib.auth.forms import UserCreationForm
from .forms import NewsForm, ScienceForm, SignUpForm,LoginForm,PostForm, TechnologyForm, ContactForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post,News,Science,Technology,ReferenceNo
from django.contrib.auth.models import Group
# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html',{'posts':posts})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            form.save()  #saving to the database
            # print(name) it's fine working
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html',{'form':form})

def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        news = News.objects.all()
        science = Science.objects.all()
        tech = Technology.objects.all()

        user = request.user 
        full_name = user.get_full_name()
        groups = user.groups.all()
        # for i in groups:
        #     print("Group ka nama",i.name)
        return render(request,'blog/dashboard.html',{'posts':posts,'news':news,'science':science,'tech':tech,'full_name':full_name,'groups':groups})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    # return render(request,'blog/.html')
    return HttpResponseRedirect('/')

def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            refNo = form.cleaned_data['ref_no']
            
            # allRefs = ReferenceNo.objects.all()
            # for ref in allRefs:
            #     i=ref.ref
            #     with open ("refNos.txt","a+") as f:
            #             f.write(i)
            #             f.write('\n')
            #         print('Exist krta hai')
            #     else:
            #         print('Nahi krta hai!')
            doesExist = ReferenceNo.objects.filter(ref = refNo).exists()
            # print(doesExist)
            if doesExist == True:
                todel = ReferenceNo.objects.get(ref = refNo)
                todel.delete()
                # print('This ref get removed!!')
                user = form.save()
                group = Group.objects.get(name = 'Author')
                user.groups.add(group)
                # messages.success(request,'Congratulations! You have become an Author')
            else:
                # print('Ye Reference Exist nahi krta hai')
                messages.error(request,'Invalid Reference Id!!')
            # user = form.save()
            # group = Group.objects.get(name = 'Author')
            # user.groups.add(group)
                
    else:    
        form = SignUpForm()
    return render(request,'blog/signup.html',{'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged In Successfully!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                category = form.cleaned_data['category']
                # print('category = ',category)
                if category == 'general':
                    pst = Post(title = title,desc = desc)
                    pst.save()
                    form = PostForm()
                elif category == 'news':
                    pst = News(title = title,desc = desc)
                    pst.save()
                    form = PostForm()
                elif category == 'technology':
                    pst = Technology(title = title,desc = desc)
                    pst.save()
                    form = PostForm()
                else: # category == 'science':
                    pst = Science(title = title,desc = desc)
                    pst.save()
                    form = PostForm()
        else:
            form = PostForm()
        return render(request,'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')


def refNos():
    import random
    import string 
    # random_st(500,4)
    lis = []
    for i in range(500):
        result = ''.join(random.choice(string.ascii_letters) for i in range(4))
        n = random.randint(0,999)
        result+=str(n)

        r2 = ''.join(random.choice(string.ascii_letters) for i in range(4))
        n = random.randint(0,90)
        r2 = r2 + str(n) + "-" +result
		
        lis.append(r2)
    for i in lis:
        re = ReferenceNo(ref = i)
        re.save()
    # print('REFERENCES GoT GENERATED!! ')

def update_post(request,id,type):
    if request.user.is_authenticated:
        if type == 'Post':  #general post for home page
            if request.method == 'POST':
                pi = Post.objects.get(pk=id)
                form = PostForm(request.POST,instance = pi)
                if form.is_valid():
                    form.save()
            else:
                pi = Post.objects.get(pk=id)
                form = PostForm(instance = pi)
            return render(request,'blog/updatepost.html',{'form':form})

        if type == 'News':
            if request.method == 'POST':
                pi = News.objects.get(pk=id)
                form = NewsForm(request.POST,instance = pi)
                if form.is_valid():
                    form.save()
            else:
                pi = News.objects.get(pk=id)
                form = NewsForm(instance = pi)
            return render(request,'blog/updatepost.html',{'form':form})

        if type == 'Sci':
            if request.method == 'POST':
                pi = Science.objects.get(pk=id)
                # print('Science Pi ',pi)
                form = ScienceForm(request.POST,instance = pi)
                if form.is_valid():
                    form.save()
            else:
                pi = Science.objects.get(pk=id)
                # form = ScienceForm(request.POST,instance = pi)
                form = ScienceForm(instance = pi)
            return render(request,'blog/updatepost.html',{'form':form})
        
        if type == 'Tech':
            if request.method == 'POST':
                pi = Technology.objects.get(pk=id)
                form = TechnologyForm(request.POST,instance = pi)
                if form.is_valid():
                    form.save()  
            else:
                pi = Technology.objects.get(pk = id)
                form = TechnologyForm(instance=pi)
            return render(request,'blog/updatepost.html',{'form':form})
        # else:
        #     pi = Post.objects.get(pk=id)
        #     form = PostForm(instance = pi)
        #     return render(request,'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')


def delete_post(request,id,type):
    if request.user.is_authenticated:
        # print("The type is ",type)
        if request.method == 'POST':
            if type == 'Post':
                pi = Post.objects.get(pk = id)
                pi.delete()
                return HttpResponseRedirect('/dashboard/')
            elif type == 'Tech':
                pi = Technology.objects.get(pk = id)
                pi.delete()
                return HttpResponseRedirect('/dashboard/')
            elif type == 'Sci':
                pi = Science.objects.get(pk = id)
                pi.delete()
                return HttpResponseRedirect('/dashboard/')
            else:
                pi = News.objects.get(pk = id)
                pi.delete()
                return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

def blogContents(request,id):
    if id == "news":
        posts = News.objects.all()
        return render(request,'blog/news.html',{'posts':posts})
    elif id == "tech":
        posts = Technology.objects.all()
        return render(request,'blog/tech.html',{'posts':posts})
    # elif id == "science":
    #     posts = Science.objects.all()
    #     return render(request,'blog/science.html',{'posts':posts})
    else:
        posts = Science.objects.all()
        return render(request,'blog/science.html',{'posts':posts})


def videosContent(request):
    return render(request,'blog/video_content.html')
    
