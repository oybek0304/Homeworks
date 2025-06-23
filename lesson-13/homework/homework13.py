import re
from datetime import datetime, timedelta
import time
import pytz


# 1. Age Calculator
def age_calculator(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    today = datetime.today()
    delta = today - birthdate

    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        months -= 1
        days += (birthdate.replace(month=birthdate.month % 12 + 1, day=1) - timedelta(days=1)).day
    if months < 0:
        years -= 1
        months += 12

    print(f"You are {years} years, {months} months, and {days} days old.")


# 2. Days Until Next Birthday
def days_until_birthday(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    today = datetime.today()
    next_birthday = birthdate.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    days_remaining = (next_birthday - today).days
    print(f"Days until next birthday: {days_remaining}")


# 3. Meeting Scheduler
def meeting_scheduler(current_time_str, hours, minutes):
    current_time = datetime.strptime(current_time_str, "%Y-%m-%d %H:%M")
    duration = timedelta(hours=hours, minutes=minutes)
    end_time = current_time + duration
    print("Meeting will end at:", end_time.strftime("%Y-%m-%d %H:%M"))


# 4. Timezone Converter
def timezone_converter(date_str, from_zone, to_zone):
    local_tz = pytz.timezone(from_zone)
    target_tz = pytz.timezone(to_zone)

    naive_dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    local_dt = local_tz.localize(naive_dt)
    converted_dt = local_dt.astimezone(target_tz)
    print("Converted Time:", converted_dt.strftime("%Y-%m-%d %H:%M %Z%z"))


# 5. Countdown Timer
def countdown_timer(future_time_str):
    future_time = datetime.strptime(future_time_str, "%Y-%m-%d %H:%M:%S")
    while True:
        now = datetime.now()
        if now >= future_time:
            print("Time's up!")
            break
        remaining = future_time - now
        print("Time remaining:", remaining, end="\r")
        time.sleep(1)


# 6. Email Validator
def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, email):
        print("Valid email.")
    else:
        print("Invalid email.")


# 7. Phone Number Formatter
def format_phone_number(number):
    digits = re.sub(r"\D", "", number)
    if len(digits) == 10:
        formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        print("Formatted Phone Number:", formatted)
    else:
        print("Invalid phone number length.")


# 8. Password Strength Checker
def password_strength(password):
    if (len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"\d", password)):
        print("Strong password.")
    else:
        print("Weak password. Try including uppercase, lowercase, and digits.")


# 9. Word Finder
def find_word(word, text):
    occurrences = [m.start() for m in re.finditer(rf"\b{re.escape(word)}\b", text, flags=re.IGNORECASE)]
    print(f"'{word}' found at positions:", occurrences)


# 10. Date Extractor
def extract_dates(text):
    pattern = r"\b(?:\d{1,2}[/-])?\d{1,2}[/-]\d{2,4}\b"
    dates = re.findall(pattern, text)
    print("Dates found:", dates)
