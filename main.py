# =========================
# Student Dictionary (0-0)
# =========================
student = {
    'name': 'Kamron1k',
    'id': '900954459',
    'course': 'CSV17',
    'grade': 'A'
}

print(student)


# =========================
# 0-1 Domain and Range
# =========================
h = {10: 'x', 20: 'y', 30: 'x', 40: 'z'}

domain = set(h.keys())
range_vals = set(h.values())

print(domain)
print(range_vals)
print(len(range_vals))


# =========================
# 0-2 Traversal
# =========================
for k in h:
    print(k, "→", h[k])


# =========================
# 0-3 Membership
# =========================
print(20 in h)
print('w' in h.values())
print('x' in h.values())


# =========================
# 1.0 Course Dictionary
# =========================
course_info = {
    'CRN': 'CSV17',
    'CourseTitle': 'Discrete Structures',
    'CourseCredit': 3,
    'CourseGrade': 'A'
}

print(course_info)


# =========================
# 1.1 List of Dictionaries
# =========================
course = [
    {'CRN': 'CSV17', 'CourseTitle': 'Discrete Structures', 'CourseCredit': 3, 'CourseGrade': 'A'},
    {'CRN': 'CSV09', 'CourseTitle': 'Intro to Computer Science', 'CourseCredit': 3, 'CourseGrade': 'B'},
    {'CRN': 'CSV42', 'CourseTitle': 'Data Structures', 'CourseCredit': 3, 'CourseGrade': 'A'},
    {'CRN': 'CSV11', 'CourseTitle': 'Intro to Programming', 'CourseCredit': 3, 'CourseGrade': 'B'}
]

print(course)


# =========================
# 1.2 Change credits for A grades
# =========================
for c in course:
    if c['CourseGrade'] == 'A':
        c['CourseCredit'] = 4

print(course)


# =========================
# 1.3 Sum credits for Python courses
# =========================
total = 0

for c in course:
    if 'Python' in c['CourseTitle']:
        total += c['CourseCredit']

print(total)


# =========================
# 1.4 Build dictionary using zip
# =========================
keys = ['CRN', 'CourseTitle', 'CourseCredit', 'CourseGrade']
values = [
    ['CSV17', 'Discrete Structures', 3, 'A'],
    ['CSV09', 'Intro to Computer Science', 3, 'B'],
    ['CSV42', 'Data Structures', 3, 'A'],
    ['CSV11', 'Intro to Programming', 3, 'B']
]

course_zip = []

for v in values:
    course_zip.append(dict(zip(keys, v)))

print(course_zip)