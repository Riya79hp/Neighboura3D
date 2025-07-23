from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson import ObjectId
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
from io import BytesIO
import os
from flask import send_file
from selenium import webdriver

app = Flask(__name__)
CORS(app)


# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/shopDB"
mongo = PyMongo(app)
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__),'Front-end','my-3d-scene', 'src', 'img')
def seed_data():
    shops_collection = mongo.db.shops
    if shops_collection.count_documents({}) == 0:
        shops = [
            {
                "name": "Veggie Mart",
                "position": {"x": -6, "z": -20},
                "hours": "9:00 AM - 9:00 PM"
            },
            {
                "name": "Yoko’s Ramen",
                "position": {"x": 6, "z": 20},
                "hours": "10:00 AM - 10:00 PM"
            },
            {
                "name": "Baker’s Den",
                "position": {"x": -6, "z": 40},
                "hours": "7:00 AM - 8:00 PM"
            },
            {
                "name": "Café Bliss",
                "position": {"x": 6, "z": 60},
                "hours": "8:00 AM - 9:00 PM"
            }
        ]
        shops_collection.insert_many(shops)
     # MG Road shops collection
    mg_road_shops_collection = mongo.db.mgroad_shops
    if mg_road_shops_collection.count_documents({}) == 0:
        mg_shops = [
            {"name": "Palace de versailles", "position": {"x": -6, "z": -30}, "hours": "9:00 AM - 8:00 PM"},
            {"name": "MoviePlex", "position": {"x": 6, "z": 30}, "hours": "11:00 AM - 9:00 PM"},
                   ]
        mg_road_shops_collection.insert_many(mg_shops)
# Initial shop data
@app.route('/shops', methods=['GET'])
def get_shops():
    shops_collection = mongo.db.shops
    shops = []
    for shop in shops_collection.find():
        shops.append({
            "id": str(shop['_id']),
            "name": shop['name'],
            "hours": shop['hours'],
            "position": shop['position']
        })
        print(shops)
    return jsonify(shops)

@app.route('/update_shop', methods=['POST'])
def update_shop():
    data = request.json
    shop_id = data['id']
    update_fields = {}

    if 'name' in data:
        update_fields['name'] = data['name']
    if 'hours' in data:
        update_fields['hours'] = data['hours']

    shops_collection = mongo.db.shops
    shops_collection.update_one(
        {'_id': ObjectId(shop_id)},
        {'$set': update_fields}
    )

    return jsonify({"message": "Shop updated successfully!"})
def take_screenshot():
    try:
        # Use modern headless mode that supports full screenshots
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,3000")
        options.add_argument("--force-device-scale-factor=1")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("https://www.bseindia.com/sensex/code/16/")

        WebDriverWait(driver, 20).until(
            lambda d: d.find_element(By.CSS_SELECTOR, '.heatamaparea.largetable')
        )

        main_div2 = driver.find_element(By.CSS_SELECTOR, '.heatamaparea.largetable')
        driver.execute_script("arguments[0].scrollIntoView(true);", main_div2)

        import time
        time.sleep(2)

        os.makedirs('static/screenshots', exist_ok=True)
        screenshot_path = "static/screenshots/main_div_screenshot2.png"
        main_div2.screenshot(screenshot_path)

        driver.quit()

        print("Screenshot taken successfully!")  # ✅ Just print here

    except Exception as e:
        print("Error taking screenshot:", str(e))  # ✅ Print instead of jsonify
@app.route('/mgroad_shops', methods=['GET'])
def get_mgroad_shops():
    shops_collection = mongo.db.mgroad_shops
    shops = []
    for shop in shops_collection.find():
        shops.append({
            "id": str(shop['_id']),
            "name": shop['name'],
            "hours": shop['hours'],
            "position": shop['position']
        })
    return jsonify(shops)
@app.route('/update_mgroad_shop', methods=['POST'])
def update_mgroad_shop():
    data = request.json
    shop_id = data['id']
    update_fields = {}

    if 'name' in data:
        update_fields['name'] = data['name']
    if 'hours' in data:
        update_fields['hours'] = data['hours']

    shops_collection = mongo.db.mgroad_shops
    shops_collection.update_one(
        {'_id': ObjectId(shop_id)},
        {'$set': update_fields}
    )

    return jsonify({"message": "MG Road Shop updated successfully!"})

@app.route('/replace-image', methods=['POST'])
def replace_image():
    file = request.files.get('image')
    filename = request.form.get('filename')

    if file and filename:
        save_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(save_path)
        return jsonify({"message": "Image replaced", "updatedPath": f"/static/img/{filename}"})
    return jsonify({"error": "Missing file or filename"}), 400

if __name__ == "__main__":
    seed_data()  # Manually seed when starting the app
    take_screenshot()
    app.run(debug=True, port=5000)
