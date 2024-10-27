import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

with ui.sidebar():
    ui.input_slider("n", "N", 0, 100, 20)
    # Adding a dropdown menu to pick the color of bars
    ui.input_select("color", "Choose Bar Color", ["black", "green", "red", "purple", "orange"])

@render.plot(alt="A histogram with optional normal curve")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)

    # Adding background colors
    fig, ax = plt.subplots()
    fig.patch.set_facecolor("#F0EAD6")  # Light cream color for the figure background
    ax.set_facecolor("#E6F2FF")

    
    plt.hist(x, bins=input.n(), color=input.color(), density=True)

