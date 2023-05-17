import datetime
import sqlite3

from flask import Flask, render_template, session, redirect, url_for, request, abort, g, flash, make_response




app = Flask(__name__)

@app.route('/pets')
@app.route('/')
def caucau():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)