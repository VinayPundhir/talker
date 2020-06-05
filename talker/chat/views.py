from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from chat.models import user_data,relation,friend,chat_data,record,active,channel
from chat.forms import login,sinup,chat_data_form
import time


def sent(user):
  temp=relation.objects.all()
  temp1=friend.objects.all()
  list1=[]
  list2=[]
  a=""
  b=""
  c=""
  for i in temp:
     a=i.name
     b=i.Request
     c={"name":a,"Request":b}
     list1.append(c)
  for i in temp1:
     a=i.name
     b=i.friend_name
     c={"name":a,"friend":b}
     list2.append(c)
  sent=False
  print "\n"
  temp=user_data.objects.all()
  u_name=""
  f_name=""
  img=""
  obj=[]
  data1=""
  data2=""
  color=""
  friends=False
  for i in temp:
    u_name=i.name
    img=i.image
    color=i.color
    data1={"name":u_name,"Request":user}
    if data1 in list1:
     sent=True
    if data1 not in list1:
      sent=False
    data2={"name":user,"friend":u_name}
    if data2 in list2:
       friends=True
    else:
        friends=False
    a={"name":u_name,"image":img,"sent":sent,"color":color,"friend":friends}
    obj.append(a)
  print obj,"\n",list2
  return obj


def request_data(request):
  name=request.session["name"]
  valid_request(name)
  obj_name =relation.objects.filter(name=name)
  obj_img=""
  obj_col=""
  a=[]
  b=[]
  obj=[]
  d=[]
  e=[]
  f=[]
  g=[]
  for n in obj_name:
    a=n.Request
    print a
    obj_img=user_data.objects.filter(name=a)
    for i in obj_img:
       b=i.image
       f=i.color
    d={"name":a,"image":b,"color":f}
    print d["name"]
    obj.insert(0,d)
  count=0
  for i in obj:
    if i["name"]:
      count+=1
  print "total r",count 
  return obj,count

def requests(request):
  obj=request_data(request)[0]
  return render(request,"requests.html",{"obj":obj})

def accept_request(request,name):
  info=friend()
  Info=friend()
  user=request.session["name"]
  info.name=user
  Info.name=name
  info.friend_name=name
  Info.friend_name=user
  info.save()
  Info.save()
  info=relation.objects.filter(Request=name)
  info.delete()
  create_channel(user,name)
  return redirect("/friends/")


def create_channel(name,friend):
 temp=channel()
 temp.name=name
 temp.friend_name=friend
 ch_name=time.asctime(time.localtime(time.time())).replace(" ","-")
 ch_name=ch_name.replace(":","-")
 temp.channel_name=ch_name
 temp.save()

def get_channel(name,friend):
 try:
    temp=channel.objects.get(name=name,friend_name=friend)
 except:
    temp=channel.objects.get(name=friend,friend_name=name)
 return temp.channel_name

def video_call(request,name):
 channel=get_channel(request.session["name"],name)
 return render(request,"video_chat_room.html",{"channel":channel,"name":name})
 

def start(request):
 try:
    if request.session["name"]:
     return redirect("/all_users/")
 except:
    return render(request,"login.html")
 return render(request,"login.html")


def send_request(request,name):
  info=relation()
  info.name=name
  user=request.session["name"]
  info.Request=user
  info.save()
  obj=sent(user)
  return render(request,"all_users.html",{"obj":obj})


# Create your views here.
def process(request):
 log=True
 return render(request,"sinup.html",locals())

def process_recieved(request):

 return HttpResponse(request.session["name"])

def all_users(request):
 user=request.session["name"]
 count=""
 if user:
  obj=sent(user)
  count=request_data(request)[1]
  if count is 0:
    count=""
  return render(request,"all_users.html",{"obj":obj,"count":count})
 return render(request,"login.html")

def logout(request):
  name=request.session["name"]
  try:


    temp=user_data.objects.get(name=request.session["name"])
    temp.color="white";
    temp.save()
  except:
     print "------------------------------------"
  try:
       del request.session["name"]
       return redirect("/")
  except:
       return redirect("/")

def login_process(request):
  user=""
  password=""
  if request.method == "POST":
   #Get the posted form
   MyLoginForm = sinup(request.POST,request.FILES)
   if MyLoginForm.is_valid():
     user = MyLoginForm.cleaned_data['username']
     password=MyLoginForm.cleaned_data['password']
  obj=user_data.objects.filter(user=user)
  user_active=user
  state=""
  state_list=[]
  temp=""
  User=""
  Password=""
  name=""
  profile=user_data.objects.all()
  for i in obj:
    User=i.user
    Password=i.password
    name=i.name
  if user == User and password == Password:
   request.session["name"]=name
   user=request.session["name"]
   online(user)
   return redirect("/all_users/")
  else:
    return render(request,"login.html",{"checking":"invalid user"})

def sinup_process(request):
  user=""
  password=""
  age=""
  name=""
  image=""
  form=""
  user_user=""
  user_name=""
  obj=user_data()
  obj1=user_data.objects.all()
  All_names=[]
  All_users=[]
  for i in obj1:
        All_names.append(i.name)
        All_users.append(i.user)
  if request.method == "POST":
   #Get the posted form
   MyLoginForm = login(request.POST,request.FILES)
   if MyLoginForm.is_valid():
      user_user= MyLoginForm.cleaned_data['username']
      if user_user in All_users:
             return render(request,"sinup.html",{"checking":"username exists"})
      user_name= MyLoginForm.cleaned_data['name']
      if user_name in All_names:
             return render(request,"sinup.html",{"checking":"name exists"})
      if " " in user_user: 
           return render(request,"sinup.html",{"checking":"Don't use space in username"})
      if " " in user_name:
            return render(request,"sinup.html",{"checking":"Don't use space in name"})
      obj.password=MyLoginForm.cleaned_data['password']
      obj.age = MyLoginForm.cleaned_data['age']
      obj.user=user_user
      obj.name=user_name
      obj.image= MyLoginForm.cleaned_data['image']
      obj.save()
  profile=user_data.objects.all()
  request.session["name"]=user_name
  online(user_name)
  return render(request,"all_users.html",{"obj":profile})


def friends(request):
  name=request.session["name"]
  obj_name =friend.objects.filter(name=name)
  obj_img=""
  obj_col=""
  a=[]
  b=[]
  obj=[]
  d=[]
  e=[]
  f=[]
  g=[]
  for n in obj_name:
    a=n.friend_name
    obj_img=user_data.objects.filter(name=a)
    for i in obj_img:
       b=i.image
       f=i.color
    d={"name":a,"image":b,"color":f}
    obj.insert(0,d)
  return render(request,"friends.html",{"obj":obj})

def chatting(request,name):
  s_name=request.session["name"]
  user=chat_data.objects.filter(name=s_name,friend_name=name)
  friend=chat_data.objects.filter(name=name,friend_name=s_name)
  a=[]
  b=[]
  c=[]
  d=[]
  obj=[]
  for i in user:
    c={"num":i.num,"msg":i.msg,"name":s_name}
    a.insert(0,c)
  for j in friend:
    c={"num":j.num,"msg":j.msg,"name":name}
    b.insert(0,c)
  friend_obj=user_data.objects.filter(name=name)
  f_img=""
  f_name=""
  for i in b:
     c={"num":i["num"],"msg":i["msg"],"name":i["name"]}
     a.append(c)
  for i in friend_obj:
    f_img=i.image.url
    f_name=i.name
  obj=sorted(a,key=lambda s:s["num"])
  return render(request,"public_profile.html",{"obj":obj,"f_img":f_img,"f_name":f_name})


#----------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------xxxxxxxxxx---------------------------------------------------------------------
#---------------------------------------------------------xxxxxxxxxx---------------------------------------------------------------------
#---------------------------------------------------------xxxxxxxxxx---------------------------------------------------------------------
#---------------------------------------------------------xxxxxxxxxx---------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------


def chatting_process(request,name):
  rec=record.objects.get(name="track")
  rec.num=rec.num+1
  print "its",rec.num
  rec.save()
  msg=""
  image=""
  if request.method == "POST":
   #Get the posted form
   MyLoginForm = chat_data_form(request.POST,request.FILES)
   print " inside post"
   if MyLoginForm.is_valid():
     print "inside valid"
     msg = MyLoginForm.cleaned_data['msg']
     image=MyLoginForm.cleaned_data['image']
     print "image",image
   if not  MyLoginForm.is_valid():
     print "inside invalid"
     try:
       msg = MyLoginForm.cleaned_data['msg']
     except:
       msg=""
     try:
       image=MyLoginForm.cleaned_data['image']
     except:
       image=""
  print "msg  ",msg," image  ",image,type(image),len(image)
  if image !="" or   msg != "" :
    print "saved"
    obj=chat_data(name=request.session["name"],friend_name=name,msg=msg,image=image,num=rec.num)
    obj.save()
  else:
    print "not saved"
  return redirect("/chatting/"+name)


def json(request,name):
  s_name=request.session["name"]
  user=chat_data.objects.filter(name=s_name,friend_name=name)
  friend=chat_data.objects.filter(name=name,friend_name=s_name)
  a=[]
  b=[]
  c=[]
  d=[]
  image=""
  obj=[]
  for i in user:
    try:
      image=i.image.url
    except:
      image="" 
    c={"num":i.num,"msg":i.msg,"name":s_name,"image":image}
    a.insert(0,c)
  for j in friend:
    try:
      image=j.image.url
    except:
      image="" 
    c={"num":j.num,"msg":j.msg,"name":name,"image":image}
    b.insert(0,c)
  friend_obj=user_data.objects.filter(name=name)
  f_img=""
  f_name=""
  for i in b:
     c={"num":i["num"],"msg":i["msg"],"name":i["name"],"image":i["image"]}
     a.append(c)
  for i in friend_obj:
    f_img=i.image.url
    f_name=i.name
  obj=sorted(a,key=lambda s:s["num"])
  data={
       'obj':obj,'f_name':f_name,'f_img':f_img,'user':s_name
      }
  return JsonResponse(data)


def valid_request(name):
  f=friend.objects.filter(name=name)
  for i in f:
    g=relation.objects.filter(name=name,Request=i.friend_name)
    g.delete()
    g=relation.objects.filter(name=name,Request=name)
    g.delete()
    print "i m working for valid_request"


def chat_size(request,name):
  s_name=request.session["name"]
  user=chat_data.objects.filter(name=s_name,friend_name=name)
  friend=chat_data.objects.filter(name=name,friend_name=s_name)
  a=[]
  b=[]
  c=[]
  d=[]
  obj=[]
  for i in user:
    c={"num":i.num,"msg":i.msg,"name":s_name}
    a.insert(0,c)
  for j in friend:
    c={"num":j.num,"msg":j.msg,"name":name}
    b.insert(0,c)
  friend_obj=user_data.objects.filter(name=name)
  f_img=""
  f_name=""
  for i in b:
     c={"num":i["num"],"msg":i["msg"],"name":i["name"]}
     a.append(c)
  for i in friend_obj:
    f_img=i.image.url
    f_name=i.name
  obj=sorted(a,key=lambda s:s["num"])
  size=len(obj)
  data={
            "size":size      }
  return JsonResponse(data)

def online(user):
    temp=user_data.objects.get(name=user)
    temp.color="green"
    temp.save()

def decline_request(request,name):
  temp=relation.objects.get(name=request.session["name"],Request=name)
  temp.delete()
  return redirect("/all_users/")



