# AI Calculator

A smart mathematical calculator that transforms hand-drawn equations into solutions using AI recognition.

## Table of Contents
- [Features](#features)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
  - [Frontend](#frontend)
  - [Backend](#backend)
- [Technical Architecture](#technical-architecture)
- [Development Guide](#development-guide)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features
- Real-time drawing canvas with multi-color support
- AI-powered recognition of handwritten mathematical expressions
- Dynamic LaTeX rendering of equations and results
- Draggable solution display
- Variable memory system for complex calculations
- Clean, modern interface with intuitive controls

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-calc.git
   cd ai-calc
   ```

2. Set up frontend and backend (see setup instructions below)
3. Start drawing and calculating!

## Project Structure

### Frontend
The frontend is built with React + TypeScript + Vite, providing an interactive drawing interface.

#### Key Files
- `src/screens/home/index.tsx`: Main calculator component with canvas and LaTeX rendering
- `vite.config.ts`: Vite configuration with path aliases
- `.env.local`: Environment configuration
- `constants.ts`: Application constants and configurations

#### Frontend Setup
```bash
cd ai-calc
npm install
npm run dev
```

### Backend
FastAPI service for mathematical processing and image recognition.

#### Key Files
- `main.py`: FastAPI server with CORS and route configuration
- `schema.py`: Pydantic models for data validation
- `requirements.txt`: Python dependencies

#### Backend Setup
```bash
cd calc-be
pip install -r requirements.txt
python main.py
```

## Technical Architecture

### Frontend Stack
- React 18+ with TypeScript
- Vite for build tooling
- MathJax for LaTeX rendering
- HTML Canvas API for drawing
- Axios for API communication

### Backend Stack
- FastAPI framework
- Python 3.8+
- Pydantic for data validation
- CORS middleware
- Custom AI model for expression recognition

## Development Guide

1. Start backend server:
   ```bash
   cd calc-be
   python main.py
   ```

2. Launch frontend development server:
   ```bash
   cd ai-calc
   npm run dev
   ```

3. Access application:
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8900

## Configuration

### Frontend (.env.local)
```
VITE_API_URL="http://localhost:8900"
```

## System Requirements
- Node.js 16+
- Python 3.8+
- npm or yarn
- Modern web browser with canvas support

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## API Endpoints

### Calculate Mathematical Expression
- **POST** `/calculator/calculate`
  - Request Body:
    ```json
    {
      "image": "string (base64 encoded image)",
      "dict_of_vars": {
        "key": "value"
      }
    }
    ```
  - Response:
    ```json
    {
      "data": [
        {
          "expr": "string (mathematical expression)",
          "result": "string (calculated result)",
          "assign": "boolean"
        }
      ]
    }
    ```

### Health Check
- **GET** `/`
  - Response:
    ```json
    {
      "message": "server is up"
    }
    ```

## License
MIT License - see LICENSE file for details
