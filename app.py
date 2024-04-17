from flask import Flask, render_template, request, redirect, url_for 
import sqlite3

app = Flask(__name__)

# Route for tasks 
@app.route("/")
def index():
    return "hi"
    