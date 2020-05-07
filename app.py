from flask import Flask,render_template,request
import imageScrapper

app = Flask(__name__)

app.config['SECRET_KEY']='uttutu'

images=[]

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":
            topic = request.form['search']
            print(topic)
            
            images = imageScrapper.get_images(topic)

            if(images == 1):
                return render_template('index.html',error=1)
            else:
                return render_template('index.html',info=images)

    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
    