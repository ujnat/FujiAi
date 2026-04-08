import streamlit as st
from PIL import Image, ImageStat

st.set_page_config(page_title="Fuji Genius v4.0", layout="centered")
st.title("📸 Fujifilm Recipe Engineer v4.0")
st.write("Upgraded: Advanced Simulation Logic & Cinema Tones")

uploaded_file = st.file_uploader("Upload for precise analysis...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, use_container_width=True)
    
    stat = ImageStat.Stat(img)
    r, g, b = stat.mean 
    brightness = (r * 299 + g * 587 + b * 114) / 1000
    
    st.divider()
    st.subheader("🧪 Professional Recipe Card")

    # --- THE PRO LOGIC ---
    # 1. WB SHIFT (More aggressive for that gold/yellow tint)
    wb_r_calc = int((r - b) / 6) + 2
    wb_b_calc = int((b - g) / 8) - 5

    # 2. THE SIMULATION DECISION (REWIRED)
    # If there's a specific balance of Green and Red (Yellowish sky), use Classic Chrome
    if abs(r - g) < 30 and b < r:
        sim = "Classic Chrome"
        notes = "Giving you that cinematic, muted yellow/green vintage look."
    elif r > 160:
        sim = "Astia/Soft"
        notes = "Smooth transitions and vibrant sunlit colors."
    else:
        sim = "Classic Negative"
        notes = "High contrast, moody street photography style."

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Film Simulation", sim)
        st.metric("WB Shift (R, B)", f"R: {wb_r_calc}, B: {wb_b_calc}")

    with col2:
        # Exposure for Analog feel: Usually slightly underexposed or neutral
        ev_val = "-1/3" if brightness > 140 else "0.0"
        st.metric("Exposure Comp.", ev_val)
        st.metric("Dynamic Range", "DR400")

    st.table({
        "Setting": ["Color", "Highlight", "Shadow", "Grain Effect", "Color Chrome Effect", "Sharpness", "Clarity"],
        "Value": ["+3", "-1", "-1", "Strong, Small", "Strong", "-2", "-2"],
        "Reason": ["Vibrant but natural", "Preserve sky detail", "Soft shadows", "Vintage grain", "Deepens warm colors", "Film look", "Dreamy mist"]
    })
