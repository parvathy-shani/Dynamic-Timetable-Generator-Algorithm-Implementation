import json

courses = [
    ("Programming in C", "EST102", "F", "S2C"),
    ("Programming in C", "EST102", "F", "S2D"),
    ("Graph Theory", "MAT206", "A", "S4C"),
    ("Graph Theory", "MAT206", "A", "S4D"),
    ("Computer Organization and Architecture", "CST 202", "B", "S4C"),
    ("Computer Organization and Architecture", "CST 202", "B", "S4D"),
    ("Database Management Systems", "CST 204", "C", "S4C"),
    ("Database Management Systems", "CST 204", "C", "S4D"),
    ("Operating Systems", "CST 206", "D", "S4C"),
    ("Operating Systems", "CST 206", "D", "S4D"),
    ("Constitution of India", "MCN202", "F", "S4C"),
    ("Constitution of India", "MCN202", "F", "S4D"),
    ("Design and Engineering", "EST200", "E", "S4D"),
    ("Design and Engineering", "EST200", "E", "S4C"),
    ("Digital Lab", "CSL 202", "S", "S4C"),
    ("Digital Lab", "CSL 202", "S", "S4D"),
    ("Operating Systems Lab", "CSL 204", "T", "S4C"),
    ("Operating Systems Lab", "CSL 204", "T", "S4D"),
    ("Mathematics for Machine Learning", "CST 284", "Minor", "S4C"),
    ("Number Theory", "CST292", "Minor", "S4C"),
    ("Computational Fundamentals for Machine Learning", "CST 284", "Honours", "S4C"),
    ("Compiler Design", "CST 302", "A", "S6C"),
    ("Compiler Design", "CST 302", "A", "S6D"),
    ("Computer Graphics and Image Processing", "CST 304", "B", "S6D"),
    ("Computer Graphics and Image Processing", "CST 304", "B", "S6C"),
    ("Algorithm Analysis and Design", "CST 306", "C", "S6C"),
    ("Algorithm Analysis and Design", "CST 306", "C", "S6D"),
    ("Foundations of machine learning", "CST 312", "D-Elective1", "S6C"),
    ("Foundations of security in computing", "CST 332", "D-Elective1", "S6C"),
    ("Programming in Python", "CST 362", "D-Elective1", "S6C"),
    ("Programming in Python", "CST 362", "D-Elective1", "S6D"),
    ("Industrial Economics & Foreign Trade", "HUT 300", "E", "S6C"),
    ("Industrial Economics & Foreign Trade", "HUT 300", "E", "S6D"),
    ("Industrial Economics & Foreign Trade", "HUT 300", "E", "S6D"),
    ("Comprehensive Course Work", "CST 308", "F", "S6C"),
    ("Comprehensive Course Work", "CST 308", "F", "S6D"),
    ("Networking Lab", "CSL 332", "S", "S6C"),
    ("Networking Lab", "CSL 332", "S", "S6D"),
    ("Mini Project", "CSD 334", "T", "S6C"),
    ("Mini Project", "CSD 334", "T", "S6D"),
    ("Concepts in deep learning", "CST 384", "Minor", "S6C"),
    ("Network Security", "CST 394", "Honours", "S6C"),
    ("Advanced Topics in Machine Learning", "CST 396", "Honours", "S6C"),
    ("Distributed Computing", "CST 402", "A", "S8C"),
    ("Distributed Computing", "CST 402", "A", "S8D"),
    ("Deep learning", "CST 414", "B-Elective3", "S8C"),
    ("Soft Computing", "CST 444", "B-Elective3", "S8C"),
    ("Soft Computing", "CST 444", "B-Elective3", "S8D"),
    ("Data Compression Techniques", "CST 446", "C-Elective4", "S8C"),
    ("Data Compression Techniques", "CST 446", "C-Elective4", "S8D"),
    ("Mobile Computing", "CST 476", "C-Elective4", "S8C"),
    ("Blockchain Technologies", "CST 428", "D-Elective5", "S8C"),
    ("Blockchain Technologies", "CST 428", "D-Elective5", "S8D"),
    ("Internet Of Things", "CST 448", "D-Elective5", "S8C"),
    ("Comprehensive Course Viva", "CST 404", "T", "S8C"),
    ("Comprehensive Course Viva", "CST 404", "T", "S8D"),
    ("Project Phase II", "CSD 416", "U", "S8C"),
    ("Project Phase II", "CSD 416", "U", "S8D")
]


course_codes = {}  #empty dictionary to store course code

# Generate codes for all courses
for course in courses:
     course_code, sem_code, batch = course[1], course[2], course[3]
     sem_code = "m" if sem_code == "Minor" else "h" if sem_code == "Honours" else sem_code[0]
     code = f"{course_code.replace(' ', '')}-{sem_code}-{batch}"
     course_codes[code] = [course_code, sem_code, batch]

# Save codes to a json file
file_path = "courses.json"     # Output file to store the output
with open(file_path, "w") as json_file:  # Open the file to write the output
    json.dump(course_codes, json_file, indent=4)  # Storing the timeslots into json file


