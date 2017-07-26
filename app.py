from flask import Flask
import my_json_formatter
import json
from collections import OrderedDict

app = Flask(__name__)

@app.route('/')
def hello():
    with open("show_list",'r') as file:
        data = json.load(file, object_pairs_hook=OrderedDict)

    formatted = my_json_formatter.format_data(data)

    return formatted

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)