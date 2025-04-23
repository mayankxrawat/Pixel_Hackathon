# Faculty workhour tracker and visualizer
 Team: BuildForGEHU’25

--Name	Role
Mayank Rawat	Backend Dev
Sarthak chaudhary	Frontend Developer
Kanchna Rana	Backend and database management
Jay Pandey documentation & backend


 --Project Features
 Secure Login using institutional email ID
 Punch In/Out system for faculty attendance


 --How It Works
 
Faculty punch in/out daily.
National Holidays
Custom Admin Holidays
Sundays
Faculty and Admin see visual reports and alerts.

--Technologies Used

--Backend
Flask (Python)
Flask-CORS – For cross-origin API access
Flask-SQLAlchemy
MySQL – Database
Datetime – For time calculations

--Frontend (HTML/CSS/JS)


--Testing & Tools
GitHub – Version control and team collaboration

--Project Structure
bash
Copy
Edit
backend/
│
├── app.py              # Main Flask app
├── models.py           # Database models
├── utils.py            # Helper functions for hours, holidays
├── auth.py             # Token-based auth and route protection
└── config.py (optional) # For future configs

frontend/
├── index.html          # Login + Punch UI
├── dashboard.html      # Faculty dashboard
├── admin.html          # Admin view
├── styles.css
└── script.js


--Setup Instructions
Backend
bash
Copy
Edit
cd backend
pip install -r requirements.txt
python app.py
Frontend
Open frontend/index.html in your browser or serve it with Flask static folder.



Team BuildForGEHU’25
📧 Email: [yourteam@email.com]
🌐 GitHub: github.com/mayankxrawat/Pixel_Hackathon

