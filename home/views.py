from django.contrib.auth.decorators import login_required, login_not_required
from django.contrib.auth.models import User, Group, Permission
from django.shortcuts import render, redirect
from django.contrib.auth import  login as d_login, authenticate, logout as d_logout

# Create your views here.
@login_required
def index(request):

    grupo_admin_existe = Group.objects.filter(name='admin').exists()
    grupo_comprador_existe = Group.objects.filter(name='comprador').exists()
    grupo_consulta_existe = Group.objects.filter(name='consultor').exists()

    if not grupo_admin_existe:
        Group.objects.create(name='admin')

    if not grupo_admin_existe:
        Group.objects.create(name='comprador')

    if not grupo_admin_existe:
        Group.objects.create(name='consultor')

    if not Permission.objects.filter(codename__contains='CAN_ALL').exists():

        _per = Permission.objects.create(codename='CAN_ALL', name='Pode tudo', content_type_id=1)
        _per.save()

        permission = Permission.objects.get(codename__contains='CAN_ALL')

        if permission is not None:
            Group.objects.get(name='admin').permissions.add(permission)

    return render(request,'index.html')

@login_not_required
def login(request):

    credencias = {
        'username': ''
    }

    if not User.objects.filter(username='daniel').exists():
        user = User.objects.create_user(username='daniel', email='', password='12346')
        user.role = 'admin'
        user.groups.add(Group.objects.get(name='admin'))
        user.save()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        credencias['username'] = username

        if user is not None:
            d_login(request, user)
            group_user = user.groups.first()
            return redirect('home')

    return render(request,'login.html',context=credencias)

@login_not_required
def logout(request):
    d_logout(request)
    return redirect('login')