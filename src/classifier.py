def classify_persona(user_query):
    query = user_query.lower()

    if any(word in query for word in ["error", "api", "database", "token"]):
        return "Technical Expert"

    elif any(word in query for word in ["angry", "frustrated", "issue", "problem"]):
        return "Frustrated User"

    else:
        return "Business Executive"
