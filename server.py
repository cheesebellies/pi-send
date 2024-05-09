from flask import Flask, send_file

app = Flask('FileTransfer')

@app.route('/<path:path>')
def sendf(path):
  return send_file(path)

app.run(host='0.0.0.0', port=25565)
