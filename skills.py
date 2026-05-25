skills_list = [

    "python",
    "sql",
    "machine learning",
    "deep learning",
    "data science",
    "pandas",
    "numpy",
    "tensorflow",
    "power bi",
    "tableau",
    "excel",
    "nlp",
    "computer vision"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    skills_list = [

        "python",
        "sql",
        "machine learning",
        "deep learning",
        "data science",
        "pandas",
        "numpy",
        "tensorflow",
        "power bi",
        "tableau",
        "excel",
        "nlp",
        "computer vision"
    ]

    for skill in skills_list:

        if skill in text:
            found_skills.append(skill)

    return found_skills