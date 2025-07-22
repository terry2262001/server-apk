from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/update', methods=['GET'])
def update_info():
    response = {
        "versionName": "1.0.11",
        "versionCode": "20241203211",
        "apkUrl": "https://iptv.ipbasevn.com/android_apk/demo/lachateau/update-apk/lachateau-v1.0.5a11.apk",
        "forceUpdate": True
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
