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

def notify():
    notification = str(timetable[day]).strip("[]").replace("'", "")
    send("https://ntfy.sh/Time_Table", 
        data=notification.encode(encoding="utf-8"), 
        headers={
            "Title": "Your Time Table for Today",
            "Priority": "urgent"})

if day in timetable:
    notify()
else:
    print("No school today")

