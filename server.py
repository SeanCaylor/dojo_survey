from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return "I'm afraid I can't let you do that, Star Fox"

@app.route('/')
def dojo_survey():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def survey_result():
    name = request.form['name']
    location = request.form['dojo_loc']
    stack = request.form['fav_stack']
    earned = request.form['belt_earned']
    comments = request.form['comments']
    print(earned)
    return render_template('result.html', name = name, location = location, stack = stack, earned = earned, comments = comments)

if __name__ == "__main__":
    app.run(debug = True)