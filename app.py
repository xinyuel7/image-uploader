from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, IMAGES, UploadSet



app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['UPLOADED_IMAGES_DEST'] = 'uploads/images'#the place where we save the images
 
images = UploadSet('images', IMAGES)
configure_uploads(app, images)

class MyForm(FlaskForm):
    image = FileField('image')

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        filename = images.save(form.image.data)
        return f'Filename: {filename}'
    return render_template('index.html', form = form)