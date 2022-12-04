from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from.models import reg,complaint,request1
from Admin.models import Login
# Create your views here.
def citizenhome(request):
    template = loader.get_template("CitizenHome.html")
    context = {}

    return HttpResponse(template.render(context, request))
def citizenreg(request):
    if request.method=="POST":
        r=reg()
        r.name=request.POST.get("name")
        r.age=request.POST.get("age")
        r.gender=request.POST.get("gen")
        r.hname=request.POST.get("hname")
        r.location=request.POST.get("location")
        r.photo=request.FILES["photo"]
        r.pin=request.POST.get("pin")
        r.lmark=request.POST.get("lmark")
        r.cno=request.POST.get("cno")
        r.email=request.POST.get("email")
        r.uname=request.POST.get("uname")
        r.status='pending'
        r.save()
        l=Login()
        l.uname=request.POST.get("uname")
        l.pwd=request.POST.get("cno")
        l.utype='citizen'
        l.save()
        return HttpResponse("<script>alert('registration completed successfully');window.location='/citizenreg';</script>")
    else:
        template = loader.get_template("citizenreg.html")
        context = {}
        return HttpResponse(template.render(context, request))

def complaints(request):
    if request.method=="POST":
        c=complaint()
        c.complaint=request.POST.get("complaint")
        c.desc=request.POST.get("details")
        c.date=request.POST.get("date")
        c.status='pending'
        uname=request.session["uname"]
        rid=reg.objects.get(uname=uname)
        c.cid=rid.id
        c.save()
        return HttpResponse("<script>alert('complaint added successfully');window.location='/complaints';</script>")

    else:
        template = loader.get_template("addcomplaint.html")
        context = {}
        return HttpResponse(template.render(context, request))
def viewcstatus(request):
    uname=request.session["uname"]
    cid=reg.objects.get(uname=uname)
    c=complaint.objects.filter(cid=cid.id)
    template = loader.get_template("viewcomplaintstatus.html")
    context = {'k':c}
    return HttpResponse(template.render(context, request))
def requests(request):
    if request.method=="POST":
        r=request1()
        uname = request.session["uname"]
        cid = reg.objects.get(uname=uname)
        r.cid=cid.id
        r.date=request.POST.get("date")
        r.rtype=request.POST.get("rtype")
        r.details=request.POST.get("details")
        r.status='pending'
        r.save()
        return HttpResponse("<script>alert('request added successfully');window.location='/request';</script>")

    else:
        template = loader.get_template("addrequest.html")
        context = {}
        return HttpResponse(template.render(context, request))
def viewrstatus(request):
    uname=request.session["uname"]
    cid=reg.objects.get(uname=uname)
    c=request1.objects.filter(cid=cid.id)
    template = loader.get_template("viewrequeststatus.html")
    context = {'k':c}
    return HttpResponse(template.render(context, request))