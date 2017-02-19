


from flask import Flask, render_template, request
from wtforms import Form, FloatField, validators
#from compute import compute



app = Flask(__name__)

class Inputform(Form):
    r = FloatField(validators=[validators.InputRequired()])
    m = FloatField(validators=[validators.InputRequired()])

   # a = FloatField(validators=[validators.InputRequired()])
   # b = FloatField(validators=[validators.InputRequired()])
    #c = FloatField(validators=[validators.InputRequired()])
   # d = FloatField(validators=[validators.InputRequired()])

@app.route("/", methods=['GET','POST'])
def index():
    form=Inputform(request.form)
    if request.method== 'POST' and form.validate():
        r = form.r.data
        m = form.m.data
       # a = form.a.data
        # b = form.b.data
       # c = form.c.data
        #d = form.d.data
        s= r*m
        l= r+m
        n= r-m
        v= r/m

        def lcm(x, y):
            if x > y:
                greater = x
            else:
                greater = y

            while (True):
                if ((greater % x == 0) and (greater % y == 0)):
                    lcm = greater
                    break
                greater += 1

            return lcm
        k = lcm(r,m)

        def gcd(x, y):

            gcd = (x * y) // lcm(x, y)
            return gcd

        g = gcd(r,m)

        return render_template("view_output_2.html", form=form, s=s, l=l, n=n, v=v, g=g, k=k)
    else:
        return render_template("view_input_2.html", form=form)

def hello():
    return "Second Python application trial"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
