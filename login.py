from flask import Flask, request, g, redirect, url_for, render_template, flash, session
import flask
import sys
from flask import json



import forms


app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
lista=[]
@app.route('/',methods=['GET','POST'])

def pagina_principal ():


        return render_template("pagina_principal.html")

@app.route('/login')

def login ():

        return render_template("login.html")

@app.route('/login/inicio_sesion',methods=["GET","POST"])

def inicio_sesion ():
        login=False
        indice_u=0
        indice_p=0

        user= request.form['name']
        pswd= (request.form["password"])
        f = open("usuarios.txt", "r")
        texto = f.readlines()
        f.close()
        usuarios=(texto[0]).split()
        g = open("claves.txt", "r")
        texto = g.readlines()
        g.close()
        claves=(texto[0]).split() 
        ind=0
        for i in usuarios:         
                print(i)
                if i==user :
                        login=True
                        indice_u=ind
                ind+=1
        ind=0
        for i in claves:


                print(i)
                if i==pswd :
                        login=True
                        indice_p=ind
                ind+=1
        print(indice_u)
        print(indice_p)
        if login and indice_p==indice_u:

                return render_template("inicio_sesion.html")
        else:
                return render_template("login.html")
@app.route('/register',methods=['GET', 'POST'])




def register ():




        return render_template("register.html")




@app.route('/register/pra',methods=['GET', 'POST'])

def registro():


        if request.method =="POST":
                user= request.form['name']
                pswd= (request.form["password"])
                f = open("usuarios.txt", "r")
                texto = f.readlines()
                f.close()
                usuarios=(texto[0]).split()
                g = open("claves.txt", "r")
                texto = g.readlines()
                g.close()
                claves=(texto[0]).split()       
        if  not(user in usuarios):
                f = open("usuarios.txt", "a")
                f.write(user+" ")
                f.close()
                            
        if  not(pswd in claves):
                f = open("claves.txt", "a")
                f.write(pswd+" ")
                f.close()
                                       


        







        return render_template("register.html")




if __name__ == '__main__':
        app.run(debug=True,port=9200)

