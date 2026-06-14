def calculate_ats_score(sections):

    score = 40

    if sections["Education"]:
        score += 10

    if sections["Skills"]:
        score += 10

    if sections["Projects"]:
        score += 10

    if sections["Internship"]:
        score += 10

    if sections["Experience"]:
        score += 10

    if sections["Certification"]:
        score += 10

    return min(score, 100)