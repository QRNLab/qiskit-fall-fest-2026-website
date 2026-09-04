import datetime

def create_ics():
    # Define event data
    events = [
        {
            "summary": "Preliminary Walkthrough",
            "start": datetime.datetime(2026, 10, 26, 20, 0),
            "end": datetime.datetime(2026, 10, 26, 21, 0),
            "description": "Hands-on basics of quantum computing and organizers' journey, outlook.\\n\\nSpeakers: Animesh Banik (Technical) and Co-organizers' introduction\\nHost: Sazzadul Islam",
        },
        {
            "summary": "Official Kick-off: Qiskit Fall Fest",
            "start": datetime.datetime(2026, 10, 27, 20, 0),
            "end": datetime.datetime(2026, 10, 27, 21, 0),
            "description": "Qiskit Fall Fest introduction, Quantum and Qiskit 101.\\n\\nSpeakers: QRN sir, IBM speaker\\nHost: Sanjana Tabassum",
        },
        {
            "summary": "Student Journeys & Hackathon Kick-off",
            "start": datetime.datetime(2026, 10, 31, 20, 0),
            "end": datetime.datetime(2026, 10, 31, 22, 0),
            "description": "Phd students explore their own journey and share technical insights. On this day, we kick off the hackathon.\\n\\nSpeakers: Shah Ishmam Mohatashim, Syed Emad Uddin Shubha, Debopriyo Biswas, Tanvir Ahmed Masum\\nHost: Animesh Banik",
        },
        {
            "summary": "Quantum in Academia & Industry",
            "start": datetime.datetime(2026, 11, 1, 20, 0),
            "end": datetime.datetime(2026, 11, 1, 22, 0),
            "description": "Professors of Bangladeshi origin who are working in the USA or other countries or home country and industry experts share their journeys.\\n\\nSpeakers: Omar Sheehab, M. Zahid Hasan, Tibra Ali, Talal Ahmed Chowdhury, Showmitra Das",
        },
        {
            "summary": "Hackathon Troubleshooting & Support",
            "start": datetime.datetime(2026, 11, 3, 20, 0),
            "end": datetime.datetime(2026, 11, 3, 21, 0),
            "description": "Helping Participants.\\n\\nSpeakers: Tridib Sarker, Sazzadul Islam, Sanjana Tabassum\\nHost: Tridib Sarker",
        },
        {
            "summary": "Hackathon Submission Deadline",
            "start": datetime.datetime(2026, 11, 5, 22, 0),
            "end": datetime.datetime(2026, 11, 5, 22, 0), # Deadline is a point in time
            "description": "This is a hard deadline to submit hackathon projects. This is not a session!",
        },
        {
            "summary": "Closing Ceremony & Winners Announcement",
            "start": datetime.datetime(2026, 11, 7, 21, 0),
            "end": datetime.datetime(2026, 11, 7, 22, 0),
            "description": "Winner announcement, announcing upcoming events, QRNLab description, Closing remarks.\\n\\nSpeakers: QRN, Judges\\nHost: Animesh Banik",
        }
    ]

    ics_content = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Qiskit Fall Fest 2026//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH"
    ]

    for event in events:
        # Format timestamps in UTC for the ICS file. 
        # BST is UTC+1. So 20:00 BST = 19:00 UTC.
        # Wait, is BST British Summer Time (UTC+1) or Bangladesh Standard Time (UTC+6)?
        # Let's assume British Summer Time (UTC+1) since it's "BST" usually in international contexts, 
        # BUT the host is from Bangladesh... 
        # Let's check typical usage. "BST" in Bangladesh is Bangladesh Standard Time. 
        # In the context of a Bangladeshi group (QRN, Bangladeshi professors), BST likely means Bangladesh Standard Time (UTC+6).
        # Wait, the prompt says "Current location is Chattogram, Bangladesh." 
        # So BST = Bangladesh Standard Time = UTC+6.
        # 8:00 PM BST = 20:00 UTC+6 = 14:00 UTC.
        
        start_utc = event['start'] - datetime.timedelta(hours=6)
        end_utc = event['end'] - datetime.timedelta(hours=6)

        dtstart = start_utc.strftime("%Y%m%dT%H%M%SZ")
        if event['start'] == event['end']: # For deadline
            dtend = dtstart
        else:
            dtend = end_utc.strftime("%Y%m%dT%H%M%SZ")
            
        now = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
        
        uid = f"{start_utc.strftime('%Y%m%dT%H%M%S')}@qiskitfallfest2026.bd"

        ics_content.extend([
            "BEGIN:VEVENT",
            f"UID:{uid}",
            f"DTSTAMP:{now}",
            f"DTSTART:{dtstart}",
            f"DTEND:{dtend}",
            f"SUMMARY:{event['summary']}",
            f"DESCRIPTION:{event['description']}",
            "LOCATION:Online",
            "END:VEVENT"
        ])

    ics_content.append("END:VCALENDAR")
    return "\\n".join(ics_content)

print(create_ics())