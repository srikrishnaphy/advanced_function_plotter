import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import E, pi

from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor,
)

local_dict = {
    'e': E,
    'pi': pi,
}

# When parsing:
eq = parse_expr(expr_input, local_dict=local_dict, transformations=transformations)

#This lets users write:  log(x, e) for natural log  or sin(pi/2) etc.


st.set_page_config(page_title="Advanced Function Plotter")

st.title("General Function Plotter")

with st.expander("📘 Function Syntax Help (click to expand)"):
    st.markdown("""
### ✅ Supported Syntax Examples

| What you mean | What to type |
|---------------|--------------|
| Natural log | `log(x)` or `log(x, e)` |
| Base-10 log | `log(x, 10)` or `log10(x)` |
| Square root | `sqrt(x)` |
| Reciprocal | `1/x` |
| Inverse sine | `arcsin(x)` |
| Inverse cosine | `arccos(x)` |
| Inverse tangent | `arctan(x)` |
| Exponentiation | `x^2` or `x**2` |
| Implicit multiplication | `2x` or `(x-1)(x+1)x` |
| Multivalued root | `y^2 = x` for ±√x |
| Use constants | `pi`, `e` |

---

### 💡 Notes:
- `log(x, a)` gives log base `a` — e.g. `log(x, 2)` is log base 2.
- Use `log(x, e)` for natural logarithm (`ln(x)`).
- `e` ≈ 2.718 and `pi` ≈ 3.141 are recognized symbols.

---

### ❌ Not Supported (yet)

| Invalid | Instead use |
|---------|--------------|
| `ln(x)` | `log(x)` or `log(x, e)` |
| `sin⁻¹(x)` | `arcsin(x)` |
| `π` or `ℯ` | Use `pi` or `e` |

💡 *Hint*: To get both branches of a multivalued function like `±√x`, write `y^2 = x` instead of `y = sqrt(x)`.
""")


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
