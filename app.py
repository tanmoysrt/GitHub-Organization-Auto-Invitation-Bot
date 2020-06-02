from flask import Flask, request,jsonify,render_template
from github import Github
import os
from dotenv import load_dotenv

if os.path.exists('.env'):
    load_dotenv()
token = os.getenv("token")
organization_name=os.getenv("organization_name")
redirection_url=os.getenv("redirection_url")

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('register.html')
@app.route('/invite',methods=['POST','GET'])
def invite():
    if(request.method=='GET'):
        email=request.args.get('git_email')
        gh = Github(token)
        org = gh.get_organization(organization_name)

        try:
            org.invite_user(email=email)
            return render_template('success.html',redirection_url=redirection_url)
        except :
            return render_template('unsuccess.html')

if __name__== '__main__':
    app.run(debug=True)