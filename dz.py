from flask import Flask,render_template,request
import db
app=Flask("Сервер")

def didgit(password):
    h=0
    for i in password:
        if i in "1234567890":
            h=h+1
    if h==0:
        return False
    else:
        return True
    
def abc(password):
    h=0
    for i in password:
        if i in "QWERTYUIOPASDFGHJKLZXCVBNM":
            h=h+1
    if h==0:
        return False
    else:
        return True

@app.route("/h", methods=["GET", "POST"])
def h():
    if request.method=="GET":
        return render_template("index.html")
    if request.method=="POST":
        m=request.form.get("name1")
        erp=None
        answer=None
        if not m:
            erp=("Пароль не введён")
        r=didgit(m)
        if r==False:
            erp=("Пароль должен содержать хотя бы одну цифру")
        if len (m)<8:
            erp=("Пароль слишком короткий")
        q=abc(m)
        if q==False:
            erp=("Пароль должен содержать хотя бы одну заглавную букву")
        else:
            answer=("Пароль надёжный")
        return render_template("index.html", erp=erp, answer=answer)


food=[]

@app.route("/g", methods=["GET", "POST"])
def g():
    if request.method=="GET":
        return render_template("index.html")
    if request. method=="POST":
        j=request.form.get("n1")
        error=None
        if not j:
            error=("Введите что-либо")
        else:
            food.append(j)
        return render_template("index.html", food=food, error=error)