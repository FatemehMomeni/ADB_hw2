from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from .serializer import SingUpSerializer, RegisteredUsersSerializer
from .models import Users


edit_user_with_family = ''

def post_SignUp(request):
    if request.method == 'POST':
        instance = Users()
        instance.name = request.POST['name']
        instance.family = request.POST['family']
        instance.birth_date = request.POST['birth_date']
        instance.tel = request.POST['tel']
        instance.address = request.POST['address']
        instance.gender = request.POST['gender']

        instance.save()
        return render(request, 'signup.html', {'context': 'اطلاعات کاربر با موفقیت ثبت شد'})


def get_RegisteredUsers(request):
    if request.method == 'GET':
        query = Users.objects.filter()
        names = query.values_list('name')
        families = query.values_list('family')
        return render(request, 'register.html', {'names': names, 'families': families})


def post_EditUser(request):
    if request.method == 'POST':
        family = request.POST['family']
        global edit_user_with_family
        edit_user_with_family = family
        return render(request, 'update.html')


def update(request):
    query = Users.objects.filter(family=edit_user_with_family)

    name = request.POST['name']
    birth_date = request.POST['birth_date']
    tel = request.POST['tel']
    address = request.POST['address']
    gender = request.POST['gender']

    if query:
        if name:
            query.update(name=name)
        if birth_date:
            query.update(birth_date=birth_date)
        if tel:
            query.update(tel=tel)
        if address:
            query.update(address=address)
        if gender:
            query.update(gender=gender)
        return render(request, 'edit.html', {'context': 'اطلاعات با موفقیت ویرایش شد'})
    else:
        return render(request, 'edit.html', {'context': 'کاربر مورد نظر یافت نشد'})


def post_UserInfo(request):
    if request.method == 'POST':
        family = request.POST['family']

        query = Users.objects.filter(family=family)
        if query:
            name = query.values_list('name')
            birth_date = query.values_list('birth_date')
            tel = query.values_list('tel')
            address = query.values_list('address')
            gender = query.values_list('gender')
            return render(request, 'info.html', {'name': name, 'family': family, 'birth_date': birth_date,
                                                 'tel': tel, 'address': address, 'gender': gender})
        else:
            return HttpResponse("کاربر مورد نظر یافت نشد")


def index(request):
    return render(request, 'index.html')


def sign(request):
    return render(request, 'signup.html')


"""def regist(request):
    return render(request, 'register.html')"""


def information(request):
    return render(request, 'info.html')


def edition(request):
    return render(request, 'edit.html')

