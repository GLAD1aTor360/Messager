from flask import Flask,render_template,request, redirect, url_for, session
import db
app=Flask("Сервер")

app.config["SECRET_KEY"]="456988T4W986YBT7N43N987Y3409856nB 045687B540"


@app.route("/register", methods=["GET", "POST"])
def reg():
    if "login" in session:
            return redirect(url_for("main"))
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
        session["login"]=login
        return render_template("settings.html")


@app.route("/login", methods=["GET", "POST"])
def log():
    if "login" in session:
        return redirect(url_for("main"))
    if request.method=="GET":
        return render_template("log.html")
    if request.method=="POST":
        login=request.form.get("name")
        password=request.form.get("password")
        erlog=None
        erpass=None
        if not login:
            erlog=("Введите логин!")
        if not password:
            erpass=("Введите пароль!")
        t=db.check_user(login, password)
        if t==False:
            erlog="Такого логина не существует!"
            erpass="Неверный пароль!"
        if erlog!=None or erpass!=None:
            return render_template("log.html", erlog=erlog, erpass=erpass)
        if t==True:
            session["login"]=login
            return redirect(url_for("main"))
        



@app.route("/main", methods=["GET", "POST"])
def main():
    if "login" not in session:
        return redirect(url_for("log"))
    if request.method=="GET":
        return render_template("main.html", chats=[1,2,3,4,5])
    
@app.route("/save-settings", methods=["POST"])
def ss():
    return redirect(url_for("main"))