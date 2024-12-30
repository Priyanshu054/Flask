from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "<html><h1>This is a simple Flask app!</h1></html>"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])   # Allow both GET and POST requests
def form():
    return render_template('form.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']   # Get the value of the 'name' key
        return f"Hello, {name}!"
    return render_template('form.html')

# variable rule
@app.route('/rating/<int:rate>') # takes only int value
def rating(rate):
    return f"Rating: {rate}"
    # return "Rating: " + str(rate)

@app.route('/score/<int:marks>')
def score(marks):
    result = 'Pass' if marks > 50 else 'Fail'
    return render_template('result.html', result=result)  # Pass the data to the template as keyword arguments

@app.route('/getMarks', methods=['GET', 'POST'])
def getresult():
    if request.method == 'POST':   # If the form is submitted
        hindi = int(request.form['hindi'])
        english = int(request.form['english'])
        maths = int(request.form['maths'])
        total = (hindi + english + maths) // 3
    else:   # if the form is not submitted
        return render_template('getMarks.html')
    return redirect(url_for('score', marks=total))


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
