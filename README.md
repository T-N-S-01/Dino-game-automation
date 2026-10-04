# 🦖 Auto Dino Bot – Computer Vision in Action

A fun Python project that uses Computer Vision to automatically play the Chrome T-Rex runner game in real time.

## 🚀 Overview
This bot reads a region of your screen in front of the dinosaur, detects obstacles from pixel intensity, and presses jump automatically.

## 🛠️ Built With
- Python
- OpenCV + Pillow
- PyAutoGUI
- NumPy

## 📦 Install
```bash
pip install -r requirements.txt
```

## ▶️ Run
1. Open Chrome Dino game (`chrome://dino`) and start running.
2. Run:
   ```bash
   python dino_bot.py
   ```
3. Tune ROI and detection parameters if needed:
   ```bash
   python dino_bot.py --x 300 --y 380 --width 180 --height 80 --threshold 120 --min-pixels 120
   ```

Press `Ctrl+C` to stop.
