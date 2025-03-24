# Insurance Tracking System - Technical Context (Simplified)

## Technology Stack

### Frontend
1. **Framework**
   - React 18.x
   - Tailwind CSS 3.x

2. **State Management**
   - React Context API
   - Local Storage for persistence

3. **UI Components**
   - Tailwind UI (free components)
   - React Hook Form
   - React Table (free version)
   - React DatePicker

### Backend
1. **Core**
   - Python 3.11+
   - FastAPI
   - SQLAlchemy

2. **Database**
   - SQLite

3. **File Storage**
   - Local file system

### Email
- Local SMTP server for development
- Simple Python `smtplib` for production

## Development Setup

### Prerequisites
```bash
# Required software
- Python 3.11+
- Node.js 20.x LTS
- Git
- VS Code (recommended)
```

### Environment Variables
```env
# Frontend (.env.local)
REACT_APP_API_URL=http://localhost:8000

# Backend (.env)
DATABASE_URL=sqlite:///./insurance_track.db
SMTP_HOST=localhost
SMTP_PORT=1025
STORAGE_PATH=./storage
```

### Local Development
```bash
# Frontend
npm install
npm start

# Backend
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

## Project Structure

### Frontend
```
frontend/
├── src/
│   ├── components/     # Reusable components
│   ├── pages/         # Page components
│   ├── hooks/         # Custom hooks
│   ├── context/       # React Context
│   └── utils/         # Utility functions
└── public/            # Static assets
```

### Backend
```
backend/
├── app/
│   ├── api/           # API routes
│   ├── models/        # SQLAlchemy models
│   ├── schemas/       # Pydantic models
│   └── services/      # Business logic
├── storage/           # Local file storage
└── tests/            # Test files
```

## Dependencies

### Core Dependencies
```txt
# Frontend (package.json)
{
  "react": "^18.2.0",
  "tailwindcss": "^3.0.0",
  "react-hook-form": "^7.0.0",
  "react-table": "^7.0.0",
  "axios": "^1.0.0"
}

# Backend (requirements.txt)
fastapi>=0.100.0
uvicorn>=0.22.0
sqlalchemy>=2.0.0
pydantic>=2.0.0
aiofiles>=0.8.0
python-dateutil>=2.8.2
```

## Database Schema

### Tables

1. **customers**
```sql
CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    address TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

2. **insurances**
```sql
CREATE TABLE insurances (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    type TEXT NOT NULL,
    renewal_date DATE NOT NULL,
    coverage_details TEXT,
    premium_amount DECIMAL(10,2),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers (id)
);
```

3. **documents**
```sql
CREATE TABLE documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    insurance_id INTEGER,
    filename TEXT NOT NULL,
    file_path TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers (id),
    FOREIGN KEY (insurance_id) REFERENCES insurances (id)
);
```

## File Storage Structure
```
storage/
├── customer_1/
│   ├── insurance_1/
│   │   ├── documents/
│   │   └── screenshots/
│   └── insurance_2/
│       ├── documents/
│       └── screenshots/
└── customer_2/
    └── insurance_1/
        ├── documents/
        └── screenshots/
```

## Technical Constraints

### Performance
- Simple SQLite queries
- Local file access
- Basic indexing

### Features
- Local-only deployment
- Single-user system
- Basic CRUD operations
- Simple email notifications

### Browser Support
- Chrome (last 2 versions)
- Firefox (last 2 versions)
- Safari (last 2 versions)
- Edge (last 2 versions)

# Technical Context

## Technology Stack

### Backend
1. FastAPI Framework
   - Version: Latest stable
   - Purpose: REST API implementation
   - Features:
     - Async support
     - Automatic OpenAPI docs
     - Type validation
     - Dependency injection

2. SQLAlchemy ORM
   - Version: Latest stable
   - Purpose: Database operations
   - Features:
     - Model definitions
     - Relationship mapping
     - Query building
     - Transaction management

3. Pydantic
   - Version: Latest stable
   - Purpose: Data validation
   - Features:
     - Schema definitions
     - Request/response models
     - Type checking
     - Data serialization

4. SQLite
   - Version: 3
   - Purpose: Development database
   - Features:
     - Local storage
     - Zero configuration
     - Easy backup
     - Development friendly

### Frontend (Planned)
1. React
   - Version: Latest stable
   - Purpose: UI framework
   - Features:
     - Component-based
     - Virtual DOM
     - Hooks
     - Context API

2. Tailwind CSS
   - Version: Latest stable
   - Purpose: Styling
   - Features:
     - Utility-first
     - Responsive design
     - Custom configuration
     - JIT compilation

3. TypeScript
   - Version: Latest stable
   - Purpose: Type safety
   - Features:
     - Static typing
     - Interface definitions
     - Type inference
     - Code organization

## Project Structure

### Backend Structure
```
backend/
├── app/
│   ├── api/
│   │   ├── customers.py
│   │   ├── insurances.py
│   │   └── documents.py
│   ├── models/
│   │   ├── customer.py
│   │   ├── insurance.py
│   │   └── document.py
│   ├── schemas/
│   │   ├── customer.py
│   │   ├── insurance.py
│   │   └── document.py
│   ├── services/
│   │   ├── customer_service.py
│   │   ├── insurance_service.py
│   │   └── document_service.py
│   ├── database.py
│   └── main.py
├── tests/
├── alembic/
└── requirements.txt
```

### Frontend Structure (Planned)
```
frontend/
├── src/
│   ├── components/
│   │   ├── layout/
│   │   ├── customers/
│   │   ├── insurance/
│   │   └── documents/
│   ├── services/
│   │   ├── api.ts
│   │   ├── customerService.ts
│   │   ├── insuranceService.ts
│   │   └── documentService.ts
│   ├── hooks/
│   ├── utils/
│   └── App.tsx
├── public/
└── package.json
```

## Development Environment

### Required Tools
1. Python 3.8+
2. Node.js 16+
3. npm/yarn
4. Git
5. VS Code (recommended)

### Python Dependencies
```
fastapi
uvicorn
sqlalchemy
pydantic
python-multipart
python-jose[cryptography]
passlib[bcrypt]
python-dotenv
```

### Development Setup
1. Backend
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

2. Frontend (Planned)
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## API Documentation

### Endpoints
1. Customers
   - GET /customers/
   - POST /customers/
   - GET /customers/{id}
   - PUT /customers/{id}
   - DELETE /customers/{id}

2. Insurance
   - GET /insurances/
   - POST /insurances/
   - GET /insurances/{id}
   - PUT /insurances/{id}
   - DELETE /insurances/{id}
   - GET /insurances/customer/{customer_id}
   - GET /insurances/upcoming-renewals/

3. Documents
   - POST /documents/upload/{customer_id}
   - GET /documents/customer/{customer_id}
   - GET /documents/insurance/{insurance_id}
   - GET /documents/{id}
   - DELETE /documents/{id}

## Database Schema

### Tables
1. customers
   ```sql
   CREATE TABLE customers (
       id INTEGER PRIMARY KEY,
       name VARCHAR,
       email VARCHAR,
       phone VARCHAR,
       address TEXT
   )
   ```

2. insurances
   ```sql
   CREATE TABLE insurances (
       id INTEGER PRIMARY KEY,
       customer_id INTEGER,
       type VARCHAR,
       policy_number VARCHAR,
       start_date DATE,
       end_date DATE,
       renewal_date DATE,
       premium DECIMAL,
       FOREIGN KEY(customer_id) REFERENCES customers(id)
   )
   ```

3. documents
   ```sql
   CREATE TABLE documents (
       id INTEGER PRIMARY KEY,
       customer_id INTEGER,
       insurance_id INTEGER,
       filename VARCHAR,
       file_path VARCHAR,
       upload_date TIMESTAMP,
       FOREIGN KEY(customer_id) REFERENCES customers(id),
       FOREIGN KEY(insurance_id) REFERENCES insurances(id)
   )
   ```

## Security Implementation

### API Security
1. CORS Configuration
   ```python
   origins = [
       "http://localhost:3000"
   ]
   app.add_middleware(CORSMiddleware, allow_origins=origins)
   ```

2. Input Validation
   - Pydantic models
   - Type checking
   - Data sanitization

### File Storage
1. Document Storage
   - Local filesystem
   - Organized by customer
   - Secure file naming
   - Type validation

## Testing Strategy

### Backend Tests (Planned)
1. Unit Tests
   - Service functions
   - Model operations
   - Utility functions

2. Integration Tests
   - API endpoints
   - Database operations
   - File operations

### Frontend Tests (Planned)
1. Component Tests
   - Rendering
   - User interactions
   - State management

2. E2E Tests
   - User flows
   - API integration
   - Error handling 