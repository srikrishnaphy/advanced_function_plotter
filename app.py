import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

st.set_page_config(page_title="Advanced Function Plotter")

st.title("General Function Plotter")

st.markdown("""
This tool lets you input **any expression involving x and y**, such as:
- `y = sin(x)`
- `y^2 = sin(x)`
- `y = sqrt(x^2 + 1)`
- `y^3 - y = x`
""")

expr_input = st.text_input("Enter your equation (use `x` and `y`) :", "y^2 = sin(x)")

x_min = st.number_input("x min", value=-10.0)
x_max = st.number_input("x max", value=10.0)
x_vals = np.linspace(x_min, x_max, 1000)

# Ensure valid range
if x_min >= x_max:
    st.error("x min must be less than x max.")
else:
    try:
        # If user entered equation with '=', convert to LHS - RHS = 0 form
        if "=" in expr_input:
            lhs_str, rhs_str = expr_input.split("=")
            expr_input = f"({lhs_str}) - ({rhs_str})"
        x, y = sp.symbols('x y')
        # Parse the equation
        eq = sp.sympify(expr_input)

        # Rearranged equation for solving y
        sol_y = sp.solve(eq, y)

        if not sol_y:
            st.warning("Couldn't solve the equation for y.")
        else:
            fig, ax = plt.subplots()

            for sol in sol_y:
                # Create a numerical function from symbolic expression
                f_lambdified = sp.lambdify(x, sol, modules=["numpy"])

                try:
                    y_vals = f_lambdified(x_vals)
                    y_vals = np.real_if_close(y_vals)
                    # Mask complex or NaN values
                    y_vals = np.where(np.isreal(y_vals), y_vals, np.nan)
                    ax.plot(x_vals, y_vals, label=f"y = {sp.pretty(sol)}")
                except Exception as e:
                    st.warning(f"Could not evaluate expression: {sol}")

            ax.set_title(f"Plot of: {expr_input}")
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.grid(True)
            ax.legend()
            st.pyplot(fig)

    except Exception as e:
        st.error(f"Invalid input or parsing error: {e}")
