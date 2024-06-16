from django.db.models import Q
from django.shortcuts import render,HttpResponse

from .models import Customer, Admin, Book, FeedBack


def indexfunction(request):
    return render(request,"index.html")
def loginfunction(request):
    return render(request,"login.html")
def registerfunction(request):
    return render(request,"register.html")
def pacakgesfunction(request):
    return render(request,"pacakges.html")
def bookfunction(request):
    return render(request, "book.html")
def servicesfunction(request):
    return render(request, "services.html")
def contactusfunction(request):
    if request.method=="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        feedback = request.POST["feedback"]
        print(f"the name is {name},email:{email},feedback:{feedback}")
        obj=FeedBack(name=name,email=email,feedback=feedback)
        obj.save()

        return render(request,"contactus.html",{"msg":"response submitted"})


    return render(request, "contactus.html")
def userlogout(request):
    return render(request,"login.html");

def customerregister(request):
    name=request.POST["name"]
    email = request.POST["emailid"]
    username = request.POST["username"]
    password=request.POST["password"]
    contact = request.POST["contactno"]
    location = request.POST["location"]
    customerobj = Customer(name=name,emailid=email,username=username,password=password,contact=contact,location=location)
    Customer.save(customerobj)
    print(customerobj)

    msg='Customer registered successfully'
    return render(request, "register.html", {"msg": msg})

def customerbook(request):
    name=request.POST["name"]
    email=request.POST["email"]
    phone=request.POST["phone"]
    adult=request.POST["adult"]
    child=request.POST["child"]
    checkin=request.POST["checkin"]
    checkout=request.POST["checkout"]
    customerobj1=Book(name=name,email=email,phone=phone,adult=adult,child=child,checkin=checkin,checkout=checkout)
    Book.save(customerobj1)
    print(customerobj1)

    msg="Booking successfull"
    return render(request,"book.html",{"msg":msg})


def checkcustlogin(request):
    email= request.POST["emailid"]
    password= request.POST["password"]

    flag = Customer.objects.filter(Q(emailid=email) & Q(password=password))

    print(flag)

    if flag:
        cust = Customer.objects.get(emailid=email)
        print(cust)
        print(cust.id,cust.name)
        request.session["cid"] = cust.id
        request.session["cname"] = cust.name
        return render(request, "customer.html", {"cid": cust.id, "cname": cust.name})

    else:
        msg = "Login Failed"
        print(msg)
        return render(request, "login.html", {"msg":msg})

def changepassword(request):
    cid=request.session["cid"]
    cname=request.session["cname"]

    return render(request,"changepwd.html",{"cid":cid,"cname":cname})


def empupdatepwd(request):
    cid=request.session["cid"]
    cname=request.session["cname"]

    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]

    flag = Customer.objects.filter(Q(id=cid) & Q(password=opwd))

    if flag:
        Customer.objects.filter(id=cid).update(password=npwd)
        msg = "Password Updated Successfully"
        return render(request, "changepwd.html", {"cid": cid, "cname": cname,"msg":msg})
    else:
        msg = "Old Password is Incorrect"
        return render(request, "changepwd.html", {"cid": cid, "cname": cname,"msg":msg})

def AdminPage(request):
    return render(request,"AdminPage.html")
def adminlogin(request):
    return render(request,"adminlogin.html")
def checkadminlogin(request):
    uname = request.POST["ausername"]
    pwd = request.POST["apassword"]

    flag = Admin.objects.filter(Q(username__exact=uname) & Q(password__exact=pwd))
    print(flag)

    if flag:
        admin = Admin.objects.get(username=uname)
        print(admin)
        request.session["auname"] = admin.username
        return render(request, "adminhome.html", {"auname": admin.username})
    else:
        msg = "Login Failed"
        return render(request, "adminlogin.html", {"msg": msg})
def adminhome(request):
    auname=request.session["auname"]
    return render(request,"adminhome.html",{"auname":auname})
def adminlogout(request):
    return render(request,"adminlogin.html")
def viewcustomers(request):
    auname=request.session["auname"]
    customerlist = Customer.objects.all()
    count = Customer.objects.count()
    return render(request,"viewcustomers.html",{"auname":auname,"customerlist":customerlist,"count":count})

