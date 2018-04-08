import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
from flask import Flask,url_for,render_template,request,url_for,redirect,send_from_directory
from addMark import addWaterMarking
from testMark import testWaterMarking
from werkzeug import secure_filename
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

UPLOAD_FOLDER='home'
ALLOWED_EXTENSIONS=set(['png','jpg','jpeg','gif'])

app=Flask(__name__)
global strMark
strMark = ' '
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route('/',methods=['GET','POST'])
def upload_file():
    if request.method=='POST':
        file1=request.files['file']
        file2=request.files['file_mask']
        if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename):
            addWaterMarking(file1,file2)
            return redirect(url_for('upload_file'))
    return '''
    <!DOCTYPE html>
    <title>upload new file</title>
    <h1>Add Digital Watermarking</h1>
	<h2>Choose picture</h2>
    <form action="/" method="POST" enctype="multipart/form-data">
    <input type="file" name="file" />
	<h2>Choose Watermarking</h2>
    <form action="/" method="POST" enctype="multipart/form-data">
    <input type="file" name="file_mask" />
	<p>
    <input type="submit" value="handle" />
	</p>
	<a href="test">Test Watermarking</a>
	<p>
	<script type="text/javascript">  
	document.write("<img src='../static/output.png?v="+new Date().getTime()+"'>");   
	</script>  
	</p>
    </form>
    '''

	
@app.route('/test',methods=['GET','POST'])
def test_file():
    global strMark
    if request.method=='POST':
        file1=request.files['file']
        file2=request.files['file_mask']
        if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename):
            boolMark = testWaterMarking(file1,file2)
            if boolMark == False:
				strMark = 'False'
            else:
				strMark = 'True'
            return redirect(url_for('test_file'))
    return '''
    <!DOCTYPE html>
    <title>upload new file</title>
    <h1>Test Digital Watermarking</h1>
	<h2>Choose picture</h2>
    <form action="/test" method="POST" enctype="multipart/form-data">
    <input type="file" name="file" />
	<h2>Choose Watermarking</h2>
    <form action="/test" method="POST" enctype="multipart/form-data">
    <input type="file" name="file_mask" />
	<p>
    <input type="submit" value="handle" target="/test" />
	</p>
	<a href="/">Add Watermarking</a>
	<p>
	'''	+ strMark+	'''
	</p>
    </form>
    '''
	
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)
	
	
if __name__ == '__main__':
    strMark = ''
    app.run()
	