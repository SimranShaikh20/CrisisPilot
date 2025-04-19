# 🚀 CrisisPilot - Smart Relief
## *Transforming Disaster Response Through AI* 🌍

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-orange)](https://tensorflow.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-red)](https://pytorch.org/)

---

## 💡 Inspiration
Natural disasters strike without warning, leaving communities vulnerable and emergency responders racing against time. We were deeply moved by recent catastrophic events where delayed response times led to preventable losses. This inspired us to leverage cutting-edge AI technology to revolutionize disaster management and potentially save countless lives. ⏳💔

## 🌟 What It Does
CrisisPilot is a comprehensive disaster management solution that combines multiple AI-powered systems:

### 🔥 1. Early-Stage Wildfire Detection
- Analyzes NOAA-20 VIIRS satellite imagery in real-time 🛰️
- Achieves **90.5% accuracy** using transfer-learned **RESNET101**
- Provides immediate alerts to emergency response teams 🚨

### 🚁 2. Drone-Based Victim Detection
- Implements **YOLOv8** for real-time human detection 🏃‍♂️
- Enables swift aerial search and rescue operations 🛩️
- Processes high-resolution imagery for accurate victim localization 🎯

### 🌊 3. AI-Powered Flood Analysis
- Performs **semantic segmentation** using **U-NET** architecture 🌐
- Maps flood-affected areas for resource optimization 🗺️
- Generates actionable insights for emergency responders 📊

### 🧠 4. LLM-Powered Emergency Q&A Chatbot (CrisisBot)
Our system includes a smart chatbot trained on domain-specific emergency response data, built using **Large Language Models (LLMs)** like **Mistral**.

#### 📌 Key Features:
- ✅ Answers real-time queries from users in disaster zones  
- 🌐 Trained on **emergency protocols**, **survival tips**, and **local rescue services**  
- 🤖 Powered by **Snowflake Cortex with Mistral-Large2** for natural language understanding  
- 🔄 Retrieval-Augmented Generation (RAG) pipeline using **Cortex Search**  
- 🗺️ Responds with **location-aware, contextual suggestions**

#### 🔧 How It Works:
- User submits a query via chatbot UI (e.g., "Where is the nearest shelter?")
- Query goes through **Cortex Search** to find the most relevant documents  
- Mistral LLM generates a human-like, reliable response  
- Streamlit interface shows chat in real-time 💬

#### 🔥 Use Cases:
- "I need food and water in [Location]. What should I do?"  
- "How can I stay safe from wildfire smoke?"  
- "Is it safe to travel through this area?"

### 🚑 5. Integrated Emergency Response System
- Monitors real-time weather conditions ⛈️
- Identifies high-risk zones through geolocation 📍
- Includes **animal welfare protection** features 🐾
- Predicts risk levels using **weather-location correlation** 📡

---

## 🛠️ How We Built It

### 📥 1. Data Collection & Preprocessing
- Gathered satellite imagery from **NOAA-20 VIIRS** 🛰️
- Created custom datasets for **victim detection**
- Preprocessed flood mapping data for **segmentation**

### 🤖 2. Model Development
- Implemented **transfer learning** on RESNET101 for **wildfire detection** 🔥
- Trained **YOLOv8** for human detection in aerial imagery 📷
- Developed **U-NET** architecture for **flood segmentation** 🌊
- Integrated **Mistral LLM** with **Cortex Search** for chatbot 💬

### 🚀 3. Integration & Deployment
- Built **API endpoints** for real-time data processing ⚡
- Created **Streamlit-based** web interface 🖥️
- Implemented **cloud-based** processing pipeline ☁️

---

## 🏗️ Technical Architecture & ML Pipeline

![CrisisPilot ML Architecture](https://gist.githubusercontent.com/Niraj1608/8d1fc288c82a0f1bf69c91369ac9879e/raw/df6629e4b216b2bd19442b960449f42fd2668d46/arc1.svg)

Our intelligent disaster response system leverages four specialized ML models working in parallel:

### 🏗️ Model Architecture

1. **🔥 Wildfire Detection Using RESNET101**
   - Transfer learning on NOAA-20 VIIRS satellite imagery 🛰️
   - **90.5% detection accuracy** in varied conditions ✅
   - Real-time monitoring and early warning system ⚠️
   - Custom-tuned for different terrain types ⛰️

2. **🚁 Victim Detection with YOLOv8**
   - Real-time processing of **drone footage** 🎥
   - High-precision **human detection** in disaster zones 🎯
   - Optimized for **aerial viewpoints** 🛩️
   - **Low-latency** for immediate response 🕒

3. **🌊 Flood Analysis via U-NET**
   - Advanced **semantic segmentation** 📡
   - Precise **mapping of flood-affected regions** 🗺️
   - **Resource allocation optimization** 💧
   - **Real-time flood progression tracking** 🚨

4. **🧠 Emergency Q&A Chatbot via LLM**
   - Query processing using **Cortex Search**
   - Natural language generation using **Mistral-Large2**
   - Real-time answers with context awareness and location-based guidance

### 🔄 Data Pipeline

- **📥 Input Sources:**
  - Satellite imagery (**NOAA-20 VIIRS**)
  - Real-time **drone feeds**
  - **Semantic mapping** data
  - **Weather and terrain** information
  - **User queries for Q&A chatbot**

- **⚡ Processing Layer:**
  - **Parallel processing** of multiple data streams
  - **GPU-accelerated inference**
  - **Edge computing integration**
  - **Automated alert generation**
  - **Natural language understanding pipeline**

- **📤 Output Systems:**
  - **Emergency alert distribution** 🚨
  - **Risk zone visualization** 🌍
  - **Resource optimization engine** 🔧
  - **Real-time situation dashboard** 📊
  - **User-interactive Q&A chatbot** 💬

---

## 🚧 Challenges We Ran Into

### 🏗️ Technical Challenges
- **Processing large satellite imagery datasets** 📡
- **Optimizing model performance for real-time detection** 🎯
- **Handling varying weather and lighting conditions** ☀️🌧️
- **Scaling LLMs for fast user interaction during high query volume**

### 🔄 Integration Challenges
- **Combining multiple AI models into a unified system** 🤖
- **Ensuring reliable real-time performance** ⏳
- **Managing computational resources efficiently** 💻

---

## 🏆 Accomplishments That We're Proud Of
✅ Achieved **90.5% accuracy** in wildfire detection 🔥  
✅ Successfully implemented **real-time victim detection system** 🚁  
✅ Developed **semantic flood mapping** using U-NET 🌊  
✅ Built an **LLM-powered emergency chatbot** for situational assistance 💬  
✅ Created a **user-friendly interface** for emergency responders 🖥️  
✅ Developed a **scalable and integrated solution** 🔄  
✅ Built a **working prototype within the hackathon timeframe** ⏳  

---

## 📚 What We Learned
- **Advanced computer vision techniques** for disaster management 🤖  
- **Real-time processing** of satellite imagery 🛰️  
- **Integration of multiple AI models** 🏗️  
- **Natural language processing with LLMs** 📘  
- **Importance of user-centric design** in emergency response systems 🎯  
- **Collaborative problem-solving** under time constraints 🤝  

---

## 🌍 Social Impact
1. **💖 Life-Saving Potential**  
2. **🏠 Community Resilience**  
3. **🌱 Environmental Protection**  
4. **💰 Economic Benefits**  
5. **♻️ Long-term Sustainability**  

---

## 🔮 What's Next for CrisisPilot

### 🔧 Technical Enhancements
- **Implement edge computing** for faster processing ⚡  
- **Expand to additional disaster types** 🌍  
- **Improve model accuracy** through additional training 🎯  

### 📲 Feature Additions
- **Mobile app development** for field teams 📱  
- **Integration with existing emergency response systems** 🚑  
- **Multi-language support** for global deployment 🌎  
- **Voice-based interaction for the chatbot** 🎙️  

### 🚀 Scaling & Deployment
- **Partner with disaster management agencies** 🏛️  
- **Pilot programs in high-risk areas** 📍  
- **Open-source community development** 🤝  

---

## 🛠️ Built With
- 🐍 Python  
- 🔥 TensorFlow  
- 🛠️ PyTorch  
- 🖥️ Streamlit  
- 🎯 YOLO  
- 🎥 OpenCV  
- 🤖 Machine Learning  
- 🧠 Mistral LLM  
- 🌐 Snowflake Cortex & Cortex Search  
- 🏗️ Computer Vision  
- 📡 Deep Learning  

---

<div align="center">
  <h3>🚀 Built with ❤️ by Team CrisisPilot</h3>
  <p>🌍 Technology that saves lives! 🌍</p>
</div>
