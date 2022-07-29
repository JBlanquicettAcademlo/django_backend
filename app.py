from flask import Flask, request
from flask_api import status

app = Flask(__name__)

@app.route('/counter_common_word')
def counter_common_word():

    word = request.args.get('word')

    custom_file = open("msg.txt", "r")
    readable_file = custom_file.read()
    readable_file_lower = readable_file.lower()
    counter = readable_file_lower.count(word)

    return {'counter': counter}, status.HTTP_200_OK

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000, debug=True)
 