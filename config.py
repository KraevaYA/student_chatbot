import os

TOKEN = 'YOUR_API'

PROJECT_DIR = os.getcwd()
_PATH_FILES = {
    "TIMETABLE_FILE": os.path.join(PROJECT_DIR, "data/timetable.json"),
    "CONTACTS_FILE": os.path.join(PROJECT_DIR, "data/contacts.json"),
    "TUTORS_INFO_FILE": os.path.join(PROJECT_DIR, "data/tutors_info.json")
}

TIMETABLE_FILE = _PATH_FILES["TIMETABLE_FILE"]
CONTACTS_FILE = _PATH_FILES["CONTACTS_FILE"]
TUTORS_INFO_FILE = _PATH_FILES["TUTORS_INFO_FILE"]
