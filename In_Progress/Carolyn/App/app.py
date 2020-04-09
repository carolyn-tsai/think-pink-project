# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    request,
    redirect)
import pickle
from sklearn import tree

bra_folder = os.path.join("static", "images")

app = Flask(__name__)

app.config["bra_images"] = bra_folder

@app.route("/")
def home_page():
    return render_template("form.html")

@app.route("/send", methods=["GET", "POST"])
def send_data():
    if request.method == "POST":
        attr_list = ["age", "weight", "height", "band_size", "cup_size", "mastectomy_side", "shoulder_pain", "bra_color", "brand", "shoulder_pain", "shoulder_pain", "wired", "molded_foam", "smooth_cup", "lace_details", "active", "lace_insert", "front_back", "reach_back", "embroidery", "jacquard"]     
        user_sub = []
        for i in attr_list:
            attr = int(request.form[i])
            user_sub.append(attr)
        style_pred = [user_sub]
        dec_tree_model = open("decision_tree_model.sav", "rb")
        tree_model = pickle.load(dec_tree_model)
        recommendation = tree_model.predict(style_pred)
        bra_recommendation = recommendation[0]
        bra_image_jpg = f"{bra_recommendation}.JPG"
        bra_image = os.path.join(app.config["bra_images"], bra_image_jpg)
        return render_template("recommendation.html", bra_style=bra_recommendation, bra_image_path=bra_image)

if __name__ == "__main__":
    app.run(debug=True)
