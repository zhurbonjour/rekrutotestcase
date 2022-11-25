from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    context = {}
    if request.values:
        if request.method == 'GET':
            context['name'] = request.values['name']
            context['message'] = request.values['message']
    return render_template('main.html', context=context)


@app.route("/extended", methods=['GET', 'POST'])
def extended():
    context = {}
    if request.method == 'GET':
        if request.values:
            context['name'] = request.values['name']
            context['message'] = request.values['message']
        else:
            context['name'] = "Rekruto"
            context['message'] = "Давай дружить"

    if request.method == 'POST':
        message = request.form['email_message']
        context['name'] = "Rekruto"
        context['message'] = message

    return render_template('extended.html', context=context)


if __name__ == "__main__":
    app.run()
