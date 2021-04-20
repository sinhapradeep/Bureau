from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .models import Coach, Teacher, Contact, Computer, Prof
#from django.contrib.auth.forms import UserCreationForm
from .form import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
#from .PayTm import Checksum
MERCHANT_KEY = '       '




context = {
             'std': 0,
             'Pay': 0,
             'cor': 0,
             'com': 0,
             'sub': 0,
    }
cours1 = 0
cours2 = 0


def index(request):

   # context['Pay'] = 29

    return render(request, 'index.html')
   #, context)


def ul(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "login successfully!!")
                    return HttpResponseRedirect('/user_profile/')
            else:
                messages.error(request, "Invalid Login")
                return redirect('/ul')
        else:
            fm = AuthenticationForm()
            return render(request, 'ul.html', {'form': fm})
    else:
        return HttpResponseRedirect('/user_profile/')



def user_profile(request):

    if request.user.is_authenticated:
        if request.method == 'POST':
            #sname = request.POST["sname"]
            sname = request.user.first_name
            amoun = context['Pay']
            cours1 = context['sub']
            cours2 = context['com']
            print(cours1)
            print(cours2)
            po = Prof(sname=sname, amoun=amoun, cours1=cours1, cours2=cours2)
            po.save()
            print("record saved")
            cours1 = cours2 = ''
            print(cours1, cours2)
            messages.success(request, "message has been sent")
            return redirect("/user_profile/")

        else:
            print("not Filled up")

            return render(request, 'profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/ul/')



def user_logout(request):
    logout(request)
    messages.success(request, "You are logged out")
    return redirect('/')



def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        #fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Account  has been created successfully!!")
    else:
        fm = SignUpForm()
        #fm = UserCreationForm()
    return render(request, 'sign_up.html', {'form': fm})



def about(request):
    return render(request, 'about.html')

def Gall(request):
    return render(request, 'gallery.html')

def career(request):
    return render(request, 'career.html')


def cont(request):
    print("Form submitted")
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        Details = request.POST["Details"]
        con = Contact(name=name, email=email, phone=phone, Details = Details)
        con.save()
        print("record saved")
        messages.success(request, "message has been sent")
        return redirect('/cont')

    else:
        print("not Filled")

        return render(request, 'contact.html')




def coach(request):
    print("Form submitted")

    if request.method == 'POST':
        subject = request.POST["subject"]
        course = request.POST["course"]
        stand = request.POST["stand"]
        co = Coach(subject=subject, course=course, stand=stand)
        co.save()
        messages.success(request, "This is our offering Fee")

        if stand == '6' or stand == '7' or stand == '8':
            if course == "Monthly":
                context['Pay'] = 780
            elif course == "Term":
                context['Pay'] = 4290
            elif course == "Yearly":
                context['Pay'] = 8580
        elif stand == '9' or stand == '10':
            if course == "Monthly":
                context['Pay'] = 880
            elif course == "Term":
                context['Pay'] = 4840
            elif course == "Yearly":
                context['Pay'] = 9680
        elif stand == '11' or stand == '12':
            if course == "Monthly":
                context['Pay'] = 1000
            elif course == "Term":
                context['Pay'] = 5500
            elif course == "Yearly":
                context['Pay'] = 11000


        context['std'] = stand
        context['cor'] = course
        context['sub'] = subject

        print("record saved")
        print(context['Pay'])
        return redirect('/coach')
    else:
        print("not Filled")
        print(context['Pay'])
        print(context['cor'])
        return render(request, 'cbse.html', context)

def coachi(request):
    print("Form submitted")

    if request.method == 'POST':
        subject = request.POST["subject"]
        course = request.POST["course"]
        stand = request.POST["stand"]
        co = Coach(subject=subject, course=course, stand=stand)
        co.save()
        messages.success(request, "This is our offering Fee")
        if stand == '6' or stand == '7' or stand == '8':
            if course == "Monthly":
                context['Pay'] = 780
            elif course == "Term":
                context['Pay'] = 4290
            elif course == "Yearly":
                context['Pay'] = 8580
        elif stand == '9' or stand == '10':
            if course == "Monthly":
                context['Pay'] = 880
            elif course == "Term":
                context['Pay'] = 4840
            elif course == "Yearly":
                context['Pay'] = 9680
        elif stand == '11' or stand == '12':
            if course == "Monthly":
                context['Pay'] = 1000
            elif course == "Term":
                context['Pay'] = 5500
            elif course == "Yearly":
                context['Pay'] = 11000
        context['cor'] =course
        context['std'] = stand
        context['sub'] = subject
        print("record saved")
        print(context['Pay'])
        return redirect('/coachi')
    else:
        print("not Filled")
        print(context['Pay'])
        print(context['cor'])
        return render(request, 'Icse.html', context)

def computer(request):
    print("Form submitted")
    coursec = 'yyy'
    if request.method == 'POST':
        coursec = request.POST["coursec"]
        cp = Computer(coursec=coursec)
        cp.save()
        messages.success(request, "This is our offering Fee")

        if coursec == "C++":
            context['Pay'] = 1999
        elif coursec == "Java":
            context['Pay'] = 2999
        elif coursec == "Python":
            context['Pay'] = 5999

        context['com'] = coursec
        print("record saved")
        print(coursec)
        print(context['Pay'])
        return redirect('/computer')
    else:
        print("not Filled com")
    print(context['Pay'])
    print(context['com'])
    return render(request, 'computer.html', context)



def teach(request):
    print("Form submitted")

    if request.method == 'POST':
        name = request.POST["name"]
        qual = request.POST["qual"]
        exp = request.POST["exp"]
        mob = request.POST["mob"]
        email = request.POST["email"]
        stand = request.POST["stand"]
        subject = request.POST["subject"]
        board = request.POST["board"]
        locat = request.POST["locat"]

        to = Teacher(name=name, qual=qual, exp=exp, mob=mob, email=email, stand=stand, subject=subject, board=board, locat=locat)
        to.save()
        print("record saved")
        messages.success(request, "message has been sent")
        return redirect('/teach')

    else:
        print("not Filled")

        return render(request, 'teacher.html')

def mat(request):
    return render(request, 'material.html')



def handlerequest(request):
    form = request.POST
    response_dict = { }
    for i in form.keys():
     #   response.dict[i]= form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    #if verify:
     #  if response_dict['RESCODE'] = '01':
     #       print("Order successful !!")
     #   else:
      #      print("order was not successful because response_dict['RESPMSG'])
      #            use of response.cgi
    #return render(request,'bureau/paymentstatus.html'{'response':'response_dict'})
    return HttpResponse('Done')
    pass


def log(request):
    print("form submitted")

    if request.method == 'POST':
        print("posted")
        username1 = request.POST["username"]
        password1 = request.POST["password"]
        User = auth.authenticate(username=username1, password=password1)
        if User is not None:
            auth.login(request, User)
            messages.success(request, "You logged in")
            return redirect('/')
        else:

            return redirect('/log')
    else:
        messages.success(request, "Invalid logged in")
        return render(request, 'index.html')


#def logout(request):
    #print("form submitted")
    #auth.logout(request)
   # messages.success(request, "You are logged out")
    #return redirect('/')

def userlogin(request):
   if not request.user.is_authenticated:
         if request.method == 'POST':
                fm = AuthenticationForm(request=request, data=request.Post)
                if fm.is_valid():
                  uname = fm.cleaned_data['username']
                  upass = fm.cleaned_data['password']
                  user = authenticate(username=uname, password=upass)
                  if user is not None:
                    login(request, user)
                    messages(request, "login successfully!!")
                    return HttpResponseRedirect('/profile/')
         else:
            fm = AuthenticationForm()
            return render(request, 'userlogin.html', {'form': fm})
   else:
     return HttpResponseRedirect('/profile/')

def coachP(request):
    print("Form submitted")

    if request.method == 'POST':
        subject = request.POST["subject"]
        course = request.POST["course"]
        stand = request.POST["stand"]
        co = Coach(subject=subject, course=course, stand=stand)
        co.save()
        messages.success(request, "message has been sent")
        if stand == '6' or stand == '7' or stand == '8':
            if course == "Monthly":
                context['Pay'] = 780
            elif course == "Term":
                context['Pay'] = 4290
            elif course == "Yearly":
                context['Pay'] = 8580
        elif stand == '9' or stand == '10':
            if course == "Monthly":
                context['Pay'] = 880
            elif course == "Term":
                context['Pay'] = 4840
            elif course == "Yearly":
                context['Pay'] = 9680
        elif stand == '11' or stand == '12':
            if course == "Monthly":
                context['Pay'] = 1000
            elif course == "Term":
                context['Pay'] = 5500
            elif course == "Yearly":
                context['Pay'] = 11000

        print("record saved")
        print(context['Pay'])
        return redirect('/coach')
    else:
        print("not Filled")
        print(context['Pay'])
        #param_dict = {

            #data_dict = {
           # 'MID_ID':'',
          #  'ORDER_ID': str(order.order_id),
          #  'TXN_AMOUNT': str(amount),
          #  'CUST_ID': email,
           # 'INDUSTRY_TYPE_ID':'Retail',
          # 'WEBSITE':'WEBSTAGING',
          #  'CHANNEL_ID':'WEB',
          #  'CALLBACK_URL':'http://127.0.0.1:8000/bureau/coach/handlerequest/',
       # }
       # param_dict['CHECKSUMHASH']= Checksum.generate_checksum(param_dict,MERCHANT_ID)
      #  return render(request,'bureau/payTm.html', {'paran_dict':param_dict})}
        return render(request, 'cbse.html', context)


def sign(request):
    print("form submitted")
    if request.method == 'POST':
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        sg = User.objects.create_user(username=username, first_name=first_name,
                                      last_name=last_name, email=email, password=password)
        sg.save()
        print("user created")
        messages.success(request, "User has been created")
        return redirect('/sign')
    else:
        print("not Filled")
        return render(request, 'signup.html')