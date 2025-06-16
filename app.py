from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)

yield_data = {
    "acres": {
        "corn":8,
        "wheat": 3,
        "potatoes":25
    },
    "hectares": {
        "corn": 20,
        "wheat": 7.5,
        "potatoes": 60
    }
}

@app.route('/', methods = ["GET", "POST"])
def index():
    result = ""
    field_size = ""
    unit = ""
    crop = ""

    if request.method == "POST":
        field_size = request.form.get('Field_Size')
        unit = request.form.get("units")
        crop = request.form.get('crop')
        print(field_size, unit)
        if not field_size or not unit or not crop   :
            result = "Please fill in all fields."
        try:
            field_size_value = float(field_size)
            result = yield_data[unit][crop] * field_size_value
        except (ValueError, KeyError, TypeError):
            result = "Invalid input"

    return render_template('index.html', result = result, field_size = field_size, unit = unit, crop = crop)

if __name__ == '__main__':
    app.run(debug = True)
