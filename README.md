# 🚀 CrisisPilot - Smart Relief  
## *Transforming Disaster Response Through AI* 🌍

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-orange)](https://tensorflow.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-red)](https://pytorch.org/)

---

## 💡 Inspiration  
Natural disasters strike without warning, leaving communities vulnerable. Witnessing the devastating impact of delayed responses drove us to build **CrisisPilot** — an AI-powered system designed to **reduce response time**, **optimize resources**, and **save lives**. ⏳💔

---

## 🌟 Features Overview  

### 🔥 Wildfire Detection  
- Real-time analysis of **NOAA-20 VIIRS** satellite imagery 🛰️  
- **90.5% accuracy** using **ResNet101** (transfer learning) 🎯  
- Immediate alerts for early-stage fire response 🚨  

### 🚁 Drone-Based Victim Detection  
- Real-time **human detection** using **YOLOv8** 👁️  
- High-resolution aerial analysis for fast victim localization 🧍‍♂️🧍‍♀️  
- Enables swift search & rescue operations 🛩️  

### 🌊 Flood Mapping & Analysis  
- Semantic segmentation with **U-NET** 🧠  
- Maps affected areas for **resource allocation** and **evacuation planning** 🗺️  
- Real-time flood progression tracking 💧  

### 🧠 CrisisBot - LLM-Powered Emergency Chatbot  
- Built with **Mistral LLM** on **Snowflake Cortex**  
- Retrieval-Augmented Generation (RAG) with **Cortex Search** 🔍  
- Offers **location-aware** survival guidance and answers 🚑  
- Responds to queries like:  
  - “Where is the nearest shelter?” 🏕️  
  - “How to avoid wildfire smoke?” 🌫️  
  - “Is it safe to travel in this area?” 🚗  

### 🌐 Integrated Emergency Response System  
- Real-time **weather monitoring** ⛈️  
- Identifies **high-risk zones** with geolocation 📍  
- **Animal welfare protection** 🐾  
- Predicts risk levels via **weather-terrain correlation** 📡  

---

## 🛠️ How We Built It  

### 📥 Data Collection  
- Satellite imagery (NOAA-20)  
- Custom aerial datasets for victim detection  
- Flood data for segmentation  

### 🤖 Model Training  
- **ResNet101** for fire detection 🔥  
- **YOLOv8** for drone-based human detection 🚁  
- **U-NET** for flood segmentation 🌊  
- **Mistral LLM + Cortex Search** for chatbot 💬  

### 🚀 Deployment  
- API endpoints for real-time inference ⚡  
- Web interface built with **Streamlit** 🖥️  
- Cloud-based scalable backend ☁️  

---

## 🧩 System Architecture  

![CrisisPilot ML Architecture](https://gist.githubusercontent.com/Niraj1608/8d1fc288c82a0f1bf69c91369ac9879e/raw/df6629e4b216b2bd19442b960449f42fd266)

### ML Models in Action  
1. **🔥 ResNet101** → Wildfire detection (90.5% accuracy)  
2. **🚁 YOLOv8** → Real-time drone-based victim detection  
3. **🌊 U-NET** → Flood segmentation & analysis  
4. **🧠 Mistral + Cortex Search** → Q&A chatbot with contextual awareness  

### 🔄 Data Flow  
- **Input**: Satellite, drone feeds, weather & terrain data, user queries  
- **Processing**: Parallel GPU inference, edge computing, alert generation  
- **Output**: Alerts 🚨, maps 🗺️, chatbot replies 💬, real-time dashboards 📊  

---

## 🚧 Challenges  

### 🛠️ Technical  
- Handling massive satellite datasets  
- Ensuring fast inference under variable lighting/weather  
- Optimizing models for real-time performance  

### 🔗 Integration  
- Unifying multiple ML pipelines  
- Efficient resource management for simultaneous processing  
- Reliable user interactions with LLMs at scale  

---

## 🏆 Achievements  
✅ 90.5% wildfire detection accuracy  
✅ Real-time drone-based victim identification  
✅ Effective flood region mapping  
✅ Functional LLM-powered chatbot  
✅ End-to-end Streamlit-based system prototype  
✅ Scalable, modular design ready for deployment  

---

## 📘 What We Learned  
- Advanced computer vision & segmentation for disaster response  
- LLM-based natural language systems for emergencies  
- Real-time data processing & streaming  
- System integration & scalability under constraints  
- Empathy-driven tech for societal impact  

---

## 🌍 Social Impact  
- **💖 Life-Saving Potential**: Early alerts, faster rescues  
- **🏠 Resilient Communities**: Support in high-risk zones  
- **🌱 Environment Protection**: Quicker wildfire intervention  
- **💰 Economic Recovery**: Minimize disaster-related losses  
- **♻️ Sustainability**: Scalable, reusable infrastructure  

---

## 🔮 What's Next  

### 🔧 Tech Roadmap  
- Deploy on **edge devices** for faster on-site processing  
- Expand to **earthquake & landslide detection**  
- Enhance model precision with diverse training datasets  

### 📲 Feature Expansion  
- **Mobile app** for field responders  
- **Voice command support** 🎙️  
- **Multilingual chatbot** 🌍  
- Connect with **emergency response networks**  

### 🌐 Scaling Up  
- Collaborate with **disaster relief agencies**  
- Launch **pilot programs** in high-risk zones  
- Grow with an **open-source community** 🤝  

---

## 🧰 Tech Stack  
- 🐍 Python  
- 🔥 TensorFlow & PyTorch  
- 🖥️ Streamlit  
- 🎯 YOLOv8 & OpenCV  
- 📡 ResNet101, U-NET  
- 🤖 Mistral LLM  
- 🌍 GIS & weather APIs  

---

<div align="center">
  <h3>🚀 Built with ❤️ by Team CrisisPilot</h3>
  <p>🌍 Innovating for a safer world</p>
</div>
