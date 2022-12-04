from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Login,major,operation
from Citizen.models import reg,complaint,request1
# Create your views here.
def adminhome(request):
    template = loader.get_template("AdminHome.html")
    context = {}

    return HttpResponse(template.render(context, request))
def index(request):
    context={}
    template=loader.get_template("index.html")
    return HttpResponse(template.render(context,request))
def gallery(request):
    context={}
    template=loader.get_template("gallery.html")
    return HttpResponse(template.render(context,request))
def service(request):
    context={}
    template=loader.get_template("service.html")
    return HttpResponse(template.render(context,request))
def contact(request):
    context={}
    template=loader.get_template("contact.html")
    return HttpResponse(template.render(context,request))
def login(request):
    if request.method=="POST":
        uname = request.POST.get("text1")
        pwd = request.POST.get("password")
        if (Login.objects.filter(uname=uname, pwd=pwd)):
            l = Login.objects.filter(uname=uname,pwd=pwd)
            for i in l:
                utype = i.utype


            if (utype == "admin"):
                context = {}
                template = loader.get_template("AdminHome.html")
                return HttpResponse(template.render(context, request))
            elif(utype=="major"):
                request.session["uname"]=uname
                context = {}
                template = loader.get_template("MajorHome.html")
                return HttpResponse(template.render(context, request))
            elif (utype == "officer"):
                request.session["uname"] = uname
                context = {}
                template = loader.get_template("OfficerHome.html")
                return HttpResponse(template.render(context, request))
            elif (utype == "citizen"):
                c=reg.objects.get(uname=uname)
                if c.status=="pending":
                    return HttpResponse("<script>alert('Access Denied!!');window.location='/login';</script>")
                else:
                    request.session["uname"] = uname
                    context = {}
                    template = loader.get_template("CitizenHome.html")
                    return HttpResponse(template.render(context, request))



            else:
                return HttpResponse("<script>alert('Access Denied!!');window.location='/login';</script>")
        else:
            return HttpResponse("<script>alert('Invalid Username Or Password');window.location='/login';</script>")

    else:

        context={}
        template=loader.get_template("Login.html")
        return HttpResponse(template.render(context,request))
def addmajor(request):
    if request.method=="POST":
        m=major()
        m.mname=request.POST.get("name")
        m.gender=request.POST.get("gen")
        m.dob=request.POST.get("dob")
        m.bgrp=request.POST.get("bgrp")
        m.phone=request.POST.get("phone")
        m.photo=request.FILES["photo"]
        m.email=request.POST.get("email")
        m.force=request.POST.get("force")
        m.exp=request.POST.get("exp")
        m.uname=request.POST.get("uname")
        m.regno=request.POST.get("regno")
        m.pwd=request.POST.get("phone")
        m.save()
        l=Login()
        l.uname=request.POST.get("uname")
        l.pwd=request.POST.get("phone")
        l.utype='major'
        l.save()
        return HttpResponse("<script>alert('Major details added  Successfully');window.location='/major';</script>")


    else:
        context = {}
        template = loader.get_template("addmajor.html")
        return HttpResponse(template.render(context, request))
def operations(request):
    if request.method=="POST":
        o=operation()
        o.oname=request.POST.get("oname")
        o.details=request.POST.get("details")
        o.odate=request.POST.get("odate")
        o.rname=request.POST.get("rname")
        o.rtotal=request.POST.get("rtotal")
        o.gname=request.POST.get("gname")
        o.gtotal=request.POST.get("gtotal")
        o.cname=request.POST.get("cname")
        o.ctotal=request.POST.get("ctotal")
        o.lname=request.POST.get("lname")
        o.ltotal=request.POST.get("ltotal")
        o.save()
        return HttpResponse("<script>alert('Operation details added  Successfully');window.location='/operations';</script>")

    else:
        context = {}
        template = loader.get_template("addoperation.html")
        return HttpResponse(template.render(context, request))

def viewcitizen(request):

    c=reg.objects.filter(status='pending')
    context = {'k':c}
    template = loader.get_template("approvecitizen.html")
    return HttpResponse(template.render(context, request))
def approve(request,id):
    c=reg.objects.get(id=id)
    c.status='approve'
    c.save()
    return HttpResponse("<script>alert('Approved  Successfully');window.location='/viewcitizen';</script>")
def reject(request,id):
    c=reg.objects.get(id=id)
    c.status='reject'
    c.save()
    return HttpResponse("<script>alert('Rejected  Successfully');window.location='/viewcitizen';</script>")
def viewcomplaint(request):
    c = complaint.objects.raw("SELECT citizen_complaint.*,citizen_reg.name,citizen_reg.location,citizen_reg.lmark,citizen_reg.cno,citizen_reg.email from citizen_complaint,citizen_reg where citizen_complaint.cid=citizen_reg.id and citizen_complaint.status='pending'")

    context = {'k': c}
    template = loader.get_template("viewcomplaint.html")
    return HttpResponse(template.render(context, request))
def accept(request,id):
    c=complaint.objects.get(id=id)
    c.status='approve'
    c.save()
    return HttpResponse("<script>alert('Accepted  Successfully');window.location='/viewcomplaint';</script>")
def reject1(request,id):
    c=complaint.objects.get(id=id)
    c.status='reject'
    c.save()
    return HttpResponse("<script>alert('Rejected  Successfully');window.location='/viewcomplaint';</script>")
def viewrequest(request):
    c = complaint.objects.raw("SELECT citizen_request1.*,citizen_reg.name,citizen_reg.location,citizen_reg.lmark,citizen_reg.cno,citizen_reg.email from citizen_request1,citizen_reg where citizen_request1.cid=citizen_reg.id and citizen_request1.status='pending'")

    context = {'k': c}
    template = loader.get_template("viewrequest.html")
    return HttpResponse(template.render(context, request))
def acceptre(request,id):
    c=request1.objects.get(id=id)
    c.status='approve'
    c.save()
    return HttpResponse("<script>alert('Accepted  Successfully');window.location='/viewrequest';</script>")
def rejectre1(request,id):
    c=request1.objects.get(id=id)
    c.status='reject'
    c.save()
    return HttpResponse("<script>alert('Rejected  Successfully');window.location='/viewrequest';</script>")


