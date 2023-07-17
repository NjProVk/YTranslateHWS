from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin
from hws import translate

import logging


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/translate', methods=['POST'])
@cross_origin()
def get_translate():
    data = request.get_json()
    text_for_translate = data.get('text')
    from_language = data.get('language')
    result = []

    text_for_translate = text_for_translate.split('\n')

    for is_text in text_for_translate:
        if is_text:
            result.append(translate(is_text, from_language)[0])
            continue
        result.append('')

    answer = '\n'.join(result)

    return jsonify({'status': 'success', 'value': answer}), 200


if __name__ == '__main__':
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run(host='localhost', port=8894)
