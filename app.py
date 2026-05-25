import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from interview_questions import generate_questions
from improvement import get_resume_suggestions
from ats_score import calculate_ats_score
from hiring_prediction import predict_hiring

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from model import extract_text
from preprocess import clean_text
from skills import extract_skills


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* MAIN BACKGROUND */
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a,
        #111827,
        #020617
    );
    color: white;
}

/* REMOVE SPACE */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* TITLE */
.main-title {
    text-align: center;
    font-size: 52px;
    font-weight: bold;
    color: white;
}

.sub-title {
    text-align: center;
    color: #94A3B8;
    font-size: 18px;
    margin-bottom: 40px;
}

/* CARD */
.card {

    background: rgba(255,255,255,0.05);

    border: 1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(10px);

    border-radius: 20px;

    padding: 25px;

    margin-bottom: 25px;

    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
}

/* BUTTON */
.stButton > button {

    width: 100%;

    border-radius: 12px;

    border: none;

    background: linear-gradient(
        90deg,
        #2563EB,
        #7C3AED
    );

    color: white;

    font-size: 16px;

    font-weight: 600;

    height: 3em;
}

/* SKILL BOX */
.skill-box {

    display: inline-block;

    padding: 10px 18px;

    margin: 6px;

    border-radius: 30px;

    background: linear-gradient(
        90deg,
        #0EA5E9,
        #2563EB
    );

    color: white;

    font-size: 14px;

    font-weight: 600;
}

/* SIDEBAR */
[data-testid="stSidebar"] {

    background: #111827;
}

/* PROGRESS BAR */
.stProgress > div > div > div > div {

    background: linear-gradient(
        90deg,
        #06B6D4,
        #3B82F6,
        #8B5CF6
    );
}

/* FOOTER */
.footer {

    text-align: center;

    color: #94A3B8;

    margin-top: 30px;

    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================

st.markdown("""

<div class="main-title">
AI Resume Screening System
</div>

<div class="sub-title">
AI + NLP + Machine Learning Based Smart Hiring Platform
</div>

""", unsafe_allow_html=True)

# =========================================================
# LOAD JOB DATASET
# =========================================================

jobs = pd.read_csv("dataset/jobs.csv")

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown("## About Project")

st.sidebar.markdown("""

This intelligent AI system:

✔ Extracts resume skills automatically

✔ Matches resumes with jobs

✔ Uses NLP + Machine Learning

✔ Predicts hiring probability

✔ Detects missing skills

✔ Generates interview questions

✔ Gives ATS resume score

""")

# =========================================================
# FILE UPLOAD
# =========================================================

uploaded_file = st.file_uploader(
    "📄 Upload Resume PDF",
    type=["pdf"]
)

# =========================================================
# MAIN SYSTEM
# =========================================================

if uploaded_file:

    # EXTRACT TEXT
    raw_text = extract_text(uploaded_file)

    # CLEAN TEXT
    cleaned_resume = clean_text(raw_text)

    # EXTRACT SKILLS
    skills = extract_skills(cleaned_resume)

    # ATS SCORE
    ats_score = calculate_ats_score(
        skills,
        raw_text
    )

    # =====================================================
    # TOP SECTION
    # =====================================================

    col1, col2 = st.columns(2)

    # LEFT SIDE
    with col1:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader("📄 Resume Preview")

        st.write(raw_text[:1500])

        st.markdown('</div>', unsafe_allow_html=True)

    # RIGHT SIDE
    with col2:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader("📊 ATS Resume Score")

        st.progress(ats_score)

        st.success(f"ATS Resume Score: {ats_score}%")

        st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # SKILLS
    # =====================================================

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🛠 Skills Extracted")

    if skills:

        for skill in skills:

            st.markdown(
                f'<span class="skill-box">{skill}</span>',
                unsafe_allow_html=True
            )

    else:
        st.warning("No skills detected")

    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # JOB MATCHING
    # =====================================================

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("💼 Recommended Jobs")

    results = []

    for index, row in jobs.iterrows():

        role = row['Job_Role']

        content = row['Skills'] + " " + row['Description']

        vectorizer = TfidfVectorizer()

        vectors = vectorizer.fit_transform([
            cleaned_resume,
            content
        ])

        similarity = cosine_similarity(vectors)[0][1]

        score = round(similarity * 100, 2)

        results.append((role, score))

    # SORT RESULTS
    results = sorted(
        results,
        key=lambda x: x[1],
        reverse=True
    )

    # SHOW RESULTS
    for role, score in results[:5]:

        st.success(f"{role} — {score}% Match")

    # BEST JOB
    best_role = results[0]

    st.success(
        f"🎯 Best Job Recommendation: {best_role[0]}"
    )

    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # GRAPH
    # =====================================================

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📈 Job Matching Analysis")

    labels = [x[0] for x in results[:5]]

    values = [x[1] for x in results[:5]]

    fig, ax = plt.subplots(figsize=(10,5))

    bars = ax.bar(labels, values)

    ax.set_facecolor("#111827")

    fig.patch.set_facecolor("#111827")

    ax.set_xlabel("Job Roles", color="white")

    ax.set_ylabel("Match %", color="white")

    ax.tick_params(colors='white')

    plt.xticks(rotation=15)

    st.pyplot(fig)

    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # SKILL GAP ANALYSIS
    # =====================================================

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📚 Skill Gap Analysis")

    required_skills = [
        "machine learning",
        "sql",
        "pandas"
    ]

    missing_skills = []

    resume_text_lower = cleaned_resume.lower()

    for skill in required_skills:

        if skill.lower() not in resume_text_lower:

            missing_skills.append(skill)

    if missing_skills:

        for skill in missing_skills:

            st.error(f"Missing Skill: {skill}")

    else:

        st.success("No major skill gaps detected")

    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # AI HIRING PREDICTION
    # =====================================================

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🤖 AI Hiring Prediction")

    cgpa = 8.0
    internships = 2
    projects = 3
    experience_years = 1
    hackathons = 2
    research_papers = 1
    skills_score = ats_score
    soft_skills_score = 75
    resume_length_words = len(raw_text.split())

    prediction = predict_hiring(

        cgpa,
        internships,
        projects,
        experience_years,
        hackathons,
        research_papers,
        skills_score,
        soft_skills_score,
        resume_length_words
    )

    if prediction == 1:

        st.success("✅ Candidate Has HIGH Hiring Probability")

    else:

        st.error("❌ Candidate Has LOW Hiring Probability")

    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # RESUME SUGGESTIONS
    # =====================================================

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🧠 AI Resume Suggestions")

    suggestions = get_resume_suggestions(
        skills,
        raw_text
    )

    if suggestions:

        for s in suggestions:

            st.warning(s)

    else:

        st.success("Excellent Resume")

    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # INTERVIEW QUESTIONS
    # =====================================================

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🎤 AI Interview Questions")

    questions = generate_questions(skills)

    if questions:

        for q in questions:

            st.info(q)

    else:

        st.warning("No interview questions generated")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("""

<div class="footer">

Developed using Artificial Intelligence, Machine Learning & NLP

</div>

""", unsafe_allow_html=True)