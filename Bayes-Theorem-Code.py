import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interact, FloatSlider

def bayes_theorem(p_b_given_a, p_a, p_b):
    p_a_given_b = (p_b_given_a * p_a) / p_b
    return p_a_given_b

def plot_bayes(p_a=0.01, p_b_given_a=0.99, p_b=0.1):
    p_b_values = np.linspace(0.01, 0.2, 100)
    p_a_given_b_values = [bayes_theorem(p_b_given_a, p_a, p_b_val) for p_b_val in p_b_values]
    
    plt.figure(figsize=(10, 6))
    plt.plot(p_b_values, p_a_given_b_values, marker='o')
    plt.title('Effect of varying $P(B)$ on $P(A|B)$')
    plt.xlabel('$P(B)$')
    plt.ylabel('$P(A|B)$')
    plt.grid(True)
    plt.show()
    return None  # Explicitly return None to prevent function signature from showing

# Sliders
p_a_slider = FloatSlider(min=0.001, max=0.2, step=0.001, value=0.01, description='$P(A)$')
p_b_given_a_slider = FloatSlider(min=0.5, max=1, step=0.01, value=0.99, description='$P(B|A)$')
p_b_slider = FloatSlider(min=0.01, max=0.2, step=0.01, value=0.1, description='$P(B)$')

# Interactive plot
interact(plot_bayes, p_a=p_a_slider, p_b_given_a=p_b_given_a_slider, p_b=p_b_slider);
