from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Admin.models import Login,operation,major
from Major.models import  officer,team,majortextmsg
from.models import officertextmsg
import base64
from django.core.mail import send_mail
from django.conf import settings
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from django.http import JsonResponse
# Create your views here.
def officerhome(request):
    template = loader.get_template("OfficerHome.html")
    context = {}

    return HttpResponse(template.render(context, request))

def viewoperationofficer(request):
    uname=request.session["uname"]
    uid=officer.objects.get(uname=uname)
    o=operation.objects.raw("select admin_operation.* from admin_operation,major_team,major_officer where major_team.offid=major_officer.id and major_team.oid=admin_operation.id and major_officer.id=%s",[uid.id])
    context = {'k':o}
    template = loader.get_template("viewoperationofficer.html")
    return HttpResponse(template.render(context, request))
def viewmajormsg(request):
    uname=request.session["uname"]
    uid=officer.objects.get(uname=uname)
    m=majortextmsg.objects.raw("SELECT major_majortextmsg.*,admin_major.mname from major_majortextmsg,admin_major,major_officer where admin_major.id=major_majortextmsg.mid and major_majortextmsg.oid=major_officer.id and major_officer.id=%s",[uid.id])


    template = loader.get_template("viewmanjormsg.html")
    context = {'k':m}
    return HttpResponse(template.render(context, request))
def viewmajormsg1(request,id):
    t = majortextmsg.objects.get(id=id)
    context = {'msg': t}
    template = loader.get_template("viewmajormsg1.html")
    return HttpResponse(template.render(context, request))
def staffmsgdecrypt(request):
    id = request.POST.get("id")
    mid = majortextmsg.objects.get(id=id)
    msg = request.POST.get("encmsg")
    key = request.POST.get("prkey")
    m = majortextmsg.objects.filter(id=id)
    for i in m:
        if (i.private == key):
            m1 = i.msg
        else:
            return HttpResponse("<script>alert('Invalid key');window.location='/viewstaffmsg1';</script>")

    # decoded = decrypt_public_key(bytes(msg.encode("utf8")),bytes(key.encode("utf8")))
    t = majortextmsg.objects.get(id=id)
    context = {'dec': m1, 'msg': t, 'key': key}
    template = loader.get_template("viewmajormsg1.html")
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

def staffmsg1(request):
    if request.method=="POST":
        sname = request.POST.get("sname")
        sid=major.objects.get(id=sname)
        msg = request.POST.get("msg")
        email = sid.email
        request.session["email"] = email
        request.session["toid"] = sid.id
        request.session["msg"] = msg
        private, public = generate_keys()
        message = bytes(msg.encode("utf8"))
        encoded = encrypt_private_key(message, public)
        decoded = decrypt_public_key(encoded, private)
        template = loader.get_template("encstaffmessage1.html")
        context = {'enc': encoded, 'prkey': private, 'pbkey': public}
        return HttpResponse(template.render(context, request))
    else:
        s = major.objects.all()
        context={'sname':s}
        template=loader.get_template("addmajortxtmsg.html")
        return HttpResponse(template.render(context,request))
def staffs(request):
    if (request.method == 'GET' and request.GET.get('q') != None):
        sid = request.GET.get('q')
        l = officer.objects.filter(id=sid).values()
        # users_list = list(framework)  # important: convert the QuerySet to a list object
        return JsonResponse(list(l), safe=False)
def encstaffmsg1(request):
    if request.method=="POST":
        t=officertextmsg()
        t.msg=request.session["msg"]
        t.private=request.POST.get("prkey")
        t.public=request.POST.get("pbkey")
        t.encmsg=request.POST.get("encmsg")
        uname=request.session["uname"]
        oid=officer.objects.get(uname=uname)
        t.oid=oid.id
        sid=request.session["toid"]
        s=major.objects.get(id=sid)
        t.mid = s.id

        t.save()
        subject = 'You got an email from defence'
        message = 'plz login your a/c and read the message. your key value='+request.POST.get("prkey")
        email_from = settings.EMAIL_HOST_USER
        mailid = request.session["email"]
        recipient_list = [mailid, ]
        send_mail(subject, message, email_from, recipient_list)

        return HttpResponse("<script>alert('Message Send Successfully');window.location='/staffmsg';</script>")

    else:
        template = loader.get_template("encstaffmessage1.html")
        context = {}
        return HttpResponse(template.render(context, request))

