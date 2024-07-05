from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


students = [
    "0, 'Doe, Jane', 'jane.doe@utsouthwestern.edu', 1280244",
    "1, 'Smith, John', 'john.smith@utsouthwestern.edu', 1280245",
    "2, 'Brown, Mike', 'mike.brown@utsouthwestern.edu', 1280246"
]

@app.route('/')
def index():
    return render_template('index.html', students=students)

@app.route('/search')
def search():
    return render_template('search.html', students=students)

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('q')
    results = [student for student in students if search.lower() in student.lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
