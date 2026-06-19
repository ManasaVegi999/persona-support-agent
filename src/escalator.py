def should_escalate(query):
    sensitive_words = ["refund", "legal", "complaint"]

    return any(word in query.lower() for word in sensitive_words)
