from flask import render_template,flash,redirect,url_for,request,jsonify,abort
from app import app,db
from flask_login import current_user, login_user,logout_user,login_required
from app.models import Task
from werkzeug.urls import url_parse
from datetime import datetime


@app.route('/v0/sample_get',methods=["GET"])
def sample_get():
    return "Hello Flask"

@app.route('/v0/sample_post',methods=['POST'])
def sample_post():
        if not request.json or not 'name' in request.json:
            abort(400)
        return "Hello to Flask, "+str(request.json.get('name',""))


@app.route('/v1/list_all',methods=["GET"])
def list_all():
    tasks=Task.query.all()
    ls=[]
    for i in tasks:
        ls.append(str(i.body))
    return jsonify({'tasks':ls})

@app.route('/v1/append',methods=["POST"])
def append():
    if not request.json or not 'task' in request.json:
        abort(400)
    numrows=db.session.query(Task).count()
    tsk=str(request.json.get('task',"")) 
    n=Task(body=tsk,pos=numrows+1)
    db.session.add(n)
    db.session.commit()
    return jsonify({'status':'200'})

@app.route('/v1/get',methods=["GET"])
def get():
    idx=request.args.get('index',-1)    
    numrows=db.session.query(Task).count()
    if(idx<1 or idx>numrows):
        abort(400)
    temp=Task.query.filter_by(pos=idx).first()
    return jsonify({'task':temp.body})

@app.route('/v1/insert',methods=["POST"])
def insert():
    if not request.json or not 'task' in request.json or not 'index' in request.json:
        abort(400)
    numrows=db.session.query(Task).count()
    idx=int(request.json.get('index',-1))
    if(idx<1 or idx>numrows+1):
        abort(403)
    tsk=request.json.get('task',"")
    if(idx==numrows+1):
        n=Task(body=tsk,pos=numrows+1)
    else:
        tasks=Task.query.filter(Task.pos>=idx)
        for i in tasks:
            i.pos+=1
        n=Task(body=tsk,pos=idx)
    db.session.add(n)
    db.session.commit()
    return jsonify({'status':'200'})

@app.route('/v1/delete/<int:index>',methods=["DELETE"])
def delete(index):
    numrows=db.session.query(Task).count()
    if(index<1 or index>numrows):
        abort(400)
    temp=Task.query.filter_by(pos=index).first()
    msg=temp.body
    db.session.delete(temp)
    tasks=Task.query.filter(Task.pos>index)
    for i in tasks:
        i.pos-=1
    db.session.commit()
    return jsonify({'task':msg})