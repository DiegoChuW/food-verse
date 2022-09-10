from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import abort, redirect, url_for
import json

#TODO: create basic login code, store usernames and passwords in json file, get the user prefereces uploaded and stored in json
#basically make a user object
#create list of recipies that will be stored (maybe make a quick helper program to copy and paste the recipe instructions into)
#create function that filters recipes based on preferences
#figure out templates and create the feed page
#find the way to insert the image and info of the chosen recipe into the template

app = Flask(__name__)
def get_new_id():
    max=0
    for i in userdata:
        i=int(i)
        if(i>max):
            max=i
    return max+1
with open("userdata.json") as f:
    userdata=json.load(f)

@app.route("/", methods=['GET', 'POST'])
def index():
    username = request.cookies.get('username')
    return "Main page"

@app.route("/feed")
def feed():
    username = request.cookies.get('username')
    with open("recipes.json") as f:
        data=json.load(f)
    return render_template("feed.html",data=data)

@app.get("/profile")
def profile_get():
    username = request.cookies.get('username')
    print(username)
    if(username):
        return render_template("profile.html")
    else:
        redirect("/login")

@app.post("/profile")
def profile_post():
    for i in userdata:
        if(userdata[str(i)]["name"]==request.cookies.get('username')):
            userdata[str(i)]["preferences"]=json.loads(request.data.decode('ascii'))
            with open("userdata.json","w+") as f:
                json.dump(userdata,f)
            break
    return redirect('/')

@app.get("/register")
def view_register_page():
    return render_template("register.html")

@app.post("/register")
def register_user():
    try:
        newuser=json.loads(request.data.decode('ascii'))
        for i in userdata:
            if(userdata[str(i)]["name"]==newuser["name"]):
                return redirect('/')
        userdata[str(get_new_id())]=newuser
        with open("userdata.json","w+") as f:
            json.dump(userdata,f)
    except Exception as e:
        print(e)
    return redirect('/')

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        try:
            data=json.loads(request.data.decode('ascii'))
        except:
            data={"name":"user0"}
        resp = make_response(render_template('profile.html'))
        resp.set_cookie('username', data["name"])
        print("LOGGED IN")
        return resp
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)#the login.html will need to show an invalid username error if the error variable is true (the variable is passed into template so we will figure out how to convert from the code html written to the template format)
