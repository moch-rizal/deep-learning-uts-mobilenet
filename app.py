import streamlit as st
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import numpy as np

st.set_page_config(page_title="Image Classification", layout="centered")

@st.cache_resource
def get_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # Inisialisasi arsitektur MobileNetV2
    model = models.mobilenet_v2(weights=None)
    model.classifier = nn.Sequential(
        nn.Dropout(0.2),
        nn.Linear(model.classifier[1].in_features, 2)
    )
    
    # Load weights dari file lokal
    try:
        model_path = "model_anjingkucing_mobilenet.pt"
        state_dict = torch.load(model_path, map_location=device)
        model.load_state_dict(state_dict)
    except Exception as e:
        st.error(f"Gagal memuat model: {e}")
        return None
        
    model.to(device)
    model.eval()
    return model

def transform_image(img):
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    return preprocess(img).unsqueeze(0)

def main():
    st.title("Klasifikasi Citra: Anjing vs Kucing")
    st.write("Implementasi MobileNet untuk UAS Deep Learning")
    
    model = get_model()
    if not model:
        return

    uploaded_file = st.file_uploader("Upload Citra", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        col1, col2 = st.columns(2)
        
        with col1:
            st.image(image, caption='Citra Input', use_container_width=True)
            
        with col2:
            if st.button('Proses Klasifikasi'):
                # Preprocessing
                tensor = transform_image(image)
                device = next(model.parameters()).device
                tensor = tensor.to(device)
                
                # Inference
                with torch.no_grad():
                    output = model(tensor)
                    probabilities = torch.nn.functional.softmax(output, dim=1)[0]
                    confidence, idx = torch.max(probabilities, 0)
                
                labels = ['Anjing', 'Kucing'] 
                result = labels[idx.item()]
                
                st.subheader(f"Hasil: {result}")
                st.write(f"Confidence: {confidence.item()*100:.2f}%")
                st.progress(int(confidence.item() * 100))

if __name__ == "__main__":
    main()
