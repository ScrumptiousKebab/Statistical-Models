import numpy as np
import sympy as sp
from tkinter import *
from PIL import Image, ImageTk

# Function to generate the fractal
def generate_fractal(grid_size, num_iter, poly_str, deriv_str):
    # Parse the function and its derivative
    z = sp.symbols('z')
    func = sp.lambdify(z, sp.sympify(poly_str), "numpy")
    func_deriv = sp.lambdify(z, sp.sympify(deriv_str), "numpy")

    re, im_vals = np.linspace(-2, 2, grid_size), np.linspace(-2, 2, grid_size)
    X, Y = np.meshgrid(re, im_vals)
    Z = X + 1j * Y

    roots = np.roots([float(c) for c in sp.Poly(sp.sympify(poly_str), domain='RR').all_coeffs()])
    root_colors = np.linspace(0, 1, len(roots))

    output = np.zeros_like(Z, dtype=float)

    for i in range(num_iter):
        Z = Z - func(Z) / func_deriv(Z)

    for i, root in enumerate(roots):
        output += np.isclose(Z, root) * root_colors[i]

    return output

# Function to update fractal image
def update_fractal():
    grid_size = int(grid_size_slider.get())
    num_iter = int(num_iter_slider.get())
    poly_str = polynomial_entry.get()
    deriv_str = derivative_entry.get()
    fractal_data = generate_fractal(grid_size, num_iter, poly_str, deriv_str)
    img = Image.fromarray(np.uint8(plt.cm.hsv(fractal_data)*255))
    img = ImageTk.PhotoImage(image=img)
    label.config(image=img)
    label.image = img

# Tkinter setup
root = Tk()
root.title("Newtonian Fractal Generator")

frame = Frame(root)
frame.pack(pady=20)

grid_size_slider = Scale(frame, from_=100, to=1000, orient=HORIZONTAL, label="Grid Size")
grid_size_slider.set(500)
grid_size_slider.grid(row=0, column=0)

num_iter_slider = Scale(frame, from_=5, to=100, orient=HORIZONTAL, label="Num of Iterations")
num_iter_slider.set(20)
num_iter_slider.grid(row=0, column=1)

polynomial_entry = Entry(frame, width=20)
polynomial_entry.insert(0, "z**3 - 1")
polynomial_entry.grid(row=0, column=2)

derivative_entry = Entry(frame, width=20)
derivative_entry.insert(0, "3 * z**2")
derivative_entry.grid(row=0, column=3)

button = Button(frame, text="Update Fractal", command=update_fractal)
button.grid(row=0, column=4)

# Display an initial fractal
initial_fractal = generate_fractal(500, 20, "z**3 - 1", "3 * z**2")
initial_img = Image.fromarray(np.uint8(plt.cm.hsv(initial_fractal)*255))
initial_img = ImageTk.PhotoImage(image=initial_img)

label = Label(root, image=initial_img)
label.pack()

root.mainloop()
