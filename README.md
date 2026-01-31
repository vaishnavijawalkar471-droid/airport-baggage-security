# ✈️ Airport Baggage Security Check System (Python)

A Python-based command-line application that simulates an **international airport baggage security check** and generates a **realistic boarding pass** after successful verification.

This project demonstrates core Python concepts like input validation, conditional logic, list processing, exception handling, and date-time operations — all wrapped in an interactive user experience.

---

## 🚀 Features

- 🧳 Interactive baggage declaration system  
- 🚫 Detection of **banned** and **risky** items  
- ⚖️ Baggage weight validation with excess fee calculation  
- 🧴 Liquid compliance checks (100ml rule)  
- 🌍 International destination selection  
- 🎟️ Automatic boarding pass generation  
- ⏱️ Real-time departure & arrival calculation  
- ✨ Clean CLI interface with structured output  

---

## 🛠️ Tech Stack

- **Language:** Python 3  
- **Libraries Used:**
  - `sys`
  - `random`
  - `datetime`

No external dependencies required.

---

## 📂 Project Structure

airport-baggage-security/
│
├── airport_security.py # Main application file
└── README.md # Project documentation 


---
🧪 How It Works
User enters personal and travel details

Baggage items are scanned for:

Banned items → Immediate rejection

Risky items → Must be checked in

Weight limits are enforced:

India: 15 kg

International: 20 kg

Liquid rules are verified

If all checks pass → Boarding pass is generated 🎉

📌 Sample Output
Passenger Name

Airline & Flight Number

Destination

Boarding Gate & Terminal

Seat Number

Departure & Arrival Time

Items declared in baggage

🎯 Learning Outcomes
Real-world input validation

Nested condition handling

List filtering and keyword detection

Date & time manipulation

User-friendly CLI design

🌱 Future Enhancements
Airline-specific baggage rules

GUI or Web version (Streamlit / Flask)

Persistent booking records

Multiple passenger handling

📜 License
This project is open-source and available for learning and educational use.

🙌 Acknowledgements
Inspired by real-world airport security workflows and built to practice practical Python programming.

Happy coding & safe travels ✈️
