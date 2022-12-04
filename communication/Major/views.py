from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import officer,team,majortextmsg
from Admin.models import Login,operation,major
from Officer.models import officertextmsg
import base64
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from django.http import JsonResponse

# Create your views here.
def majorhome(request):
    template = loader.get_template("MajorHome.html")
    context = {}

    return HttpResponse(template.render(context, request))
def officers(request):
    if request.method=="POST":
        m=officer()
        m.name=request.POST.get("name")
        m.gender=request.POST.get("gen")
        m.dob=request.POST.get("dob")
        m.bgrp=request.POST.get("bgrp")
        m.phone=request.POST.get("phone")
        m.photo=request.FILES["photo"]
        m.email=request.POST.get("email")
        m.fname=request.POST.get("fname")
        m.exp=request.POST.get("exp")
        m.uname=request.POST.get("uname")
        m.regno=request.POST.get("regno")
        m.pwd=request.POST.get("phone")
        m.dname=request.POST.get("dname")
        m.save()
        l=Login()
        l.uname=request.POST.get("uname")
        l.pwd=request.POST.get("phone")
        l.utype='officer'
        l.save()
        return HttpResponse("<script>alert('Officer details added  Successfully');window.location='/officers';</script>")


    else:
        context = {}
        template = loader.get_template("addofficer.html")
        return HttpResponse(template.render(context, request))
def viewoperation(request):
    o=operation.objects.all()
    context = {'k':o}
    template = loader.get_template("viewoperation.html")
    return HttpResponse(template.render(context, request))
def teams(request):
    if request.method=="POST":
        t=team()
        uname=request.session["uname"]
        mid=major.objects.get(uname=uname)
        t.mid=mid.id
        t.oid=request.POST.get("oname")
        t.offid=request.POST.get("name")
        t.tcode=request.POST.get("tcode")
        t.save()
        return HttpResponse("<script>alert('team added  Successfully');window.location='/team';</script>")


    else:
        o=operation.objects.all()
        off=officer.objects.all()
        context = {'op':o,'off':off}
        template = loader.get_template("createteam.html")
        return HttpResponse(template.render(context, request))
def generate_keys():
    modulus_length = 1024

    key = RSA.generate(modulus_length)
    #print (key.exportKey())

    pub_key = key.publickey()
    #print (pub_key.exportKey())

    return key, pub_key
def encrypt_private_key(a_message, private_key):
    encryptor = PKCS1_OAEP.new(private_key)
    encrypted_msg = encryptor.encrypt(a_message)
    print(encrypted_msg)
    encoded_encrypted_msg = base64.b64encode(encrypted_msg)
    print(encoded_encrypted_msg)
    return encoded_encrypted_msg
def decrypt_public_key(encoded_encrypted_msg, public_key):
    encryptor = PKCS1_OAEP.new(public_key)
    decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
    print(decoded_encrypted_msg)
    decoded_decrypted_msg = encryptor.decrypt(decoded_encrypted_msg)
    print(decoded_decrypted_msg)
    return decoded_decrypted_msg

def staffmsg(request):
    if request.method=="POST":
        sname = request.POST.get("sname")
        sid=officer.objects.get(id=sname)
        msg = request.POST.get("msg")
        email = sid.email
        request.session["email"] = email
        request.session["toid"] = sid.id
        request.session["msg"] = msg
        private, public = generate_keys()
        message = bytes(msg.encode("utf8"))
        encoded = encrypt_private_key(message, public)
        decoded = decrypt_public_key(encoded, private)
        template = loader.get_template("encstaffmessage.html")
        context = {'enc': encoded, 'prkey': private, 'pbkey': public}
        return HttpResponse(template.render(context, request))
    else:
        s = officer.objects.all()
        context={'sname':s}
        template=loader.get_template("addofficertxtmsg.html")
        return HttpResponse(template.render(context,request))
def staffs(request):
    if (request.method == 'GET' and request.GET.get('q') != None):
        sid = request.GET.get('q')
        l = officer.objects.filter(id=sid).values()
        # users_list = list(framework)  # important: convert the QuerySet to a list object
        return JsonResponse(list(l), safe=False)
def encstaffmsg(request):
    if request.method=="POST":
        t=majortextmsg()
        t.msg=request.session["msg"]
        t.private=request.POST.get("prkey")
        t.public=request.POST.get("pbkey")
        t.encmsg=request.POST.get("encmsg")
        uname=request.session["uname"]
        mid=major.objects.get(uname=uname)
        t.mid=mid.id
        sid=request.session["toid"]
        s=officer.objects.get(id=sid)
        t.oid = s.id

        t.save()
        subject = 'You got an email from defence'
        message = 'plz login your a/c and read the message. your key value='+request.POST.get("prkey")
        email_from = settings.EMAIL_HOST_USER
        mailid = request.session["email"]
        recipient_list = [mailid, ]
        send_mail(subject, message, email_from, recipient_list)

        return HttpResponse("<script>alert('Message Send Successfully');window.location='/staffmsg';</script>")

    else:
        template = loader.get_template("encstaffmessage.html")
        context = {}
        return HttpResponse(template.render(context, request))
def viewofficermsg(request):
    uname=request.session["uname"]
    uid=major.objects.get(uname=uname)
    m=officertextmsg.objects.raw("SELECT officer_officertextmsg.*,major_officer.name from officer_officertextmsg,major_officer,admin_major where officer_officertextmsg.oid=major_officer.id and officer_officertextmsg.mid=admin_major.id and major_officer.id=%s",[uid.id])


    template = loader.get_template("viewofficermsg.html")
    context = {'k':m}
    return HttpResponse(template.render(context, request))
def viewofficermsg1(request,id):
    t = officertextmsg.objects.get(id=id)
    context = {'msg': t}
    template = loader.get_template("viewofficermsg1.html")
    return HttpResponse(template.render(context, request))
def staffmsgdecrypt1(request):
    id = request.POST.get("id")
    mid = officertextmsg.objects.get(id=id)
    msg = request.POST.get("encmsg")
    key = request.POST.get("prkey")
    m = officertextmsg.objects.filter(id=id)
    for i in m:
        if (i.private == key):
            m1 = i.msg
        else:
            return HttpResponse("<script>alert('Invalid key');window.location='/viewofficermsg1';</script>")

    # decoded = decrypt_public_key(bytes(msg.encode("utf8")),bytes(key.encode("utf8")))
    t = officertextmsg.objects.get(id=id)
    context = {'dec': m1, 'msg': t, 'key': key}
    template = loader.get_template("viewofficermsg1.html")
    return HttpResponse(template.render(context, request))
