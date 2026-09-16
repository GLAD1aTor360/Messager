from flask import Flask,render_template,request, redirect, url_for
import db
app=Flask("Сервер")



@app.route("/register", methods=["GET", "POST"])
def reg():
    if request.method=="GET":
        return render_template("register.html")
    if request.method=="POST":
        login=request.form.get("name")
        password=request.form.get("password")
        password2=request.form.get("password2")
        erlog=None
        erpass1=None
        erpass2=None
        if not login:
            erlog=("Введите логин!")
        if not password:
            erpass1=("Введите пароль!")
        if not password2:
            erpass2=("Повторите пароль!")
        if password!=password2:
             erpass2=("Пароли не совпадают!")
        a=db.find_login(login)
        if a==True:
            erlog=("Логин занят!")
        if erlog!=None or erpass1!=None or erpass2!=None:
            return render_template("register.html", erlog=erlog, erpass1=erpass1, erpass2=erpass2)
        b=db.create_user(login, password)
        return render_template("settings.html")


@app.route("/login", methods=["GET", "POST"])
def log():
    if request.method=="GET":
        return render_template("log.html")
    if request.method=="POST":
        log=request.form.get("name")
        password=request.form.get("password")
        erlog=None
        erpass=None
        if not log:
            erlog=("Введите логин!")
        if not password:
            erpass=("Введите пароль!")
        t=db.check_user(log, password)
        if t==False:
            erlog="Такого логина не существует!"
            erpass="Неверный пароль!"
        if erlog!=None or erpass!=None:
            return render_template("log.html", erlog=erlog, erpass=erpass)
        if t==True:
            return redirect(url_for("main"))
        



@app.route("/main", methods=["GET", "POST"])
def main():
    if request.method=="GET":
        return render_template("main.html", chats=[1,2,3,4,5])
    
@app.route("/save-settings", methods=["POST"])
def ss():
    return redirect(url_for("main"))