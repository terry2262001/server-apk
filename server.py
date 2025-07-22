from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Biến lưu thông tin update (global)
update_data = {
    "versionName": "1.0.11",
    "versionCode": "20241203211",
    "apkUrl": "https://iptv.ipbasevn.com/android_apk/demo/lachateau/update-apk/lachateau-v1.0.5a11.apk",
    "forceUpdate": True
}

@app.route('/update', methods=['GET'])
def get_update_info():
    return jsonify(update_data)

@app.route('/update', methods=['POST'])
def set_update_info():
    global update_data
    data = request.get_json()
    
    # Validate đầu vào đơn giản (có thể mở rộng nếu cần)
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    required_keys = ["versionName", "versionCode", "apkUrl", "forceUpdate"]
    if not all(key in data for key in required_keys):
        return jsonify({"error": "Missing required fields"}), 400

    update_data = data
    return jsonify({"message": "Update info set successfully", "data": update_data}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000)) 
    app.run(debug=True, host='0.0.0.0', port=port)
