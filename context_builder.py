#Building the final Prompt that will be sent to the LLM 
def build_context(short_mem, vector_mem, user_message, max_vector=3):

    context = "=== Recent Conversation ===\n"

    for role, msg in short_mem[-6:]:
        context += f"{role}: {msg}\n"

    context += "\n=== Relevant Past Memory ===\n"

    for mem in vector_mem[:max_vector]:
        context += f"{mem}\n"

    context += f"\nUser: {user_message}\n"

    return context
