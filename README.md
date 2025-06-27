# 🌆 Neighbora3D

> **The future of hyperlocal 3D exploration — right in your browser.**  
> Explore a real-time, interactive, intelligent street experience powered by WebGL, real-world APIs, and creative engineering.

![Neighbora3D Banner](./assets/neighbora3d-banner.png)

---

## 📌 Features

### 🏙️ Immersive 3D Street View
- Built with **Three.js** and **WebGL**, Neighbora3D simulates a vibrant street environment.
- Explore various shops, storefronts, and structures — just like walking through a real-world neighborhood.

### 🏪 Smart Shops
- Each shop displays:
  - **Name and branding**
  - **QR codes** (scan to visit online store!)
  - **Operating hours**
- Interactive objects and clickable billboards.
- Built-in **Shopkeeper Dashboard** to edit shop details in real time.

### 📺 Dynamic Billboards
- Live streams running **24/7** including:
  - 🎮 Gameplay reels
  - 🍜 Cooking shows
  - 📰 News & Stock tickers
  - 🧪 Weather & pollution sensors
- Fetches real-time data via **REST APIs** (stocks, AQI, weather).

### 🌗 Day & Night Cycle
- Smooth transitions from sunrise to sunset.
- Functional **street lights** and **moving sun/moon** system based on simulated time or real-time clock.

### 🎬 Auto-Updating Movie Theater
- A digital multiplex showcasing:
  - Now playing movies
  - Auto-refreshed **posters**
  - Future scope: Virtual ticket booking & seat previews.

---

## 📽️ Screenshots

> Add your screenshots in a folder named `/assets` and replace image paths.

| 3D Street View | Smart Shop Boards | Movie Theater |
|:--:|:--:|:--:|
| ![street](./assets/streetview.png) | ![shop](./assets/ramenshop.png) | ![theater](./assets/theater.png) |

---

## 🧠 Technologies Used

| Frontend              | Backend & APIs         | Others                |
|-----------------------|------------------------|------------------------|
| **Three.js**          | **Flask**              | REST APIs (Stocks, AQI)|
| **React (if used)**   | **Node.js**            | **MongoDB**            |
| **WebGL**             | **Express.js**         | **Socket.IO (optional)**|

---

## 🛠️ Local Setup

```bash
git clone https://github.com/your-username/neighbora3d.git
cd neighbora3d
npm install   # or pip install -r requirements.txt for Flask parts
npm start
