def generate_response(persona, query):
    if persona == "Technical Expert":
        return f"Technical Response: {query}"

    elif persona == "Frustrated User":
        return f"I understand your concern. Let's resolve: {query}"

    else:
        return f"Business Summary: {query}"
