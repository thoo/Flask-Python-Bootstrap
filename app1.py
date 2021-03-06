from output_form1 import DemoForm
from flask import Flask, render_template, request
from function  import GDP_PCA_plot
import sys, os, inspect
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.config.update(dict(
    SECRET_KEY = 'pandindan lan',
    CSRF_ENABLED = True,
))

@app.route('/', methods=['GET', 'POST'])
def index():
    dict1={}
    form = DemoForm(request.form)


    #print(form)
    if request.method == 'POST' and form.validate_on_submit():
        #print("form",form.data['multi_select'])
        #print("form.multi_select_plot.data",form.multi_select_plot.data)
        result = GDP_PCA_plot(form.multi_select.data,form.multi_select_plot.data)
        #print(result)
    else:
        result = None

    return render_template('view_2_1.html', form=form,
                           result=result)

if __name__ == '__main__':
    app.run(port=33035,debug=False)
