from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
messages = []


@app.route('/', methods=['GET', 'POST'])
def index():
    global messages
    if request.method == 'POST':
        message_text = request.form['message']
        messages.append(message_text)
        with open('requirements.txt', 'a') as f:
            f.write(message_text + '\n')
        return redirect(url_for('index'))
    else:
        return render_template('index.html', show_messages=False)


@app.route('/messages')
def get_messages():
    global messages
    return render_template('index.html', messages=messages, show_messages=True)


if __name__ == '__main__':
    app.run(debug=True)
