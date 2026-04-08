import streamlit as st
from PIL import Image, ImageStat

st.set_page_config(page_title="Fuji Genius v3.0", layout="centered")
st.title("📸 Fujifilm Recipe Engineer v3.0")
st.write("Deep color analysis enabled. Results are now in English.")

uploaded_file = st.file_uploader("Upload a photo for analysis...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, use_container_width=True)
    
    # --- ADVANCED COLOR & LIGHT ANALYSIS ---
    stat = ImageStat.Stat(img)
    r, g, b = stat.mean 
    brightness = (r * 299 + g * 587 + b * 114) / 1000
    
    st.divider()
    st.subheader("🧪 Engineered Recipe Card")

    # --- LOGIC ENGINE ---
    # 1. WB SHIFT (Based on color dominance)
    wb_r_calc = int((r - g) / 8) + 3  # Pushing Red further for warmth
    wb_b_calc = int((b - g) / 10) - 4 # Pulling Blue down

    # 2. FILM SIMULATION SELECTION
    if r > 140 and g > 120: 
        sim = "Classic Negative"
        notes = "Perfect for that nostalgic, high-contrast look."
    elif b > 130:
        sim = "Classic Chrome"
        notes = "Ideal for cinematic blues and documentary style."
    else:
        sim = "Astia/Soft"
        notes = "Best for soft skin tones and natural light."

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Film Simulation", sim)
        st.metric("WB Shift (R, B)", f"R: {wb_r_calc}, B: {wb_b_calc}")
        st.caption(f"💡 {notes}")

    with col2:
        # Better Exposure Logic
        ev_val = "-2/3" if brightness > 155 else "0.0"
        st.metric("Exposure Comp.", ev_val)
        st.metric("Dynamic Range", "DR400")

    # 3. UPDATED PARAMETER TABLE (Aggressive Color)
    st.table({
        "Setting": ["Color", "Highlight", "Shadow", "Grain Effect", "Color Chrome Effect", "Sharpness", "Clarity"],
        "Value": ["+4", "-2", "0", "Strong, Small", "Strong", "-2", "-2"],
        "Reason": ["Vibrant analog soul", "Soft highlights", "Natural shadows", "Film texture", "Deep tones", "Analog softness", "Dreamy look"]
    })
