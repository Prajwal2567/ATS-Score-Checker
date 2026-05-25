import joblib
import pandas as pd

# LOAD TRAINED MODEL
model = joblib.load("hiring_model.pkl")

# PREDICTION FUNCTION
def predict_hiring(
    cgpa,
    internships,
    projects,
    experience_years,
    hackathons,
    research_papers,
    skills_score,
    soft_skills_score,
    resume_length_words
):

    # CREATE DATAFRAME
    data = pd.DataFrame([[
        cgpa,
        internships,
        projects,
        experience_years,
        hackathons,
        research_papers,
        skills_score,
        soft_skills_score,
        resume_length_words
    ]], columns=[

        'cgpa',
        'internships',
        'projects',
        'experience_years',
        'hackathons',
        'research_papers',
        'skills_score',
        'soft_skills_score',
        'resume_length_words'
    ])

    # PREDICT
    prediction = model.predict(data)

    return prediction[0]