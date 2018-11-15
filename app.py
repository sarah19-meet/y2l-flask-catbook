from flask import Flask
from flask import render_template
from database import get_all_cats, get_cat_by_id

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def new_home(id):
	cat=get_cat_by_id(id)
	return render_template("cat.html", cat=cat)

@app.route('/create', methods=['GET','POST'])
def cat_new():
	if reguest.method == 'GET':
		return render_template("cat_new.html")
	else:
		name=request.form['catname']

		save_database(name)
		return render_template("home.html", n=name
			)

	

if __name__ == '__main__':
   app.run(debug = True)
