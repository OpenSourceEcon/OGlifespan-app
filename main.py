import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the pickled function
pkl_func_path = (
    "/Users/richardevans/Docs/Economics/OSE/OG/OGlifespan-app/" +
    "interp_rbf_OGlifesense.pkl"
)
with open(pkl_func_path, 'rb') as f:
    interp_func = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        slider1_value = request.form["slider1"]
        slider2_value = request.form["slider2"]
        slider3_value = request.form["slider3"]
        slider4_value = request.form["slider4"]
        slider5_value = request.form["slider5"]
        slider6_value = request.form["slider6"]
        slider7_value = request.form["slider7"]
        input_array = np.array(
            [
                [
                    slider1_value, slider2_value, slider3_value,
                    slider4_value, slider5_value, slider6_value,
                    slider7_value
                ]
            ]
        )
        result_vec = interp_func(input_array)[0]
        pop_diffs_2045_2065 = result_vec[0]
        pop_diffs_2025_2100 = result_vec[1]
        pop_diffs_2050 = result_vec[2]
        avg_diff = result_vec[3]
        avg_gdp_pc_diff = result_vec[4]
        NPV = result_vec[5]
        return render_template("index.html", result=NPV)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
