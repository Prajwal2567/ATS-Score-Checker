def calculate_ats_score(skills, raw_text):

    score = 0

    # SKILL SCORE
    score += len(skills) * 5

    # KEYWORDS
    keywords = [
        "project",
        "experience",
        "certification",
        "internship",
        "achievement",
        "teamwork"
    ]

    for word in keywords:

        if word in raw_text.lower():
            score += 5

    # RESUME LENGTH
    word_count = len(raw_text.split())

    if word_count > 300:
        score += 10

    # LIMIT SCORE
    if score > 100:
        score = 100

    return score