from django.shortcuts import render, redirect
from .models import User
import mysql.connector
from operator import itemgetter
from django.contrib import  messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

def welcome(request):
    return render(request, 'index.html')

def home(request):    
    return render(request, 'home.html')

def login(request):
    
    con = mysql.connector.connect(host="127.0.0.1", user = "root", password ="root", database="drone")
    cur = con.cursor()
    conn = mysql.connector.connect(host="127.0.0.1", user = "root", password ="root", database="drone")
    curr = conn.cursor()
    
    sqlcommand = "SELECT email from projectdrone_user"
    sqlcommand2 = "SELECT pwd from projectdrone_user"
    cur.execute(sqlcommand)
    curr.execute(sqlcommand2)
    
    e=[]
    p=[]
    
    for i in cur:
        e.append(i)
    for j in curr:
        p.append(j)
        
    res = list(map(itemgetter(0), e))
    res2 = list(map(itemgetter(0), p))
            
    if request.method =="POST":
        email = request.POST['email']
        pwd = request.POST['pwd']
        i=1
        k=len(res)
        while i <k:
            if res[i]==email and res2[i]==pwd:
                return render(request, 'home.html', {'email': email})
                break
            i+=1
        else:
            messages.info(request, "Wrong Password or Email")
            return redirect('login')
                  
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        user = User()
        user.email = request.POST['email']
        user.uname = request.POST['uname']
        user.pwd = request.POST['pwd']
        user.pwd2 = request.POST['pwd2']
        
        if user.pwd != user.pwd2:
            messages.info(request, "Password Not Match")
            return redirect('register')
        elif user.uname == "" or user.pwd =="":
            messages.info(request, "please enter all information")
        else:
            user.save()
            return redirect('login')
            
    
    
    return render(request, 'register.html')

def logout(request):
    try:
        del request.session['email']
    except:
        return render(request, 'index.html')
    return render(request, 'index.html')
