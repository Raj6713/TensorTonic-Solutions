def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    for _ in range(steps):
        x = x0 - lr*grad(a, b,x0)
        x0=x
    return x

def grad(a, b, x):
    return 2*a*x+b