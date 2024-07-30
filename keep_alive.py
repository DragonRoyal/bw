import secrets
from threading import Thread
generated_key = secrets.token_urlsafe
from io import BytesIO
from PIL import Image
import os
from flask import *
from PIL import *
import random
import flask
from flask import jsonify
import requests
from replit import db
import os

app = flask.Flask(__name__)
pass
@app.route('/')
def main():
  return flask.render_template("index.html")   

def run():
  app.run(host="0.0.0.0", port=8080)

responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
             "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.",
             "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.",
             "Yes.", "Yes – definitely.", "You may rely on it."]

def keep_alive():
    server = Thread(target=run)
    server.start()

@app.route("/api")
async def apiidklol():
  return redirect('https://youtu.be/dQw4w9WgXcQ')

@app.route("/register")
async def api_key_register():
  pass


@app.route("/register/discord",methods=['get'])
async def discord_url():
  discord_url_link='https://discord.com/api/oauth2/authorize?client_id=873325983405580338&redirect_uri=https%3A%2F%2Fmaiapi.dragonroyale.repl.co%2Fregister%2Fdiscord&response_type=code&scope=identify%20guilds%20email'

  url = "https://discord.com/api/users/@me"
  access_token = Oauth.get_access_token(str(quart.request.args['code']))
  
  headers = {"Authorization": f"Bearer {access_token}"}
  gen_key=secrets.token_hex(20)
  user_object = requests.get(url = url, headers = headers).json()
  print("user objetc",user_object)
  userid=user_object["id"]
  with open('apikey.csv', mode='r') as keyfile:
    csv_reader = csv.reader(keyfile, delimiter=',')
    userid_exists = 0
    for row in csv_reader:
      if row[0]==userid:
        print(f"user id:{userid} already exists ")
        userid_exists=1
        return "Only 1 api key per User, You already have one"
        #break
        
  if userid_exists==0:
    with open('apikey.csv', mode='a') as keyfile:
      key_writer = csv.writer(keyfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      key_writer.writerow([userid, gen_key,])
    
  return f"sucessful your api key is {genkey}"

@app.route('/wanted',methods=['GET'])
def wanted():
    if 'avatar' in flask.request.args:
        Lavatar = str(flask.request.args['avatar'])
        response = requests.get(Lavatar)
        image = Image.open(BytesIO(response.content))
        image.save("avatar.png")
        pfp=Image.open("avatar.png")
        pfp=pfp.resize((177,177))
        wanted =Image.open("image/wanted.jpg")
        wanted.paste(pfp,(120,212))
        wanted.save("trash_photo/wanted2.png")
        return  send_file("trash_photo/wanted2.png", mimetype='image/png')
 

    else:
      return page_not_found(404)


@app.route('/greyscale',methods=['GET'])
def grey_scale():
    if 'avatar' in flask.request.args:
        Lavatar = str(flask.request.args['avatar'])
        response = requests.get(Lavatar)
        image = Image.open(BytesIO(response.content))
        pfp = image.convert("L")
        pfp.save("greyscale.png")
        return send_file("greyscale.png", mimetype='image/png')
        #pfp = pfp.open('profile.png')

@app.route('/drake',methods=['GET'])
def drake():
  my_image = Image.open("drake.png")

@app.route('/dog',methods=['GET'])
def dogs():
  imgList= os.listdir("dogs")
  dog = random.choice(imgList)
  print(dog)
  return send_file(f"dogs/{dog}")

@app.route('/cat',methods=['GET'])
def cats():
  imgList= os.listdir("cats")  
  cat = random.choice(imgList)
  print(cat)
  return send_file(f"cats/{cat}")

@app.route('/punch',methods=['GET'])
def punchs():
  imgList= os.listdir("punchs")  
  punch = random.choice(imgList)
  return send_file(f"punchs/{punch}",mimetype='image/gif')
   
   
@app.route('/rip',methods=['GET'])
def restip():
  print("R.I.P")
  return send_file("image/rip.png")


@app.route('/support')
def support():
  return render_template("support.html")

@app.route('/api')
def api():
  return render_template("api.html")

@app.route('/doc')
def doc():
  return render_template("doc.html")

@app.route('/projects')
def projects():
  return render_template("projects.html")

@app.route('/fact')
def fact():
  return random.choice(db["facts"])

@app.route('/8ball')
def get8ballresponse():
  question = request.args.get('question')
  return jsonify({
    "question" : question,
    "response" : random.choice(responses)
  })

@app.route('/admin')
def admin_panel():
  if str(request.args.get('password')) == os.getenv('password'):
    return render_template('admin.html')
  else:
    return redirect('/')

#app.run(host="0.0.0.0",port=80,)
