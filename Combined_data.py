import json
# Define the teacher codes
teacher_codes = {
    "Gopakumar G": "CSAP01n",
    "Ameena A": "CSAA02n",
    "Manju S Nair": "CSAA03f",
    "Alka Vijay": "CSAA04n",
    "Shyama Das": "CSPP05f",
    "Shiny B": "CSAA06n",
    "Sreelekshmi K R": "CSAA07n",
    "Arathy UP": "CSAA08n",
    "Angel Thankam Thomas": "CSAA09n",
    "Rosy K Philp": "CSAA10n",
    "Jithy John": "CSAA11f",
    "Sabhana Mol S": "CSAA12n",
    "Jyothirmayi Devi": "CSAA13f",
    "Vishnu S Kumar": "CSAA14n",
    "Leya G": "CSAA15n",
    "Betty James": "CSAA16n",
    "Sulaja Sanal": "CSAA17n",
    "Nasseena N": "CSAA18n",
    "Ajoy Thomas": "CSAA19n",
    "Anjitha P": "CSAA20n",
    "Neethu Treesa Jacob": "CSAA21n",
    "Syeatha Merlin Thampy": "CSAA22n",
    "Sheerna Thampi": "CSAA23n",
    "Chinchu M Pillai": "CSAA24n",
    "Sushitha Susan Jacob": "CSAA25n",
    "Ahammed Siraj K K": "CSAP26n"
}

courses = [
    {
        "Course": "Programming in C",
        "Course code": "EST102",
        "Sem code": "F",
        "lecture/week": 1,
        "tutorial/week": 2,
        "practical/week": 0,
        "allotted lecturers": ["Gopakumar G(lecture)", "Ameena A(practical)", "Alka Vijay(practical)", "Shyama Das(tutorial)"],
        "batches": "S2C"
    },
    {
        "Course": "Programming in C",
        "Course code": "EST102",
        "Sem code": "F",
        "lecture/week": 2,
        "tutorial/week": 1,
        "practical/week": 2,
        "allotted lecturers": ["Manju S Nair(lecture)", "Shiny B(practical)", "Arathy UP(practical)", "Betty James(tutorial)"],
        "batches": "S2D"
    },
    {
        "Course": "Graph Theory",
        "Course code": "MAT206",
        "Sem code": "A",
        "lecture/week": 3,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["OD(lecture)", "OD(tutorial)"],
        "batches": "S4C"
    },
    {
        "Course": "Graph Theory",
        "Course code": "MAT206",
        "Sem code": "A",
        "lecture/week": 3,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["OD(lecture)", "OD(tutorial)"],
        "batches": "S4D"
    },
    {
        "Course": "Computer Organization and Architecture",
        "Course code": "CST202",
        "Sem code": "B",
        "lecture/week": 3,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Angel Thankam Thomas(lecture)", "Angel Thankam Thomas(tutorial)"],
        "batches": "S4C"
    },
    {
        "Course": "Computer Organization and Architecture",
        "Course code": "CST202",
        "Sem code": "B",
        "lecture/week": 3,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Gopakumar G(lecture)", "Gopakumar G(tutorial)"],
        "batches": "S4D"
    },
    {
        "Course": "Database Management Systems",
        "Course code": "CST204",
        "Sem code": "C",
        "lecture/week": 3,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Rosy K Philp(lecture)", "Rosy K Philp(tutorial)"],
        "batches": "S4C"
    },
    {
        "Course": "Database Management Systems",
        "Course code": "CST204",
        "Sem code": "C",
        "lecture/week": 3,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Rosy K Philp(lecture)", "Rosy K Philp(tutorial)"],
        "batches": "S4D"
    },
    {
        "Course": "Operating Systems",
        "Course code": "CST206",
        "Sem code": "D",
        "lecture/week": 3,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Jithy John(lecture)", "Jithy John(tutorial)"],
        "batches": "S4C"
    },
    {
        "Course": "Operating Systems",
        "Course code": "CST206",
        "Sem code": "D",
        "lecture/week": 3,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Jithy John(lecture)", "Jithy John(tutorial)"],
        "batches": "S4D"
    },
    {
        "Course": "Constitution of India",
        "Course code": "MCN202",
        "Sem code": "F",
        "lecture/week": 2,
        "tutorial/week": 0,
        "practical/week": 0,
        "allotted lecturers": ["OD(lecture)"],
        "batches": "S4C"
    },
    {
        "Course": "Constitution of India",
        "Course code": "MCN202",
        "Sem code": "F",
        "lecture/week": 2,
        "tutorial/week": 0,
        "practical/week": 0,
        "allotted lecturers": ["OD(lecture)"],
        "batches": "S4D"
    },
    {
        "Course": "Design and Engineering",
        "Course code": "EST200",
        "Sem code": "E",
        "lecture/week": 2,
        "tutorial/week": 0,
        "practical/week": 0,
        "allotted lecturers": ["Sabhana Mol S(lecture)"],
        "batches": "S4D"
    },
    {
        "Course": "Design and Engineering",
        "Course code": "EST200",
        "Sem code": "E",
        "lecture/week": 2,
        "tutorial/week": 0,
        "practical/week": 0,
        "allotted lecturers": ["Sreelekshmi K R(lecture)"],
        "batches": "S4C"
    },
    {
        "Course": "Digital Lab",
        "Course code": "CSL202",
        "Sem code": "S",
        "lecture/week": 0,
        "tutorial/week": 0,
        "practical/week": 2,
        "allotted lecturers": ["OD(Practical)"],
        "batches": "S4C"
    },
    {
        "Course": "Digital Lab",
        "Course code": "CSL202",
        "Sem code": "S",
        "lecture/week": 0,
        "tutorial/week": 0,
        "practical/week": 2,
        "allotted lecturers": ["OD(Practical)"],
        "batches": "S4D"
    },
    {
        "Course": "Operating Systems Lab",
        "Course code": "CSL204",
        "Sem code": "T",
        "lecture/week": 0,
        "tutorial/week": 0,
        "practical/week": 2,
        "allotted lecturers": ["Jyothirmayi Devi(Practical)/Vishnu S Kumar(Practical)"],
        "batches": "S4C"
    },
    {
        "Course": "Operating Systems Lab",
        "Course code": "CSL204",
        "Sem code": "T",
        "lecture/week": 0,
        "tutorial/week": 0,
        "practical/week": 2,
        "allotted lecturers": ["Jithy John(Practical)/Angel Thankam Thomas(Practical)"],
        "batches": "S4D"
    },
    {
        "Course": "Mathematics for Machine Learning",
        "Course code": "CST284",
        "Sem code": "Minor",
        "lecture/week": 3,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Leya G(lecture)", "Leya G(tutorial)"],
        "batches": "S4C"
    },
{
        "Course": "Number Theory",
        "Course code": "CST292",
        "Sem code": "Minor",
        "lecture/week": 3,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Betty James(lecture)", "Betty James(tutorial)"],
        "batches": "S4C"
    },
    {
        "Course": "Computational Fundamentals for Machine Learning",
        "Course code": "CST284",
        "Sem code": "Honours",
        "lecture/week": 3,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Sulaja Sanal(lecture)", "Sulaja Sanal(tutorial)"],
        "batches": "S4C"
    },
    {
        "Course": "Compiler Design",
        "Course code": "CST302",
        "Sem code": "A",
        "lecture/week": 3,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Nasseena N(lecture)", "Nasseena N(tutorial)"],
        "batches": "S6C"
    },
    {
        "Course": "Compiler Design",
        "Course code": "CST302",
        "Sem code": "A",
        "lecture/week": 3,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Nasseena N(lecture)", "Nasseena N(tutorial)"],
        "batches": "S6D"
    },
    {
        "Course": "Computer Graphics and Image Processing",
        "Course code": "CST304",
        "Sem code": "B",
        "lecture/week": 3,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Jyothirmayi Devi(lecture)", "Jyothirmayi Devi(tutorial)"],
        "batches": "S6D"
    },
    {
        "Course": "Computer Graphics and Image Processing",
        "Course code": "CST304",
        "Sem code": "B",
        "lecture/week": 3,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Jyothirmayi Devi(lecture)", "Jyothirmayi Devi(tutorial)"],
        "batches": "S6C"
    },
    {
        "Course": "Algorithm Analysis and Design",
        "Course code": "CST306",
        "Sem code": "C",
        "lecture/week": 3,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Sreelekshmi K R(lecture)", "Sreelekshmi K R(tutorial)"],
        "batches": "S6C"
    },
    {
        "Course": "Algorithm Analysis and Design",
        "Course code": "CST306",
        "Sem code": "C",
        "lecture/week": 3,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Alka Vijay(lecture)", "Alka Vijay(tutorial)"],
        "batches": "S6D"
    },
    {
        "Course": "Foundations of Machine Learning",
        "Course code": "CST312",
        "Sem code": "D-Elective1",
        "lecture/week": 2,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Sulaja Sanal(lecture)", "Sulaja Sanal(tutorial)"],
        "batches": "S6C"
    },
    {
        "Course": "Foundations of Security in Computing",
        "Course code": "CST332",
        "Sem code": "D-Elective1",
        "lecture/week": 2,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Ajoy Thomas(lecture)", "Ajoy Thomas(tutorial)"],
        "batches": "S6C"
    },
    {
        "Course": "Programming in Python",
        "Course code": "CST362",
        "Sem code": "D-Elective1",
        "lecture/week": 2,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Shiny B(lecture)", "Shiny B(tutorial)"],
        "batches": "S6C"
    },
    {
        "Course": "Programming in Python",
        "Course code": "CST362",
        "Sem code": "D-Elective1",
        "lecture/week": 2,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Shyama Das(lecture)", "Shyama Das(tutorial)"],
        "batches": "S6D"
    },
    {
        "Course": "Industrial Economics & Foreign Trade",
        "Course code": "HUT300",
        "Sem code": "E",
        "lecture/week": 3,
        "tutorial/week": 0,
        "practical/week": 0,
        "allotted lecturers": ["OD(lecture)"],
        "batches": "S6C"
    },
    {
        "Course": "Industrial Economics & Foreign Trade",
        "Course code": "HUT300",
        "Sem code": "E",
        "lecture/week": 3,
        "tutorial/week": 0,
        "practical/week": 0,
        "allotted lecturers": ["OD(lecture)"],
        "batches": "S6D"
    },
    {
        "Course": "Industrial Economics & Foreign Trade",
        "Course code": "HUT300",
        "Sem code": "E",
        "lecture/week": 3,
        "tutorial/week": 0,
        "practical/week": 0,
        "allotted lecturers": ["OD(lecture)"],
        "batches": "S6D"
    },
    {
        "Course": "Comprehensive Course Work",
        "Course code": "CST308",
        "Sem code": "F",
        "lecture/week": 1,
        "tutorial/week": 0,
        "practical/week": 0,
        "allotted lecturers": ["Alka Vijay(lecture)", "Rosy K Philp(lecture)", "Nasseena N(lecture)"],
        "batches": "S6C"
    },
    {
        "Course": "Comprehensive Course Work",
        "Course code": "CST308",
        "Sem code": "F",
        "lecture/week": 1,
        "tutorial/week": 0,
        "practical/week": 0,
        "allotted lecturers": ["Angel Thankam Thomas(lecture)", "Betty James(lecture)", "Sreelekshmi K R(lecture)"],
        "batches": "S6D"
    },
    {
        "Course": "Networking Lab",
        "Course code": "CSL332",
        "Sem code": "S",
        "lecture/week": 0,
        "tutorial/week": 0,
        "practical/week": 3,
        "allotted lecturers": ["Betty James(practical)", "Ameena A(practical)", "Anjitha P(practical)"],
        "batches": "S6C"
    },
    {
        "Course": "Networking Lab",
        "Course code": "CSL332",
        "Sem code": "S",
        "lecture/week": 0,
        "tutorial/week": 0,
        "practical/week": 3,
        "allotted lecturers": ["Nasseena N(practical)", "Neethu Treesa Jacob(practical)", "Anjitha P(practical)"],
        "batches": "S6D"
    },
    {
        "Course": "Mini Project",
        "Course code": "CSD334",
        "Sem code": "T",
        "lecture/week": 0,
        "tutorial/week": 0,
        "practical/week": 3,
        "allotted lecturers": ["Syeatha Merlin Thampy(practical)", "Sheerna Thampi(practical)"],
        "batches": "S6C"
    },
{
        "Course": "Mini Project",
        "Course code": "CSD334",
        "Sem code": "T",
        "lecture/week": 0,
        "tutorial/week": 0,
        "practical/week": 3,
        "allotted lecturers": ["Sabhana Mol S(practical)", "Shiny B(practical)", "Rosy K Philp(practical)"],
        "batches": "S6D"
    },
    {
        "Course": "Concepts in Deep Learning",
        "Course code": "CST384",
        "Sem code": "Minor",
        "lecture/week": 3,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Alka Vijay(lecture)", "Alka Vijay(tutorial)"],
        "batches": "S6C"
    },
    {
        "Course": "Network Security",
        "Course code": "CST394",
        "Sem code": "Honours",
        "lecture/week": 3,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Neethu Treesa Jacob(lecture)", "Neethu Treesa Jacob(tutorial)"],
        "batches": "S6C"
    },
    {
        "Course": "Advanced Topics in Machine Learning",
        "Course code": "CST396",
        "Sem code": "Honours",
        "lecture/week": 3,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Angel Thankam Thomas(lecture)", "Angel Thankam Thomas(tutorial)"],
        "batches": "S6C"
    },
    {
        "Course": "Distributed Computing",
        "Course code": "CST402",
        "Sem code": "A",
        "lecture/week": 2,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Chinchu M Pillai(lecture)", "Chinchu M Pillai(practical)"],
        "batches": "S8C"
    },
    {
        "Course": "Distributed Computing",
        "Course code": "CST402",
        "Sem code": "A",
        "lecture/week": 2,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Chinchu M Pillai(lecture)", "Chinchu M Pillai(practical)"],
        "batches": "S8D"
    },
    {
        "Course": "Deep Learning",
        "Course code": "CST414",
        "Sem code": "B-Elective3",
        "lecture/week": 2,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Sushitha Susan Jacob(lecture)", "Sushitha Susan Jacob(tutorial)"],
        "batches": "S8C"
    },
    {
        "Course": "Soft Computing",
        "Course code": "CST444",
        "Sem code": "B-Elective3",
        "lecture/week": 2,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Neethu Treesa Jacob(lecture)", "Neethu Treesa Jacob(tutorial)"],
        "batches": "S8C"
    },
    {
        "Course": "Soft Computing",
        "Course code": "CST444",
        "Sem code": "B-Elective3",
        "lecture/week": 2,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Neethu Treesa Jacob(lecture)", "Neethu Treesa Jacob(tutorial)"],
        "batches": "S8D"
    },
    {
        "Course": "Data Compression Techniques",
        "Course code": "CST446",
        "Sem code": "C-Elective4",
        "lecture/week": 2,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Anjitha P(lecture)", "Anjitha P(tutorial)"],
        "batches": "S8C"
    },
    {
        "Course": "Data Compression Techniques",
        "Course code": "CST446",
        "Sem code": "C-Elective4",
        "lecture/week": 2,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Syeatha Merlin Thampy(lecture)", "Syeatha Merlin Thampy(tutorial)"],
        "batches": "S8D"
    },
    {
        "Course": "Mobile Computing",
        "Course code": "CST476",
        "Sem code": "C-Elective4",
        "lecture/week": 2,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Ameena A(lecture)", "Ameena A(tutorial)"],
        "batches": "S8C"
    },
    {
        "Course": "Blockchain Technologies",
        "Course code": "CST428",
        "Sem code": "D-Elective5",
        "lecture/week": 2,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Vishnu S Kumar(Lecture)", "Vishnu S Kumar(tutorial)"],
        "batches": "S8C"
    },
    {
        "Course": "Blockchain Technologies",
        "Course code": "CST428",
        "Sem code": "D-Elective5",
        "lecture/week": 2,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Vishnu S Kumar(Lecture)", "Vishnu S Kumar(tutorial)"],
        "batches": "S8D"
    },
    {
        "Course": "Internet Of Things",
        "Course code": "CST448",
        "Sem code": "D-Elective5",
        "lecture/week": 2,
        "tutorial/week": 1,
        "practical/week": 0,
        "allotted lecturers": ["Shiny B(Lecture)", "Shiny B(tutorial)"],
        "batches": "S8C"
    },
    {
        "Course": "Comprehensive Course Viva",
        "Course code": "CST404",
        "Sem code": "T",
        "lecture/week": 1,
        "tutorial/week": 0,
        "practical/week": 0,
        "allotted lecturers": ["Sreelekshmi K R (lecture)", "Neethu Treesa Jacob(lecture)", "Gopakumar G(lecture)"],
        "batches": "S8C"
    },
    {
        "Course": "Comprehensive Course Viva",
        "Course code": "CST404",
        "Sem code": "T",
        "lecture/week": 1,
        "tutorial/week": 0,
        "practical/week": 0,
        "allotted lecturers": ["Ameena A(lecture)", "Betty James(lecture)", "Alka Vijay(lecture)"],
        "batches": "S8D"
    },
    {
        "Course": "Project Phase II",
        "Course code": "CSD416",
        "Sem code": "U",
        "lecture/week": 0,
        "tutorial/week": 0,
        "practical/week": 12,
        "allotted lecturers": ["Chinchu M Pillai(practical)", "Ahammed Siraj K K(practical)", "Sulaja Sanal(practical)"],
        "batches": "S8C"
    },
    {
        "Course": "Project Phase II",
        "Course code": "CSD416",
        "Sem code": "U",
        "lecture/week": 0,
        "tutorial/week": 0,
        "practical/week": 12,
        "allotted lecturers": ["Leya G(practical)", "Ahammed Siraj K K(practical)", "Vishnu S Kumar(practical)"],
        "batches": "S8D"
    }
]




# Combine teacher names with courses
combined_data = []
for course in courses:
    lecturers = []
    for lecturer in course["allotted lecturers"]:
        teacher_name = lecturer.split("(")[0]
        lecturers.append({"teacher_name": teacher_name, "teacher_code": teacher_codes.get(teacher_name)})
    course["lecturers"] = lecturers
    combined_data.append(course)

# Write combined data to JSON file (can be modified to write other formats)
with open("combined_data.json", "w") as outfile:
    json.dump(combined_data, outfile, indent=4)

print("Combined data written to combined_data.json")