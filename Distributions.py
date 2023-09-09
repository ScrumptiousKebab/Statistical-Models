import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, poisson, binom
from ipywidgets import interact, FloatSlider, IntSlider, Dropdown

def plot_distribution(distribution, mean=0, std_dev=1, lambda_param=5, n=10, p=0.5):
    plt.figure(figsize=(10, 6))
    plt.grid(True)
    
    if distribution == 'Normal':
        x = np.linspace(-10, 10, 1000)
        y = norm.pdf(x, mean, std_dev)
        plt.plot(x, y)
        plt.xlabel("x")
        plt.ylabel("Probability Density")
        p1 = norm.cdf(0, mean, std_dev)
        p2 = 1 - norm.cdf(0, mean, std_dev)
        print(f"P(X < 0): {p1:.4f}")
        print(f"P(X > 0): {p2:.4f}")

    elif distribution == 'Poisson':
        x = np.arange(0, 20)
        y = poisson.pmf(x, lambda_param)
        plt.stem(x, y)
        plt.xlabel("Number of Events")
        plt.ylabel("Probability")
        p1 = poisson.cdf(5, lambda_param)
        print(f"P(X <= 5): {p1:.4f}")
    
    elif distribution == 'Binomial':
        x = np.arange(0, n+1)
        y = binom.pmf(x, n, p)
        plt.stem(x, y)
        plt.xlabel("Number of Successes")
        plt.ylabel("Probability")
        p1 = binom.cdf(5, n, p)
        print(f"P(X <= 5): {p1:.4f}")
        
    plt.title(f"{distribution} Distribution")
    plt.show()

interact(
    plot_distribution,
    distribution=Dropdown(options=['Normal', 'Poisson', 'Binomial'], description='Distribution:'),
    mean=FloatSlider(min=-5, max=5, step=0.1, description='Mean:'),
    std_dev=FloatSlider(min=0.1, max=5, step=0.1, description='Std Dev:'),
    lambda_param=FloatSlider(min=0.1, max=20, step=0.1, description='Lambda:'),
    n=IntSlider(min=1, max=50, step=1, description='n:'),
    p=FloatSlider(min=0, max=1, step=0.01, description='p:')
);
