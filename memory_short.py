from collections import defaultdict

short_memory = defaultdict(list)
MAX_SHORT_MEMORY = 6 #maximum 

def add_to_short_memory(session_id, role, message):
    short_memory[session_id].append((role, message))

    if len(short_memory[session_id]) > MAX_SHORT_MEMORY:
        short_memory[session_id].pop(0)

def get_short_memory(session_id):
    return short_memory[session_id]
