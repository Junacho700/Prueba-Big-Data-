from flask import Flask, jsonify
import boto3

app = Flask(__name__)

@app.route('/buckets', methods=['GET'])
def get_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    return jsonify(buckets=buckets)

if __name__ == '__main__':
    app.run(port="5000", host='0.0.0.0',debug=True)

