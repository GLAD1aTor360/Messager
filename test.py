from flask import Flask, render_template, request
app=Flask("mess") 


@app.route("/", methods=["GET"])
def slash():
    return render_template("me.html")