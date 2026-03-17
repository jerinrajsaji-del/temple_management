# Divine Seva - Premium Temple Management System

Divine Seva is a state-of-the-art, multi-tenant temple management platform designed to provide a seamless and spiritually enriching experience for both devotees and temple administrators. Inspired by the premium aesthetics of kshethrasuvidham.com, it features a cinematic Maroon & Gold design system, advanced animations, and a robust role-based administrative architecture.

## ✨ Core Features

### 🏯 For Devotees
- **Cinematic Experience**: A high-end visual interface with smooth transitions and premium typography.
- **Pooja Discovery**: Easily browse and discover ritual offerings across various temples.
- **Seamless Booking**: A streamlined booking process with mandatory Nakshatra details for ritual accuracy.
- **Secure Payments**: A high-fidelity simulated payment gateway supporting UPI, Cards, and Net Banking.
- **Spiritual Ledger**: A personal dashboard to track booking history and access digital e-receipts.

### 🛡️ For Administrators
- **Multi-Temple Support**: Tiered access allowing specific administrators to manage individual temples.
- **Scoped Management**: Dashboard analytics and record management filtered by temple ownership.
- **Full CRUD Control**: Add, Edit, and Delete poojas and temple profiles directly from the frontend.
- **Safety Measures**: Confirmation guardrails for all destructive administrative actions.

## 🛠️ Technology Stack
- **Framework**: Django 5.x
- **Frontend**: Bootstrap 5.3.2, CSS3 Animations, Bootstrap Icons
- **Database**: SQLite (Development)
- **Image Processing**: Pillow

## 🚀 Setup & Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Temple_management
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize Database**
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```
   Access the platform at `http://127.0.0.1:8000/`

## 🎨 Design System
The platform utilizes a custom "Divine Theme":
- **Primary**: Maroon (`#800000`)
- **Accent**: Gold (`#FFD700`)
- **Aesthetic**: Glassmorphism, Fade-in & Slide-up animations, Hover transforms.

---
*Created with spiritual intent for temple automation.*
