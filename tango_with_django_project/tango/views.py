from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from tango.models import Category,Page,UserProfile
from tango.forms import CategoryForm,PageForm,UserForm,UserProfileForm
from django.contrib.auth.models import  User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    categories = Category.objects.order_by('-likes')[:5]
    pages = Page.objects.order_by('-views')[:5]
    request.session.set_test_cookie()
    response = render(request, 'tango/index.html', context={'categories': categories, 'pages': pages})
    visitor_cookie_handler(request,response)
    return response

def about(request):
    if request.session.test_cookie_worked():
       request.session.delete_test_cookie()
       print('Test Cookie worked')

    return render(request,'tango/about.html')
def visitor_cookie_handler(request,response):
    #获取访问次数
    visits = int(request.COOKIES.get('visits','1'))
    str_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(type(str_time))
    last_visit_cookie = request.COOKIES.get('last_visit',str_time)
    last_visit_time = datetime.strptime(last_visit_cookie,'%Y-%m-%d %H:%M:%S')
    # if last_visit_time -  datetime.now()> 0:
    #     visits = visits +1
    #     response.set_cookie('last_visit',str_time)
    # else:
    #     visits = 1
    #     response.set_cookie('last_visit',last_visit_cookie)
    # response.set_cookie('visits',visits)
def show_category(request,category_id):
    try:
        category = Category.objects.get(id = category_id)
        pages = Page.objects.filter(category = category_id)
        category_dic = {}
        category_dic['category'] =  category
        category_dic['pages'] = pages
    except Category.DoesNotExist:
        category_dic['category'] = None
        category_dic['pages'] = None
    return render(request, 'tango/category.html', context=category_dic)
def show_page(request,page_id):
    print(page_id)
    try:
        page = Page.objects.get(id = page_id)
        page_dic = {}
        page_dic['page'] = page
        page.views = page.views + 1;
        page.save()
    except Page.DoesNotExist:
        page_dic['page'] = None
    return render(request, 'tango/page.html', context = page_dic)
@login_required
def add_category(request):
    form = CategoryForm()
    print('11111111111')
    print(form.is_valid())
    print(request.method)
    if request.method == 'POST':
        # print('errors----->begin')
        # print(form.errors)
        # print('errors----->end')
        form = CategoryForm(request.POST) #在验证表单之前赋值^-^
        if form.is_valid():

            #保存新的种类到数据库
            form.save(commit=True)
            #Category已保存
            #我们可以反馈给一个确认信息
            #index 页显示已添加的类别
            #我们可以引导用户到index页
            return index(request)
        else:
            #表单有错误
            #只在控制台打印

            print(form.errors)
            #return render(request, 'tango/add_category.html',{'form': form})
    else:
        return render(request,'tango/add_category.html',{'form': form})
@login_required #装饰器 作用 如果用户没有登陆会跳转到settings.py中LOGIN_URL设置的地址
def add_page(request):
    form = PageForm()
    if request.method == 'POST':
        print(request.body)
        form = PageForm(request.POST)
        print(form.data)
        if form.is_valid ():
            form.save()
            return index(request)
        else:
            print(form.errors)
    else:
        context_dic = {}
        context_dic['form'] = form
        context_dic['category'] = Category.objects.all()
        return render(request,'tango/add_page.html',context_dic)

def register(request):

    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data = request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            #save后保存到数据库的密码是明文
            user = user_form.save()
            #设置密文密码再次保存
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            #print('files --------')
            #print(request.FILES)

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            # Now we save the UserProfile model instance.
            profile.save()
            # Update our variable to indicate that the template
            # registration was successful.
            registered = True
            return index(request)
        else:
            print(user_form.errors)
            print(profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,'tango/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print('Invalid login details: {0}, {1}'.format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request,'tango/user_login.html',{})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
