from flask import Flask
from flask import render_template
import my_json_formatter
import json
from collections import OrderedDict

app = Flask(__name__)

@app.route('/')
def hello():
    with open("show_list",'r') as file:
        data = json.load(file, object_pairs_hook=OrderedDict)

    formatted = my_json_formatter.format_data(data)
    with open("templates/show.html",'w') as file:
        file.write(formatted)

    return render_template('show.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)