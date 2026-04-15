student = {
    'name': 'Kamron1k',
    'id': '900954459',
    'course': 'CSV17',
    'grade': 'A'
}

h = {10: 'x', 20: 'y', 30: 'x', 40: 'z'}

domain = set(h.keys())
range = set(h.values())

course = [
    {'CRN': 'CSV17', 'CourseTitle': 'Discrete Structures', 'CourseCredit': 3, 'CourseGrade': 'A'},
    {'CRN': 'CSV09', 'CourseTitle': 'Intro to Computer Science', 'CourseCredit': 3, 'CourseGrade': 'B'},
    {'CRN': 'CSV42', 'CourseTitle': 'Data Structures', 'CourseCredit': 3, 'CourseGrade': 'A'},
    {'CRN': 'CSV11', 'CourseTitle': 'Intro to Programming', 'CourseCredit': 3, 'CourseGrade': 'B'}
]

for c in course:
    if c['CourseGrade'] == 'A':
        c['CourseCredit'] = 4

total = 0
for c in course:
    if 'Python' in c['CourseTitle']:
        total += c['CourseCredit']

keys = ['CRN', 'CourseTitle', 'CourseCredit', 'CourseGrade']
values = [
    ['CSV17', 'Discrete Structures', 3, 'A'],
    ['CSV09', 'Intro to Computer Science', 3, 'B'],
    ['CSV42', 'Data Structures', 3, 'A'],
    ['CSV11', 'Intro to Programming', 3, 'B']
]

course_zip = [dict(zip(keys, v)) for v in values]