from django.shortcuts import render, redirect
from .models import Member,History,Manage
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string

# Create your views here.

def home(request):
    return render(request,'home/index.html')

def about(request):
    return render(request,'home/about.html')

def event(request):
    return render(request,'home/event.html')

def faq(request):
    return render(request,'home/faq.html')

def contact(request):
    return render(request,'home/contact.html')

def signup(request):
    if request.method=='POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        pword = request.POST['password']
        country = request.POST['country']
        phone = request.POST['phone']

        request.session['email'] = email

        user = Member(fname=fname, lname=lname, email=email, pword=pword, country=country
                      , phone=phone)
        user.save()




        # htm_msg = render_to_string('mail/welcome.html', {} , request)
        # send_mail(
        #     subject='SURECOIN LTD WELCOME YOU',
        #     message='',
        #     from_email='support@surecoin.uk',
        #     recipient_list=[ request.session['email'] ],
        #     html_message=htm_msg,
        #     fail_silently=False
        # )

        try:
            user = Member.objects.get(email=request.session['email'])
            request.session['user']=user.email
            return redirect('/account/')

        except ObjectDoesNotExist:
            cont = {'error': "SIGNUP FAILED PLEASE USE VALID DETAILS AND TRY AGAIN"}
            return render(request, 'auth/signup.html', cont)


    return render(request,'auth/signup.html')

def login(request):
    if request.method=='POST':
        user= request.POST['email']
        try:
            l_user= Member.objects.get(email=user)
            if request.POST['password'] == l_user.pword:
                request.session['user']=user
                return redirect('/account/')
            else:
                cont = {'error': 'user not found or password is incorrect'}
                return render(request, 'auth/login.html', cont)

        except ObjectDoesNotExist:
            cont= {'error':'user not found or password is incorrect'}
            return render(request, 'auth/login.html', cont)

    return render(request, 'auth/login.html')

def account(request):
    if request.session['user']:
        sites = Manage.objects.get(site='site')
        user = Member.objects.get(email=request.session['user'])
        His = History.objects.filter(email=request.session['user'])

        if user.id_type and user.id_front :
            status ='VERIFIED'
        else:
            status = 'ACCOUNT NOT VERIFIED'

        cont={'user':user, "his":His, 'status':status,'site':sites}
        return render(request, 'user/account.html', cont)

def admin(request):
    if request.session['user']:
        user = Member.objects.get(email=request.session['user'])
        site = Manage.objects.get(site='site')

        if user.code == site.admin:
            mem = Member.objects.all().order_by('fname')
            cont = {'user': user, 'Mem': mem}

            if request.GET.get('rem'):
                rem = request.GET.get('rem')
                user = Member.objects.get(email=rem)
                user.delete()
            return render(request, 'admin/admin.html', cont)

def edit(request):
    if request.session['user']:
        user = Member.objects.get(email=request.session['user'])
        site = Manage.objects.get(site='site')

        if user.code == site.admin:
            if 'bal' in request.POST:
                mem = request.GET.get('mem')
                mems = Member.objects.get(email=mem)
                int_pro =mem.profit

                mems.invest = request.POST['bal']
                mems.profit = request.POST['prof']
                mems.bonus = request.POST['ref_B']
                mems.bal = request.POST['promo']
                mems.code = request.POST['code']
                mems.btc_equ = request.POST['btc']

                mems.save()

                if int_pro < mems.profit:
                    crd=mems.profit-int_pro
                    title = "ACCOUNT CREDITED"
                    msg = "your account has been credit from the current on going trade" + str(crd)
                    bal=mems.bal

                    msg_html = render_to_string('admin/mailing.html', {'title': title, 'msg': msg, 'bal':bal}, request)
                    # send_mail(
                    #     subject=title,
                    #     message='',
                    #     from_email='exocoins@exocoin.us',
                    #     recipient_list=[mems.email],
                    #     html_message=msg_html,
                    #     fail_silently=False,
                    # )


            if 'title' in request.POST:
                mem = request.GET.get('mem')
                mems = Member.objects.get(email=mem)

                mems.title = request.POST['title']
                mems.msg = request.POST['body']
                mems.save()

            if 'del_n' in request.POST:
                his = request.POST['del_n']
                His = History.objects.get(pk=his)
                His.delete()

            if 'edit_status' in request.POST:
                mem = request.GET.get('mem')
                mems = Member.objects.get(email=mem)
                his = History.objects.filter(email=mems.email).order_by('-date')
                cont = {'user': user, 'mem': mems, 'Refs': ref, 'His': his}
                return render(request, 'admin/history.html', cont)

            if 'status' in request.POST:
                his = request.POST['status']
                His = History.objects.get(pk=his)
                His.status = request.POST['update']
                His.save()

            if 'email' in request.POST:
                mem = request.GET.get('mem')
                mems = Member.objects.get(email=mem)

                title = request.POST['email']
                msg = request.POST['msg']

                msg_html = render_to_string('admin/mailing.html', {'title': title, 'msg': msg}, request)
                # send_mail(
                #     subject=title,
                #     message='',
                #     from_email='exocoins@exocoin.us',
                #     recipient_list=[mems.email],
                #     html_message=msg_html,
                #     fail_silently=False,
                # )

            if request.GET.get('mem'):
                mem = request.GET.get('mem')
                mems = Member.objects.get(email=mem)
                his = History.objects.filter(email=mems.email).order_by('-date')
                cont = {'user': user, 'mem': mems,  'His': his}
                return render(request, 'admin/edit.html', cont)

def site(request):
    if request.session['user']:
        user = Member.objects.get(email=request.session['user'])

        site = Manage.objects.get(site='site')

        if user.code == site.admin:

            user = Member.objects.get(email=request.session['user'])
            site = Manage.objects.get(site='site')
            cont = {'site': site, 'user': user}

            if 'mail' in request.POST:
                site.mail = request.POST['mail']
                site.phone = request.POST['phone']
                site.add = request.POST['add']
                site.btc = request.POST['btc']
                site.admin = request.POST['code']

            return render(request, 'admin/site.html', cont)


    return render(request, 'user/account.html')


def profile(request):
    return render(request,'user/profile.html')

def verification(request):
    if request.session['user']:
        user = Member.objects.get(email=request.session['user'])
        if request.method =='POST':
            user.id_type = request.POST['id_type']
            user.id_front = request.FILES['id_front']
            user.id_back = request.FILES['id_back']
            user.save()
            return redirect('/account/')

        return render(request,'user/verification.html')

def upgrade(request):
    return render(request,'user/upgrade.html')

def fund(request):
    return render(request,'user/fund.html')