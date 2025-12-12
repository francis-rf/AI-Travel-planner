# AI Travel Planner ✈️

> Your intelligent companion for unforgettable day trips - Generate personalized itineraries powered by AI

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![LangChain](https://img.shields.io/badge/LangChain-Latest-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Overview

AI Travel Planner is a modern web application that leverages the power of AI to create personalized day trip itineraries. Simply enter your destination city and interests, and let our AI assistant craft the perfect itinerary tailored just for you.

### Demo

**Live Application:** [http://localhost:8000](http://localhost:8000)

**Key Capabilities:**
- Generate customized itineraries based on user interests
- Discover top 5 recommended places in any city
- Get chronological schedules (Morning, Afternoon, Evening)
- Receive pro tips for your specific trip
- Beautiful, modern glassmorphism UI

## ✨ Features

### Core Features
- 🤖 **AI-Powered Recommendations** - Uses advanced LLMs via Groq for intelligent itinerary generation
- 🎨 **Modern UI** - Stunning glassmorphism design with animated gradients
- 📍 **City-Based Planning** - Support for any city worldwide
- ❤️ **Interest Matching** - Personalized recommendations based on your preferences
- 📅 **Structured Itineraries** - Clear morning, afternoon, and evening schedules
- 💡 **Pro Tips** - Practical advice for transport, hidden gems, and local recommendations

### Technical Features
- ⚡ **FastAPI Backend** - High-performance async API
- 🔗 **LangChain Integration** - Modern LCEL chains for LLM interactions
- 📊 **Comprehensive Logging** - Production-ready logging with rotation
- 🛡️ **Error Handling** - Custom exceptions and validation
- 🐳 **Docker Support** - Easy containerization and deployment
- ☸️ **Kubernetes Ready** - K8s manifests for production deployment
- 📝 **API Documentation** - Auto-generated Swagger and ReDoc docs

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern, fast web framework for building APIs
- **LangChain** - Framework for developing LLM applications
- **Groq** - Fast LLM inference API
- **Pydantic** - Data validation using Python type hints
- **Uvicorn** - Lightning-fast ASGI server

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern glassmorphism design
- **Vanilla JavaScript** - No frameworks, pure performance
- **Google Fonts (Inter)** - Beautiful typography

### DevOps
- **Docker** - Containerization
- **Kubernetes** - Container orchestration
- **Python Logging** - Structured logging

## 🏗️ Architecture

```
┌─────────────────┐
│   Web Browser   │
│  (Frontend UI)  │
└────────┬────────┘
         │ HTTP/REST
         ▼
┌─────────────────┐
│   FastAPI App   │
│  (app.py)       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ TravelPlanner   │
│  (planner.py)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Itinerary Chain │
│ (LangChain)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Groq API       │
│  (LLM)          │
└─────────────────┘
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Groq API key ([Get one here](https://console.groq.com))

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "3. AI Travel Agent"
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -e .
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   OPENAI_MODEL=qwen/qwen3-32b
   ENVIRONMENT=development
   ```

5. **Run the application**
   ```bash
   uvicorn app:app --reload
   ```

6. **Access the application**
   
   Open your browser and navigate to:
   - Frontend: [http://localhost:8000](http://localhost:8000)
   - API Docs (Swagger): [http://localhost:8000/api/docs](http://localhost:8000/api/docs)
   - API Docs (ReDoc): [http://localhost:8000/api/redoc](http://localhost:8000/api/redoc)

## 💡 Usage

### Web Interface

1. **Enter Your Destination**
   - Type the city name (e.g., "Paris", "Tokyo", "New York")

2. **Add Your Interests**
   - Type an interest and press Enter
   - Add multiple interests (e.g., "museums", "food", "art", "nightlife")

3. **Generate Itinerary**
   - Click "Generate My Itinerary"
   - Wait for AI to create your personalized plan

4. **Review Your Itinerary**
   - See top 5 recommended places
   - View chronological schedule
   - Read pro tips for your trip

### Example Queries

**Paris Art & Food Lover:**
- City: `Paris`
- Interests: `museums, food, art, cafes`

**Tokyo Tech & Culture:**
- City: `Tokyo`
- Interests: `temples, technology, anime, sushi, nightlife`

**New York Explorer:**
- City: `New York`
- Interests: `broadway, museums, skyline, pizza, shopping`

## 📚 API Documentation

### Generate Itinerary

**Endpoint:** `POST /api/generate-itinerary`

**Request Body:**
```json
{
  "city": "Paris",
  "interests": ["museums", "food", "art"]
}
```

**Response:**
```json
{
  "itinerary": "### 🏙️ Top 5 Recommended Places in Paris\n\n1. **Louvre Museum**...",
  "city": "Paris",
  "interests": ["museums", "food", "art"]
}
```

**Status Codes:**
- `200 OK` - Itinerary generated successfully
- `400 Bad Request` - Invalid input (empty city or no interests)
- `500 Internal Server Error` - Failed to generate itinerary

### Health Check

**Endpoint:** `GET /health`

**Response:**
```json
{
  "status": "healthy",
  "service": "AI Travel Planner"
}
```

## 🐳 Deployment

### Docker Deployment

1. **Build the Docker image**
   ```bash
   docker build -t ai-travel-planner .
   ```

2. **Run the container**
   ```bash
   docker run -d \
     -p 8000:8000 \
     -e GROQ_API_KEY=your_api_key \
     -e OPENAI_MODEL=qwen/qwen3-32b \
     --name travel-planner \
     ai-travel-planner
   ```

3. **View logs**
   ```bash
   docker logs -f travel-planner
   ```

### Kubernetes Deployment

1. **Create secret with API key**
   ```bash
   kubectl create secret generic travel-planner-secrets \
     --from-literal=GROQ_API_KEY=your_api_key \
     --from-literal=LLM_MODEL=llama-3.1-70b-versatile
   ```

2. **Deploy to Kubernetes**
   ```bash
   kubectl apply -f k8s.yaml
   ```

3. **Check deployment**
   ```bash
   kubectl get pods -l app=travel-planner
   kubectl get svc travel-planner-service
   ```

4. **Access the application**
   ```bash
   # Get external IP
   kubectl get svc travel-planner-service
   
   # Or port-forward for testing
   kubectl port-forward svc/travel-planner-service 8000:80
   ```

## 📁 Project Structure

```
3. AI Travel Agent/
├── app.py                      # FastAPI application entry point
├── Dockerfile                  # Docker configuration
├── k8s.yaml                   # Kubernetes manifests
├── requirements.txt           # Python dependencies
├── setup.py                   # Package setup
├── .env                       # Environment variables (not in git)
├── .gitignore                 # Git ignore rules
├── README.md                  # This file
│
├── src/                       # Source code
│   ├── __init__.py
│   ├── chains/               # LangChain implementations
│   │   ├── __init__.py
│   │   └── itinerary_chain.py  # LCEL chain for itinerary generation
│   └── core/                 # Core business logic
│       ├── __init__.py
│       └── planner.py        # TravelPlanner class
│
├── utils/                    # Utility modules
│   ├── __init__.py
│   ├── logger.py            # Logging configuration
│   └── custom_exception.py  # Custom exception handling
│
├── config/                   # Configuration files
│   ├── __init__.py
│   └── config.py            # App configuration
│
├── static/                   # Frontend files
│   ├── index.html           # Main HTML page
│   ├── styles.css           # Glassmorphism styles
│   └── script.js            # Frontend JavaScript
│
└── logs/                     # Application logs (auto-generated)
    └── log_YYYY-MM-DD.log
```

## 🎨 Design Features

### Glassmorphism UI
- **Animated gradient background** - Smoothly shifting purple/pink gradients
- **Floating shapes** - Subtly animated blur elements
- **Glass cards** - Frosted glass effect with backdrop blur
- **Smooth transitions** - Professional micro-animations
- **Responsive design** - Mobile-friendly layout

### Color Palette
- Primary: `#6366f1` (Indigo)
- Secondary: `#ec4899` (Pink)
- Accent: `#f59e0b` (Amber)
- Gradients: Purple → Pink → Blue

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `GROQ_API_KEY` | Your Groq API key | - | ✅ Yes |
| `OPENAI_MODEL` | LLM model to use | `qwen/qwen3-32b` | No |
| `ENVIRONMENT` | Environment (development/production) | `development` | No |

### Logging

Logs are stored in the `logs/` directory with daily rotation:
- **Log file format:** `log_YYYY-MM-DD.log`
- **Retention:** 30 days
- **Levels:** DEBUG (dev), INFO (prod)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Groq** - For fast LLM inference
- **LangChain** - For the amazing LLM framework
- **FastAPI** - For the excellent web framework
- **Google Fonts** - For the Inter typeface

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: [your-email@example.com]

---

**Made with ❤️ for travelers worldwide** ✈️🌍

*Powered by AI | Built with FastAPI, LangChain & Modern Web Technologies*
