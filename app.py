import streamlit as st
from PIL import Image, ImageStat

st.set_page_config(page_title="Fuji Recipe Engineer v2.0", layout="centered")

st.title("📸 Fujifilm Reçete Mühendisi v2.0")
st.write("Analiz derinleştirildi: Beyaz Dengesi ve Gerçek Pozlama değerleri eklendi.")

uploaded_file = st.file_uploader("Bir fotoğraf yükle...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Analiz Edilen Fotoğraf", use_container_width=True)
    
    # --- GELİŞMİŞ ANALİZ MOTORU ---
    stat = ImageStat.Stat(img)
    r, g, b = stat.mean
    brightness = (r + g + b) / 3
    
    st.divider()
    st.subheader("🎯 Profesyonel Reçete Kartı")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 1. Simülasyon Kararı
        if r > b + 10: # Sıcak/Kırmızı tonlar baskınsa
            sim = "Classic Negative"
            sub_text = "Nostaljik ve sert kontrastlı tonlar."
        elif b > g: # Maviler baskınsa
            sim = "Classic Chrome"
            sub_text = "Belgesel tadında, soluk ve sinematik."
        else:
            sim = "Provia/Standard"
            sub_text = "Doğal ve dengeli renkler."
            
        st.metric("Film Simulation", sim)
        st.caption(f"💡 {sub_text}")

        # 2. Beyaz Dengesi (WB Shift) - YENİ!
        # Fotoğraftaki renk sapmasını ölçüp tersine veya destekleyici ayar verir
        wb_r = int((r - 128) / 20)
        wb_b = int((128 - b) / 20)
        st.metric("WB Shift", f"R: {wb_r}, B: {wb_b}")
        st.caption("💡 Fotoğrafın renk sıcaklığını eşlemek için.")

    with col2:
        # 3. Gerçek Pozlama Değerleri (1/3 basamakları) - DÜZELTİLDİ!
        if brightness < 100: ev = "+1.0"
        elif brightness < 130: ev = "+2/3"
        elif brightness < 150: ev = "+1/3"
        else: ev = "0.0"
        
        st.metric("Exposure Comp.", ev)
        st.caption("💡 Makine tekerleğindeki gerçek tık sayısı.")

        st.metric("Dynamic Range", "DR400" if brightness > 130 else "DR100")
        st.caption("💡 Işık patlamalarını engellemek için.")

    # 4. Detaylı Parametre Tablosu
    st.table({
        "Parametre": ["Grain Effect", "Color Chrome Effect", "Highlight", "Shadow", "Color", "Sharpness", "Clarity"],
        "Ayar": ["Strong, Small", "Strong", "-2.0", "-1.0", "+2", "0", "-3.0"],
        "Not": ["Kumlanma dokusu", "Derin renkler", "Yumuşak ışık", "Detaylı gölge", "Canlılık", "Doğal keskinlik", "Dreamy efekt"]
    })
