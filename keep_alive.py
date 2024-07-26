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
