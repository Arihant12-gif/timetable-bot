import os
import requests
from datetime import datetime

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# (time, subject, room, teacher)
TIMETABLE = {
    "Monday": [
        ("09:55-10:50", "Organization & Architecture of Computer", "A-213", "Akanksha Chauhan"),
        ("12:40-13:35", "System Administration Lab (B)", "E-201", "Rimmy"),
        ("13:35-14:30", "Computer Vision", "A-110", "Sachin"),
    ],
    "Tuesday": [
        ("09:55-10:50", "Computer Vision", "A-004", "Sachin"),
        ("12:40-13:35", "Organization & Architecture of Computer", "A-112", "Akanksha Chauhan"),
    ],
    "Wednesday": [
        ("09:55-10:50", "Advanced Environmental Studies", "A-203", "Vishal Penuly"),
        ("12:40-13:35", "Competitive Programming & Algorithmic Optimization", "E-306", "Himanshu Verma"),
        ("13:35-14:30", "Organization & Architecture of Computer", "A-112", "Akanksha Chauhan"),
    ],
    "Thursday": [
        ("09:00-09:55", "Organization & Architecture of Computer", "A-212", "Akanksha Chauhan"),
        ("12:40-13:35", "System Administration Lab (A)", "E-201", "Rimmy"),
    ],
    "Friday": [
        ("10:50-11:45", "Computer Vision", "A-008", "Sachin"),
        ("12:40-13:35", "System Administration Lab (A)", "E-201", "Rimmy"),
        ("13:35-14:30", "Competitive Programming & Algorithmic Optimization", "E-306", "Himanshu Verma"),
    ],
    "Saturday": [
        ("09:00-09:55", "Summer Internship III", "A-211", "Shakti Singh"),
        ("09:55-10:50", "Computer Vision", "A-209", "Sachin"),
        ("10:50-11:45", "Competitive Programming & Algorithmic Optimization", "E-306", "Himanshu Verma"),
        ("12:40-13:35", "System Administration Lab (B)", "E-201", "Rimmy"),
    ],
    "Sunday": [],
}

today = datetime.now().strftime("%A")
classes = TIMETABLE.get(today, [])

if classes:
    lines = [f"{t}\n{subject} ({room})\n{teacher}\n" for t, subject, room, teacher in classes]
    message = f"Aaj ({today}) ka timetable:\n\n" + "\n".join(lines)
else:
    message = f"Aaj ({today}) koi class nahi hai. Chill karo!"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
r = requests.post(url, data={"chat_id": CHAT_ID, "text": message})
print(r.status_code, r.text)