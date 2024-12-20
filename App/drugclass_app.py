import gradio as gr
import skops.io as sio

unknown_types = sio.get_untrusted_types(file="Model/drug_pipeline.skops")
#print(unknown_types)
model=sio.load("Model/drug_pipeline.skops", trusted=unknown_types)

def predict_drug(age, sex, blood_pressure, cholesterol, na_to_k_ratio):
    """Predict drugs based on patient features.
    Args:
        age (int): Age of patient
        sex (str): Sex of patient 
        blood_pressure (str): Blood pressure level
        cholesterol (str): Cholesterol level
        na_to_k_ratio (float): Ratio of sodium to potassium in blood"""
    
    features = [age, sex, blood_pressure, cholesterol, na_to_k_ratio]
    predicted_drug = model.predict([features])[0]

    label = f"Predicted Drug: {predicted_drug}"
    return label

inputs = [
    gr.Slider(16, 74, step=1, label="Age"),
    gr.Radio(["M", "F"], label="Sex"),
    gr.Radio(["HIGH", "LOW", "NORMAL"], label="Blood Pressure"),
    gr.Radio(["HIGH", "NORMAL"], label="Cholesterol"),
    gr.Slider(6.2, 38.2, step=0.1, label="Na_to_K"),
]
outputs = [gr.Label(num_top_classes=5)]

examples = [
    [25, "M","LOW", "NORMAL" , 25.4],
    [35, "F", "HIGH", "NORMAL", 9],
    [55, "M", "HIGH", "HIGH", 24],

]

title = "Drug Classification Model"
description = "Enter the details to correctly identify Drug type?"
article = "This app is for CTCD_for_Machine_Learning_Models."

gr.Interface(
    fn=predict_drug,
    inputs=inputs,
    outputs=outputs,
    examples=examples,
    title=title,
    description=description,
    article=article,
    theme=gr.themes.Citrus(),
).launch()



    

