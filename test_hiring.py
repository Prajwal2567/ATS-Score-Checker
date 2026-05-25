from hiring_prediction import predict_hiring

result = predict_hiring(

    cgpa=8.5,
    internships=2,
    projects=4,
    experience_years=1,
    hackathons=3,
    research_papers=1,
    skills_score=85,
    soft_skills_score=80,
    resume_length_words=700

)

print("Hiring Prediction:", result)