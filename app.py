import streamlit as st
from PIL import Image, ImageStat

# Sayfa Ayarları
st.set_page_config(page_title="Fuji Recipe AI", layout="centered")

st.title("📸 Fujifilm Reçete Mühendisi")
st.write("Fotoğrafını yükle, kameran için **en yakın** ayarları al.")

# Dosya Yükleme
uploaded_file = st.file_uploader("Bir fotoğraf seç veya sürükle", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Analiz Edilen Fotoğraf", use_container_width=True)
    
    # --- ANALİZ MOTORU ---
    stat = ImageStat.Stat(img)
    rgb_means = stat.mean
    brightness = sum(rgb_means) / 3
    
    st.divider()
    st.subheader("🎯 Önerilen Reçete Kartı")
    
    # Karar Mekanizması (Senin istediğin hassasiyette geliştirildi)
    col1, col2 = st.columns(2)
    
    with col1:
        # Film Simülasyonu Kararı
        if rgb_means[0] > rgb_means[2]: # Kırmızılar baskınsa
            sim = "Classic Negative"
            desc = "Sıcak ve nostaljik tonlar algılandı."
        else:
            sim = "Classic Chrome"
            desc = "Belirgin maviler ve sinematik solukluk algılandı."
            
        st.metric("Film Simulation", sim)
        st.caption(f"💡 {desc}")

        # Clarity (Netlik) Kararı
        clarity = "-3.0" if brightness > 120 else "0"
        st.metric("Clarity", clarity)
        st.caption("💡 Yumuşak analog dokusu için.")

    with col2:
        # Pozlama ve DR Kararı
        ev = "+0.7" if brightness < 150 else "0.0"
        dr = "DR400" if brightness > 130 else "DR100"
        
        st.metric("Exposure Comp.", ev)
        st.metric("Dynamic Range", dr)
        st.caption("💡 Parlak alanları korumak için.")

    # Detaylı Tablo
    st.table({
        "Ayar": ["Highlight", "Shadow", "Color", "Sharpness", "Noise Red."],
        "Değer": ["-2.0", "-1.0", "-2", "-1", "-4"],
        "Neden": ["Parlaklığı yumuşatmak", "Gölgeleri açmak", "Film solukluğu", "Doğallık", "Gren koruma"]
    })
