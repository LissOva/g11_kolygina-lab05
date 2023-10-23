
from flask import Flask, render_template, request
from datetime import datetime

app = Flask('lab05')
items = []
@app.route('/')
def some_page():
	n = request.args.get('param')
	t = datetime.now()
	s = t.strftime('%H:%M:%S')
	return render_template('index.html',name = str(n),your_time_here=s)
	
@app.route('/list', methods=['GET', 'POST'])
def some_list():
	if request.method == 'POST':
		text = request.form.get('content')
		items.append(text)
		return  render_template('list.html', text_items=items)
	return  render_template('list.html', text_items=items)
