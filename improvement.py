def get_resume_suggestions(skills, raw_text):

    suggestions = []

    text = raw_text.lower()

    word_count = len(raw_text.split())

    # =====================================================
    # TECHNICAL SKILLS CHECK
    # =====================================================

    if len(skills) < 5:

        suggestions.append(
            "Add more technical skills such as Python, SQL, Machine Learning, Power BI, or Cloud technologies."
        )

    # =====================================================
    # PROJECT SECTION
    # =====================================================

    if "project" not in text:

        suggestions.append(
            "Add academic or real-world project experience to strengthen your resume."
        )

    # =====================================================
    # CERTIFICATIONS
    # =====================================================

    if "certification" not in text and "certificate" not in text:

        suggestions.append(
            "Include certifications from platforms like Coursera, Udemy, Google, AWS, or Microsoft."
        )

    # =====================================================
    # INTERNSHIP
    # =====================================================

    if "internship" not in text:

        suggestions.append(
            "Add internship experience to improve practical exposure and hiring chances."
        )

    # =====================================================
    # EXPERIENCE
    # =====================================================

    if "experience" not in text:

        suggestions.append(
            "Mention work experience, freelance work, or practical contributions if available."
        )

    # =====================================================
    # ACHIEVEMENTS
    # =====================================================

    if "achievement" not in text and "award" not in text:

        suggestions.append(
            "Add achievements, hackathons, coding competitions, or awards."
        )

    # =====================================================
    # GITHUB / PORTFOLIO
    # =====================================================

    if "github" not in text and "portfolio" not in text:

        suggestions.append(
            "Include GitHub or portfolio links to showcase your projects and coding skills."
        )

    # =====================================================
    # LINKEDIN
    # =====================================================

    if "linkedin" not in text:

        suggestions.append(
            "Add your LinkedIn profile to improve professional visibility."
        )

    # =====================================================
    # RESUME LENGTH
    # =====================================================

    if word_count < 250:

        suggestions.append(
            "Resume content is too short. Add more details about projects, skills, and experience."
        )

    elif word_count > 1000:

        suggestions.append(
            "Resume is too lengthy. Keep it concise and focused on relevant skills and achievements."
        )

    # =====================================================
    # COMMUNICATION SKILLS
    # =====================================================

    communication_words = [
        "communication",
        "leadership",
        "teamwork",
        "presentation"
    ]

    found_soft_skills = False

    for word in communication_words:

        if word in text:
            found_soft_skills = True

    if not found_soft_skills:

        suggestions.append(
            "Add soft skills like communication, teamwork, leadership, and problem solving."
        )

    # =====================================================
    # EDUCATION
    # =====================================================

    if "education" not in text and "university" not in text:

        suggestions.append(
            "Clearly mention your education details, CGPA, and university information."
        )

    # =====================================================
    # ATS KEYWORDS
    # =====================================================

    ats_keywords = [
        "python",
        "sql",
        "machine learning",
        "data analysis",
        "cloud",
        "api"
    ]

    missing_keywords = []

    for keyword in ats_keywords:

        if keyword not in text:

            missing_keywords.append(keyword)

    if missing_keywords:

        suggestions.append(
            "Improve ATS score by adding keywords like: " +
            ", ".join(missing_keywords[:5])
        )

    # =====================================================
    # FINAL QUALITY CHECK
    # =====================================================

    if len(suggestions) == 0:

        suggestions.append(
            "Excellent resume. Your profile looks strong for technical roles."
        )

    return suggestions