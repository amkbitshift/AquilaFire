# 🔥 AquilaFire – AI-Powered Wildfire Early Detection & Risk Forecasting

AquilaFire is an AI-based early wildfire detection system developed as a **24-hour hackathon MVP**.  
It focuses on **early smoke detection**, intelligent **fire risk assessment**, and **fire spread simulation** to assist disaster management authorities.

---
<img width="1920" height="1020" alt="Screenshot 2025-12-26 111350" src="https://github.com/user-attachments/assets/53439743-6830-4413-a7df-b9c074134d14" />
<img width="1920" height="1020" alt="Screenshot 2025-12-26 111415" src="https://github.com/user-attachments/assets/ca6917ba-c0c9-4275-94e8-d7b8d2804a54" />
<img width="1920" height="1020" alt="Screenshot 2025-12-26 111506" src="https://github.com/user-attachments/assets/f367c555-a370-4ab3-b1e4-a1c118735872" />

## 🚀 Key Features

- 🌫️ **Hybrid Smoke Detection**
  - YOLOv8-Nano deep learning model
  - Smoke color & texture validation
  - Temporal consistency check to reduce false alarms

- 📊 **Fire Risk Scoring (0–100)**
  - Based on smoke confidence, temperature, humidity, and wind speed
  - Explainable and lightweight logic

- 🔥 **Fire Spread Simulation**
  - Grid-based cellular automata model
  - Spread influenced by wind direction
  - Visual prediction for next few hours (prototype)

- 🖥️ **Interactive Dashboard**
  - Built using Streamlit
  - Upload images, view detection, risk level, and spread simulation

---

## 🏗️ System Architecture

Camera / Image Input
↓
Hybrid Smoke Detection
↓
Feature Extraction
↓
Fire Risk Score Engine
↓
Alert Generation + Dashboard
↓
Fire Spread Simulation (Prototype)


---

## ⚙️ Tech Stack

- **AI / ML:** YOLOv8-Nano
- **Programming:** Python
- **UI:** Streamlit
- **Image Processing:** OpenCV
- **Simulation:** Cellular Automata
- **Visualization:** Matplotlib

---

## 🧪 How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/AquilaFire.git
cd AquilaFire

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Dashboard
streamlit run app.py

📸 Demo Outputs
Feature	Preview
Dashboard	screenshots/dashboard.png
Smoke Detection	screenshots/detection.png
Fire Spread Simulation	screenshots/spread_simulation.png

<img width="1920" height="1020" alt="Screenshot 2025-12-26 111350" src="https://github.com/user-attachments/assets/2125b581-10e8-4fcf-9754-2941cd702c7e" />
<img width="1920" height="1020" alt="Screenshot 2025-12-26 111506" src="https://github.com/user-attachments/assets/bfa7c652-93c1-4d32-be41-ab96977a3a0f" />
<img width="1920" height="1020" alt="Screenshot 2025-12-26 111415" src="https://github.com/user-attachments/assets/c2562041-dd1d-42fa-ab3d-43c28326bbc9" />

🧠 Hackathon Scope Clarification

This project is a functional MVP built within 24 hours

Satellite feeds and drone dispatch are simulated modules

Core AI detection, risk scoring, and visualization are fully functional

Architecture is designed for easy real-world scaling

🌍 Impact

Early detection before flames appear

Reduced response time for authorities

Protection of forests, wildlife, and nearby communities

Alignment with UN SDGs: Climate Action & Life on Land

👥 Team Cicada 101

Ameya Jose Chazhoor (Team Lead)

Maria Ann Mathew

Niranjana PP

Shaun Saji E

📜 License

This project is open for academic and research purposes.

AquilaFire/
│
├── app.py                  # Streamlit dashboard (main entry)
├── detect.py               # Hybrid smoke detection (YOLO + color)
├── smoke_filter.py         # Smoke color validation
├── fire_spread.py          # Fire spread simulation (cellular automata)
├── risk.py                 # Fire risk score logic
│
├── sample_data/
│   ├── fire1.jpg
│   ├── smoke1.jpg
│
├── screenshots/
│   ├── dashboard.png
│   ├── detection.png
│   ├── spread_simulation.png
│
├── requirements.txt
├── README.md
└── LICENSE   (optional)

requirements.txt
ultralytics
streamlit
opencv-python
numpy
matplotlib
---
