# Insurance Track

A comprehensive insurance tracking system built with FastAPI and React. This application helps manage customer insurance policies, track renewals, and organize related documents.

## Features

- Customer management
- Insurance policy tracking
- Document management
- Renewal notifications
- Modern, responsive UI

## Tech Stack

### Backend
- FastAPI (Python)
- SQLAlchemy ORM
- SQLite Database
- Pydantic for data validation

### Frontend (Planned)
- React
- TypeScript
- Tailwind CSS
- React Hook Form

## Project Structure

```
insurance-track/
├── backend/
│   ├── app/
│   │   ├── api/         # API routes
│   │   ├── models/      # Database models
│   │   ├── schemas/     # Pydantic schemas
│   │   └── services/    # Business logic
│   ├── tests/
│   └── requirements.txt
├── frontend/            # (Planned)
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   └── hooks/
│   └── package.json
└── memory-bank/        # Project documentation
```

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+ (for frontend)
- Git

### Backend Setup

1. Clone the repository
```bash
git clone https://github.com/dolphinium/insurance-track.git
cd insurance-track
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the development server
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### Frontend Setup (Coming Soon)

1. Install dependencies
```bash
cd frontend
npm install
```

2. Start development server
```bash
npm run dev
```

The application will be available at `http://localhost:3000`

## API Documentation

Once the backend server is running, you can access the API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 