from datetime import datetime

# Zodiac list with date ranges
zodiac_signs = [
    ("Capricorn", (12, 22), (1, 19)),
    ("Aquarius", (1, 20), (2, 18)),
    ("Pisces", (2, 19), (3, 20)),
    ("Aries", (3, 21), (4, 19)),
    ("Taurus", (4, 20), (5, 20)),
    ("Gemini", (5, 21), (6, 20)),
    ("Cancer", (6, 21), (7, 22)),
    ("Leo", (7, 23), (8, 22)),
    ("Virgo", (8, 23), (9, 22)),
    ("Libra", (9, 23), (10, 22)),
    ("Scorpio", (10, 23), (11, 21)),
    ("Sagittarius", (11, 22), (12, 21))
]

# Extract zodiac names for index mapping
zodiac_names = [z[0] for z in zodiac_signs]

# Compatibility matrix (2D list)
matrix = [
    [85,60,75,90,70,80,65,95,70,85,60,88],
    [60,88,70,75,85,78,72,80,90,76,82,68],
    [75,70,90,65,80,85,88,78,72,84,76,82],
    [90,75,65,88,70,85,60,95,78,82,68,86],
    [70,85,80,70,92,78,75,88,95,76,84,72],
    [80,78,85,85,78,90,82,88,76,92,84,80],
    [65,72,88,60,75,82,90,78,84,86,80,76],
    [95,80,78,95,88,88,78,92,85,90,76,84],
    [70,90,72,78,95,76,84,85,90,88,82,80],
    [85,76,84,82,76,92,86,90,88,90,80,78],
    [60,82,76,68,84,84,80,76,82,80,88,86],
    [88,68,82,86,72,80,76,84,80,78,86,90]
]

# Function to find zodiac sign
def find_zodiac(day, month):
    for name, start, end in zodiac_signs:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return name
    return "Capricorn"

# Function to get compatibility message
def get_result(score):
    if score >= 90:
        return "🌟 Excellent Match"
    elif score >= 75:
        return "🤝 Good Compatibility"
    elif score >= 60:
        return "⚖️ Average Match"
    else:
        return "Needs Effort"


# ---------------- MAIN ----------------
try:
    d1 = input().strip()
    d2 = input().strip()

    # Convert string to date
    date1 = datetime.strptime(d1, "%d-%m")
    date2 = datetime.strptime(d2, "%d-%m")

    # Get zodiac signs
    sign1 = find_zodiac(date1.day, date1.month)
    sign2 = find_zodiac(date2.day, date2.month)

    # Get matrix index
    i = zodiac_names.index(sign1)
    j = zodiac_names.index(sign2)

    # Get compatibility score
    score = matrix[i][j]

    # Output
    print("\n----- Zodiac Compatibility Result -----\n")
    print("Person 1 Zodiac :", sign1)
    print("Person 2 Zodiac :", sign2)
    print("Compatibility   :", str(score) + "%")
    print("Result          :", get_result(score))

# Proper exception handling
except ValueError:
    print("Invalid input! Please enter date in DD-MM format.")