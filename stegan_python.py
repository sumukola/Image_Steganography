from flask import Flask , redirect, url_for, render_template, request, flash,send_from_directory,Response
from steganography import Steganography
from main import imagemerge , textmerge 
import imghdr
from PIL import Image
import os,shutil
from werkzeug.utils import secure_filename
from  Text_in_Image import *

app = Flask(__name__)
app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
response=Response()
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'static/uploads')
OUTPUTS=os.path.join(path,'static/outputs')
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
WD = os.getcwd()
app.config['WD']=WD
PEOPLE_FOLDER = os.path.join('static', 'outputs')
app.config['UPLOAD_FOLD'] = PEOPLE_FOLDER

if not os.path.isdir(OUTPUTS):
    os.mkdir(OUTPUTS)
app.config['OUTPUTS'] = OUTPUTS

ALLOWED_EXTENSIONS = set(['png', 'jpg'])
@app.route("/")
def home():
    return render_template('htmlpage.html')
     
@app.route('/tini', methods=['GET','POST'])
def tini():
    return render_template('TII.html')

@app.route('/iini', methods=['GET','POST'])
def iini():
    return render_template('III.html')
    
@app.route('/extract' , methods=['GET','POST'])
def extract():
    return render_template('extract_tii.html')
    
@app.route('/extra' , methods=['GET','POST'])
def extra():
    return render_template('extractiii.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
    return render_template('III.html')

@app.route('/', methods=['POST'])
def upload_file():
    if 'tii' in request.form:
        if request.method =='POST':
            if 'img' not in request.files:
                return redirect(request.url)
            file= request.files['img']
            if file.filename == '':
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                message=request.form.get("message")
                return  htii(message,file)
            else:
                return redirect(request.url)
    else:
        if request.method == 'POST':
            if 'img1' not in request.files:
                return redirect(request.url)
            if 'img2' not in request.files:
                return redirect(request.url)
            file1= request.files['img1']
            file2= request.files['img2']
            if file1.filename == '' or file2.filename=='':
                return redirect(request.url)
            if (file1 and allowed_file(file1.filename)) and (file2 and allowed_file(file2.filename)):
                filename = secure_filename(file1.filename)
                file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                filename = secure_filename(file2.filename)
                file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return hiini(file1,file2)
            else:
                return redirect(request.url)
                
@app.route('/textini', methods=['POST'])
def textini():
    if request.method =='POST':
        if 'image' not in request.files:
            return redirect(request.url)
        file= request.files['image']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(filename)
            decoded_text=textmerge.Decrypt(file)
            return decoded_text
        else:
            return redirect(request.url)
            
@app.route('/imageini',methods=['POST'])
def imageini():
    if request.method =='POST':
        if 'img' not in request.files:
            return redirect(request.url)
        file= request.files['img']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(filename)
            decoded_image=imagemerge.unmerge(file)
            decoded_image.save(os.path.join(app.config['OUTPUTS'],'decoded_image.png'))
            full_filename = os.path.join(app.config['UPLOAD_FOLD'], 'decoded_image.png')
            return render_template("show.html", user_image = full_filename )
        else:
            return redirect(request.url)
    
                     
@app.route('/hiini',methods=['GET','POST'])
def hiini(file1,file2):
        merged_image = imagemerge.merge(file1,file2)
        fname = request.form.get('filename')
        error=None
        if merged_image is not None:
            merged_image.save(os.path.join(app.config['OUTPUTS'], 'hidden_image.png'))
            full_filename = os.path.join(app.config['UPLOAD_FOLD'], 'hidden_image.png')
            return render_template("show.html", user_image = full_filename)
        else:
            return "Size of image 1 should be larger than image2"
    
@app.route('/htii' ,methods=['GET','POST'])
def htii(message,file):
   encrypted=textmerge.Encrypt(message,file)
   #fname = request.form.get('filename')
   encrypted.save(os.path.join(app.config['OUTPUTS'], 'hidden.png'))
   full_filename = os.path.join(app.config['UPLOAD_FOLD'], 'hidden.png')
   return render_template('show.html',user_image = full_filename)
  
'''@app.route('/eiini',methods=['GET','POST'])
def eiini():
    file=request.form.get('file')
    fname=request.form.get('filename')
    decoded_image=imagemerge.unmerge(file)
    decoded_image.save(os.path.join(app.config['OUTPUTS'], fname + '.png'))
    full_filename = os.path.join(app.config['UPLOAD_FOLD'], fname + '.png')
    return render_template("show.html", user_image = full_filename)
    #return redirect(url_for('upload_form'))'''
    
if __name__ == "__main__":
    app.run(debug=True)