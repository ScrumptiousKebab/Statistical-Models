import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import widgets, Output
from IPython.display import display, clear_output
from matplotlib.patches import Wedge
import time

output = Output()

def plot_roulette_wheel(angle_offset, spin_result=None):
    labels = ['0', '32', '15', '19', '4', '21', '2', '25', '17', '34', '6', '27', '13', '36', '11', '30', '8', '23', '10', '5', '24', '16', '33', '1', '20', '14', '31', '9', '22', '18', '29', '7', '28', '12', '35', '3', '26']
    colors = ['green'] + ['red', 'black'] * 18

    fig, ax = plt.subplots(figsize=(10, 10))

    for i, (label, color) in enumerate(zip(labels, colors)):
        angle = 360 / len(labels)
        theta1 = angle * i + angle_offset
        theta2 = angle * (i + 1) + angle_offset
        wedge = Wedge(center=(0.5, 0.5), r=0.4, theta1=theta1, theta2=theta2, facecolor=color)
        ax.add_artist(wedge)

        angle_text = np.radians(i * 10 + angle_offset)
        x = 0.5 + 0.35 * np.cos(angle_text)
        y = 0.5 + 0.35 * np.sin(angle_text)
        ax.text(x, y, label, ha='center', va='center', fontsize=12, color='white')

    if spin_result is not None:
        ax.text(0.5, 0.5, str(spin_result), ha='center', va='center', fontsize=36, color='gold')

    ax.set_aspect('equal', 'box')
    plt.axis('off')
    plt.show()

def spin_roulette(btn):
    result = np.random.choice(['0', '32', '15', '19', '4', '21', '2', '25', '17', '34', '6', '27', '13', '36', '11', '30', '8', '23', '10', '5', '24', '16', '33', '1', '20', '14', '31', '9', '22', '18', '29', '7', '28', '12', '35', '3', '26'])
    
    total_frames = 50
    for frame in range(total_frames):
        with output:
            clear_output(wait=True)
            plot_roulette_wheel(frame * (360 / total_frames))
            time.sleep(0.05)  # pause for a short time to allow the frame to be displayed
    
    with output:
        clear_output(wait=True)
        plot_roulette_wheel(0, result)

# Create a button for spinning the Roulette
spin_button = widgets.Button(description='Spin Roulette')
spin_button.on_click(spin_roulette)

display(spin_button, output)
