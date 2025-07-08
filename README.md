
# 🧮 Advanced Function Plotter

A lightweight Desmos-style math visualizer built using **Streamlit + SymPy**, capable of plotting **algebraic** and **transcendental equations** (even **multivalued** ones!) involving variables `x` and `y`.

This is a beginner-level but functional prototype for plotting general equations — a fundamental tool for students of math and physics.

> ⚠️ This is an **ongoing project** — the goal is to create a symbolic, web-based math engine with Desmos-like expressiveness using pure Python.

## 🎓 Educational Motivation

This project is a beginner-level but functional prototype for plotting general mathematical expressions — a fundamental tool for students of mathematics and physics. 

It aims to demonstrate:
- How symbolic equations can be interpreted and plotted using Python
- The power of building intuitive tools with minimal code
- The importance of visualizing multivalued and transcendental functions, which are common in physics

This is a humble and early-stage effort, but it captures many core ideas behind symbolic plotting — and offers a foundation for more advanced development in the future.


---

## 🚀 Try it Live

👉 [Open App on Streamlit Cloud](https://brwso3rj5zlnherzg4bhyq.streamlit.app/)

---

## 🧠 What It Can Do

- ✅ Plot equations like `y^2 = sin(x)` or `y^3 = x`
- ✅ Supports multivalued solutions (e.g., ±√x)
- ✅ Handles inverse functions: `arcsin(x)`, `arccos(x)`, `arctan(x)`
- ✅ Accepts logarithms with arbitrary base: `log(x, e)`, `log(x, 2)`
- ✅ Recognizes constants: `pi`, `e`
- ✅ Allows implicit multiplication: `2x`, `(x-1)(x+1)x`
- ✅ Clean interface with syntax help and error handling
- ✅ Deployed to the web using [Streamlit](https://streamlit.io)

---

## 🖼️ Example Expressions

| Input                          | Interprets as...                    |
|-------------------------------|-------------------------------------|
| `y^2 = sin(x)`                | ±√sin(x)                            |
| `y^3 - y = x`                 | Cubic equation in y                |
| `y = log(x, e)`               | Natural logarithm                  |
| `y = sqrt(x^2 + 1)`           | Always real-valued                 |
| `y^2 = arctan(x)*1/x + sin(x^2)` | Complex composite function        |

---

## 🧱 Tech Stack

- **Streamlit** – UI and frontend framework
- **SymPy** – Symbolic math engine for parsing and solving
- **NumPy** – Fast numeric evaluation and array support
- **Matplotlib** – Plotting engine

---

## ⚠️ Current Limitations

- ❌ No automatic handling of removable discontinuities (e.g., `1/x` at `x = 0`)
- ❌ No support for parametric plots or 3D (yet)
- ❌ Discontinuities are shown as plot breaks instead of smoothing
- ❌ No sliders for parameter exploration (planned!)
- ❌ Equation rendering does not yet use LaTeX prettification (coming soon)

---

## 📌 Roadmap / Future Features

- [ ] Improve continuity around singular points (`1/x`, `log(x)`, etc.)
- [ ] Add support for parameter sliders (e.g., `a * sin(bx)`)
- [ ] LaTeX preview of entered expressions
- [ ] Parametric and polar plotting support
- [ ] 3D surface plotting using `plotly`
- [ ] Auto-simplification or step-by-step solving

---

## 💡 Inspiration

This project was inspired by the elegant interface of [Desmos](https://www.desmos.com/calculator) and the desire to understand how symbolic plotting can be built from scratch using Python tools.

---

## 👨‍💻 Author

Built by **Srikrishna Ghosh**, powered by curiosity and a few late nights (with lots of help from ChatGPT).

---

## 📜 License

MIT License — open for educational and personal use.



