from flask import *
import time
app = Flask(__name__)
account = []
@app.route('/remain/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', says=account)
    else:
        title = request.form.get('say_title')
        text = request.form.get('say')
        user = request.form.get('say_user')
        account.append({"title": title,
                      "text": text,
                      "user": user})
        return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True, )
