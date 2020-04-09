# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    request,
    redirect)
import pickle

# Create path for bra images
bra_folder = os.path.join("static", "images")

# Create app
app = Flask(__name__)

# Configure bra images folder path
app.config["bra_images"] = bra_folder

# Landing page for the form
@app.route("/")
def home_page():
    return render_template("form.html")

# Once user submits inputs, render the recommendation template
@app.route("/send", methods=["GET", "POST"])
def send_data():
    if request.method == "POST":
        attr_list = ["age", "weight", "height", "band_size", "cup_size", "mastectomy_side", "shoulder_pain", "bra_color", "brand", "shoulder_pain", "shoulder_pain", "wired", "molded_foam", "smooth_cup", "lace_details", "active", "lace_insert", "front_back", "reach_back", "embroidery", "jacquard"]     
        user_sub = []

        # Create for loop to obtain user inputs and append results to the user_sub list
        for i in attr_list:
            attr = int(request.form[i])
            user_sub.append(attr)

        # To use the decision tree model, input has to be in [[]] format
        style_pred = [user_sub]

        # Load the model and obtain prediction
        dec_tree_model = open("decision_tree_model.sav", "rb")
        tree_model = pickle.load(dec_tree_model)
        recommendation = tree_model.predict(style_pred)
        bra_recommendation = recommendation[0]

        # Create file name for the image that matches with the bra style result
        bra_image_jpg = f"{bra_recommendation}.JPG"
        bra_image = os.path.join(app.config["bra_images"], bra_image_jpg)

        # Render the recommendation with the results obtained above
        return render_template("recommendation.html", bra_style=bra_recommendation, bra_image_path=bra_image)

if __name__ == "__main__":
    app.run(debug=True)
