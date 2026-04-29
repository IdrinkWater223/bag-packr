from datetime import datetime as dt
import requests


timetable = {
    "Monday":    ["Mathematics", "Metal Work", "History", "Physical Education"],
    "Tuesday":   ["Spanish", "English Language", "Personal Development", "Biology", "Visual Arts"],
    "Wednesday": ["Chemistry", "Biology", "Geography", "Physics", "Building & Technology"],
    "Thursday":  ["Technical Drawing", "English Language", "Social Studies", "Mathematics"],
    "Friday":    ["Physics", "Mathematics", "Music", "English Literature", "Information Technology"],
}

day = dt.now().strftime("%A")
send = requests.post

def notis():
    notification = str(timetable[day]).strip("[]").replace("'", "")
    send("Add your own ntfy link", 
        data=notification.encode(encoding="utf-8"), 
        headers={
            "Title": "📚 Your Time Table for Today",
            "Priority": "urgent"})

if day in timetable:
    notis()
else:
    print("No school today")

