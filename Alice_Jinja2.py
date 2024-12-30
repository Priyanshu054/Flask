from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Data to pass to the template
    data = {
        "name": "Alice",
        "place": "Wonderland",
        "items": ["Tea", "Cake", "Mushroom"]
    }
    return render_template('template.html', **data)  # Pass the data to the template as keyword arguments
    # return render_template('template.html', name='Alice', place="Wonderland", items=["Tea", "Cake", "Mushroom"])  # Pass the data to the template as keyword arguments

if __name__ == '__main__':
    app.run(debug=True)
