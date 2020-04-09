# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    request,
    redirect)
import pickle
from sklearn import tree

# bra_folder = os.path.join("static", "images")

app = Flask(__name__)

# app.config["bra_images"] = bra_folder

@app.route("/")
def home_page():
    return render_template("form.html")

@app.route("/send", methods=["GET", "POST"])
def send_data():
    if request.method == "POST":
        age = int(request.form["age"])
        band_size = int(request.form["band_size"])
        height = int(request.form["height"])
        weight = int(request.form["weight"])
        cup_size = int(request.form["cup_size"])
        bra_color = int(request.form["bra_color"])
        mastectomy_side = int(request.form["mastectomy_side"])
        lace_details = int(request.form["lace_details"])
        shoulder_pain = int(request.form["shoulder_pain"])
        smooth_cup = int(request.form["smooth_cup"])
        molded_foam = int(request.form["molded_foam"])
        wired = int(request.form["wired"])
        lace_insert = int(request.form["lace_insert"])
        front_back = int(request.form["front_back"])
        active = int(request.form["active"])
        reach_back = int(request.form["reach_back"])
        wide_strap = int(request.form["shoulder_pain"])
        padded_strap = int(request.form["shoulder_pain"])
        brand = int(request.form["brand"])
        embroidery = int(request.form["embroidery"])
        jacquard = int(request.form["jacquard"])
        patient_submission = [[age, weight, height, band_size, cup_size, mastectomy_side, shoulder_pain, bra_color, brand, wide_strap, padded_strap, wired, molded_foam, smooth_cup, lace_details, active, lace_insert, front_back, reach_back, embroidery, jacquard]]
        dec_tree_model = open("decision_tree_model.sav", "rb")
        tree_model = pickle.load(dec_tree_model)
        bra_recommendation = tree_model.predict(patient_submission)
        #bra_recommendation = recommendation
        #bra_image_jpg = f'"{bra_recommendation}.jpg"'
        #bra_image_path = os.path.join(app.config["bra_images"], bra_image_jpg)
    return render_template("recommendation.html", variable=bra_recommendation)



if __name__ == "__main__":
    app.run(debug=True)
