#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Assignment 11

from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)

tdlist = []

@app.route('/')
def hello_world():
    return render_template('index.html', tdlist = tdlist)


@app.route('/submit', methods = ['POST'])
def submit():
    if not (re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", request.form['email'])):
        return redirect('/')
    else:
        tdlist.append((request.form['task'], request.form['email'], request.form['priority']))
        return redirect('/')
    

@app.route('/clear', methods = ["POST"])
def clear():
    del tdlist[:]
    return redirect('/')
    
    

if __name__ == '__main__':
    app.run()


# In[ ]:




