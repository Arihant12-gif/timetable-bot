
import os
from datetime import datetime
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

TOKEN = os.environ["BOT_TOKEN"]


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


async def today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    day = datetime.now().strftime("%A")
    classes = TIMETABLE.get(day, [])

    if not classes:
        message = f"Aaj ({day}) koi class nahi hai. Chill karo!"
    else:
        lines = []

        for time, subject, room, teacher in classes:
            lines.append(
                f"🕒 {time}\n"
                f"📚 {subject}\n"
                f"🏫 Room: {room}\n"
                f"👨‍🏫 {teacher}"
            )

        message = f"Aaj ({day}) ka timetable:\n\n"
        message += "\n\n".join(lines)

    await update.message.reply_text(message)

    
async def tomorrow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from datetime import timedelta

    tomorrow_day = (datetime.now() + timedelta(days=1)).strftime("%A")
    classes = TIMETABLE.get(tomorrow_day, [])
    print("Tomorrow:", tomorrow_day)
    print("Classes:", classes)

    if not classes:
        message = f"Kal ({tomorrow_day}) koi class nahi hai. Chill karo!"
    else:
        lines = []

        for time, subject, room, teacher in classes:
            lines.append(
                f"🕒 {time}\n"
                f"📚 {subject}\n"
                f"🏫 Room: {room}\n"
                f"👨‍🏫 {teacher}"
            )

        message = f"Kal ({tomorrow_day}) ka timetable:\n\n"
        message += "\n\n".join(lines)

    await update.message.reply_text(message)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Timetable Bot ready hai!\n"
        "/today - Aaj ka timetable"
    )


app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("today", today))
app.add_handler(CommandHandler("tomorrow", tomorrow))

app.run_polling()
