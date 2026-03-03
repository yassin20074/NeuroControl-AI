#Retrieve the required libraries 
import json
from Tools import *
from logger import log_full_event

#Create Tools
Tools= {
    "open_notepad": open_notepad,
    "open_calculator": open_calculator,
    "get_system_info": get_system_info,
    "list_files": list_files,
}

def execute(response, session_id, user_msg):
    try:
        command = json.loads(response)
        action = command.get("action") #Bring Actions

        if action == "none":
            log_full_event(session_id, user_msg, response, "none") #Save results in logging
            return command.get("message")

        if action in TOOLS:
            result = TOOLS[action]()
            log_full_event(session_id, user_msg, response, action)
            return result if result else "Executed successfully"

        return "Unauthorized action."

    except Exception as e:
        log_full_event(session_id, user_msg, response, f"Error: {e}")
        return f"Execution Error: {e}"
