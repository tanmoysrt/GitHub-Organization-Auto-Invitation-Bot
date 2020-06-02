from flask import Flask, request,jsonify,render_template
from github import Github
from boto.s3.connection import S3Connection
from dotenv import load_dotenv
import os
if os.path.exists('.env'):
    load_dotenv('.env')
    token = os.getenv("TOKEN")
    organization_name=os.getenv("ORGANIZATION_NAME")
    redirection_url=os.getenv("REDIRECTION_URL")
else:
    token = os.environ("TOKEN")
    organization_name=os.environ("ORGANIZATION_NAME")
    redirection_url=os.environ("REDIRECTION_URL")

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
    app.run()