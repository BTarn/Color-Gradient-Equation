import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

def main():
    st.title("Color Gradient Equation")

    func_input = st.text_area("Enter function f(x) where x in [0, 1] for (red, green, blue, alpha) as a Python expression:", "(x, x**2, np.sin(x*np.pi), 1)")
    generate_button = st.button("Generate Gradient")
    
    if generate_button:

        try:
            x_vals = np.linspace(0, 1, 256)
            colors = np.array([eval(func_input, {"x": x, "np": np}) for x in x_vals])
            
            fig, ax = plt.subplots(figsize=(8, 2))
            ax.imshow([colors], aspect='auto', extent=[0, 1, 0, 1])
            ax.set_xticks([])
            ax.set_yticks([])
            
            buf = BytesIO()
            plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
            st.image(buf, caption="Generated Gradient", use_container_width=True)
            
        except Exception as e:
            st.error(f"Error in function evaluation: {e}")

if __name__ == "__main__":
    main()
