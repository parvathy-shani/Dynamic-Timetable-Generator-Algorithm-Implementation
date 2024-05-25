import json


courses = [
    {"courseName": "Programming in C", "courseCode": "EST102", "type": "F", "allottedBatch": "S2C"},
    {"courseName": "Programming in C", "courseCode": "EST102", "type": "F", "allottedBatch": "S2D"},
    {"courseName": "Graph Theory", "courseCode": "MAT206", "type": "A", "allottedBatch": "S4C"},
    {"courseName": "Graph Theory", "courseCode": "MAT206", "type": "A", "allottedBatch": "S4D"},
    {"courseName": "Computer Organization and Architecture", "courseCode": "CST 202", "type": "B", "allottedBatch": "S4C"},
    {"courseName": "Computer Organization and Architecture", "courseCode": "CST 202", "type": "B", "allottedBatch": "S4D"},
    {"courseName": "Database Management Systems", "courseCode": "CST 204", "type": "C", "allottedBatch": "S4C"},
    {"courseName": "Database Management Systems", "courseCode": "CST 204", "type": "C", "allottedBatch": "S4D"},
    {"courseName": "Operating Systems", "courseCode": "CST 206", "type": "D", "allottedBatch": "S4C"},
    {"courseName": "Operating Systems", "courseCode": "CST 206", "type": "D", "allottedBatch": "S4D"},
    {"courseName": "Constitution of India", "courseCode": "MCN202", "type": "F", "allottedBatch": "S4C"},
    {"courseName": "Constitution of India", "courseCode": "MCN202", "type": "F", "allottedBatch": "S4D"},
    {"courseName": "Design and Engineering", "courseCode": "EST200", "type": "E", "allottedBatch": "S4D"},
    {"courseName": "Design and Engineering", "courseCode": "EST200", "type": "E", "allottedBatch": "S4C"},
    {"courseName": "Digital Lab", "courseCode": "CSL 202", "type": "S", "allottedBatch": "S4C"},
    {"courseName": "Digital Lab", "courseCode": "CSL 202", "type": "S", "allottedBatch": "S4D"},
    {"courseName": "Operating Systems Lab", "courseCode": "CSL 204", "type": "T", "allottedBatch": "S4C"},
    {"courseName": "Operating Systems Lab", "courseCode": "CSL 204", "type": "T", "allottedBatch": "S4D"},
    {"courseName": "Mathematics for Machine Learning", "courseCode": "CST 284", "type": "Minor", "allottedBatch": "S4C"},
    {"courseName": "Number Theory", "courseCode": "CST292", "type": "Minor", "allottedBatch": "S4C"},
    {"courseName": "Computational Fundamentals for Machine Learning", "courseCode": "CST 284", "type": "Honours", "allottedBatch": "S4C"},
    {"courseName": "Compiler Design", "courseCode": "CST 302", "type": "A", "allottedBatch": "S6C"},
    {"courseName": "Compiler Design", "courseCode": "CST 302", "type": "A", "allottedBatch": "S6D"},
    {"courseName": "Computer Graphics and Image Processing", "courseCode": "CST 304", "type": "B", "allottedBatch": "S6D"},
    {"courseName": "Computer Graphics and Image Processing", "courseCode": "CST 304", "type": "B", "allottedBatch": "S6C"},
    {"courseName": "Algorithm Analysis and Design", "courseCode": "CST 306", "type": "C", "allottedBatch": "S6C"},
    {"courseName": "Algorithm Analysis and Design", "courseCode": "CST 306", "type": "C", "allottedBatch": "S6D"},
    {"courseName": "Foundations of machine learning", "courseCode": "CST 312", "type": "D-Elective1", "allottedBatch": "S6C"},
    {"courseName": "Foundations of security in computing", "courseCode": "CST 332", "type": "D-Elective1", "allottedBatch": "S6C"},
    {"courseName": "Programming in Python", "courseCode": "CST 362", "type": "D-Elective1", "allottedBatch": "S6C"},
    {"courseName": "Programming in Python", "courseCode": "CST 362", "type": "D-Elective1", "allottedBatch": "S6D"},
    {"courseName": "Industrial Economics & Foreign Trade", "courseCode": "HUT 300", "type": "E", "allottedBatch": "S6C"},
    {"courseName": "Industrial Economics & Foreign Trade", "courseCode": "HUT 300", "type": "E", "allottedBatch": "S6D"},
    {"courseName": "Industrial Economics & Foreign Trade", "courseCode": "HUT 300", "type": "E", "allottedBatch": "S6D"},
    {"courseName": "Comprehensive Course Work", "courseCode": "CST 308", "type": "F", "allottedBatch": "S6C"},
    {"courseName": "Comprehensive Course Work", "courseCode": "CST 308", "type": "F", "allottedBatch": "S6D"},
    {"courseName": "Networking Lab", "courseCode": "CSL 332", "type": "S", "allottedBatch": "S6C"},
    {"courseName": "Networking Lab", "courseCode": "CSL 332", "type": "S", "allottedBatch": "S6D"},
    {"courseName": "Mini Project", "courseCode": "CSD 334", "type": "T", "allottedBatch": "S6C"},
    {"courseName": "Mini Project", "courseCode": "CSD 334", "type": "T", "allottedBatch": "S6D"},
    {"courseName": "Concepts in deep learning", "courseCode": "CST 384", "type": "Minor", "allottedBatch": "S6C"},
    {"courseName": "Network Security", "courseCode": "CST 394", "type": "Honours", "allottedBatch": "S6C"},
    {"courseName": "Advanced Topics in Machine Learning", "courseCode": "CST 396", "type": "Honours", "allottedBatch": "S6C"},
    {"courseName": "Distributed Computing", "courseCode": "CST 402", "type": "A", "allottedBatch": "S8C"},
    {"courseName": "Distributed Computing", "courseCode": "CST 402", "type": "A", "allottedBatch": "S8D"},
    {"courseName": "Deep learning", "courseCode": "CST 414", "type": "B-Elective3", "allottedBatch": "S8C"},
    {"courseName": "Soft Computing", "courseCode": "CST 444", "type": "B-Elective3", "allottedBatch": "S8C"},
    {"courseName": "Soft Computing", "courseCode": "CST 444", "type": "B-Elective3", "allottedBatch": "S8D"},
    {"courseName": "Data Compression Techniques", "courseCode": "CST 446", "type": "C-Elective4", "allottedBatch": "S8C"},
    {"courseName": "Data Compression Techniques", "courseCode": "CST 446", "type": "C-Elective4", "allottedBatch": "S8D"},
    {"courseName": "Mobile Computing", "courseCode": "CST 476", "type": "C-Elective4", "allottedBatch": "S8C"},
    {"courseName": "Blockchain Technologies", "courseCode": "CST 428", "type": "D-Elective5", "allottedBatch": "S8C"},
    {"courseName": "Blockchain Technologies", "courseCode": "CST 428", "type": "D-Elective5", "allottedBatch": "S8D"},
    {"courseName": "Internet Of Things", "courseCode": "CST 448", "type": "D-Elective5", "allottedBatch": "S8C"},
    {"courseName": "Comprehensive Course Viva", "courseCode": "CST 404", "type": "T", "allottedBatch": "S8C"},
    {"courseName": "Comprehensive Course Viva", "courseCode": "CST 404", "type": "T", "allottedBatch": "S8D"},
    {"courseName": "Project Phase II", "courseCode": "CSD 416", "type": "U", "allottedBatch": "S8C"},
    {"courseName": "Project Phase II", "courseCode": "CSD 416", "type": "U", "allottedBatch": "S8D"}
]


course_codes = {}  # Empty dictionary to store course code

# Generate codes for all courses
for course in courses:
    course_code, sem_code, batch = course["courseCode"], course["type"], course["allottedBatch"]
    sem_code = "m" if sem_code == "Minor" else "h" if sem_code == "Honours" else sem_code[0]
    code = f"{course_code.replace(' ', '')}-{sem_code}-{batch}"
    course_codes[code] = [course_code, sem_code, batch]

# Save codes to a json file
file_path = "courses.json"  # Output file to store the output
with open(file_path, "w") as json_file:  # Open the file to write the output
    json.dump(course_codes, json_file, indent=4)  # Store the timeslots into json file
