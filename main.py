from flask import Flask,render_template,request,url_for,redirect,Response,session
import cv2
from deepface import DeepFace

global aadharno,capture
capture=0
myapp = Flask(__name__)
cam = cv2.VideoCapture(0)
@myapp.route('/')
def homepage():
    return render_template("homepage.html")

@myapp.route('/',methods=['POST'])
def store():
    global aadharno
    aadharno = request.form.get('Aadhar')
    session["aadharno"] = aadharno
    return redirect(url_for('camera'))
    
   
@myapp.route('/camera')
def camera():
    return render_template('camera.html')


def gen():
    global capture
    while True:
        suc,frame = cam.read()
        if suc:
            if(capture):
                capture=0
                p='img.png'
                cv2.imwrite(p,frame)
                
            try:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')    
            except Exception as e:
                pass
            
        else:
            break
            
@myapp.route('/requests',methods=['POST'])
def tasks():
    if request.method == 'POST':
        if request.form.get('capture') == 'capture':
            global capture
            capture=1
            global aadharno
            if "aadharno" in session:
                aadharno = session["aadharno"]
                #print(aadharno)
                aadhar_image = cv2.imread('static/data/' + aadharno + '.jpg')
                p = cv2.imread('img.png')
                result = DeepFace.verify(p,aadhar_image,model_name="Facenet",enforce_detection=False,
                         distance_metric='euclidean_l2',detector_backend = 'retinaface')
                print(result)
                if result['verified']:
                    return redirect('/success')
                else:
                    return redirect('/failure')
    return render_template('camera.html')

@myapp.route('/video')
def video():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')

@myapp.route('/success')
def success():
    return render_template('verified.html')

@myapp.route('/failure')
def failure():
    return render_template('notverified.html')



if __name__=="__main__":
    myapp.secret_key= 'super secret key'
    myapp.config['SESSION_TYPE']='filesystem'
   
    myapp.run(debug=True,port=8000)