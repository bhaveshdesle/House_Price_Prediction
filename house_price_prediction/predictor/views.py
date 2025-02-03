from django.shortcuts import render
import pickle
import numpy as np
from .forms import HousePriceForm

with open("predictor/model.pkl", "rb") as file:
    model = pickle.load(file)

def predict_price(request):
    prediction = None
    error = None

    if request.method == "POST":
        form = HousePriceForm(request.POST)
        if form.is_valid():
            try:
                features = np.array([
                    form.cleaned_data["bedrooms"],
                    form.cleaned_data["bathrooms"],
                    form.cleaned_data["sqft_living"],
                    form.cleaned_data["sqft_lot"],
                    form.cleaned_data["floors"]
                ]).reshape(1, -1)

                #predict
                prediction = model.predict(features)[0]
                prediction = round(prediction, 2)
            except Exception as e:
                error = "Error processing input: " + str(e)
        else:
            error = "Invalid form input"
    else:
        form = HousePriceForm()

    return render(request, "predictor/index.html", {"form": form, "prediction": prediction, "error": error})
