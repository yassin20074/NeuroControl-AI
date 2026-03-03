import logging
import json
import time

logging.basicConfig(
    filename="system.log",
    level=logging.INFO
)
#construction log
def log_full_event(session_id, user_msg, ai_response, action, status="success", latency=None):

    log_data = {
        "session_id": session_id,
        "user_message": user_msg,
        "ai_response": ai_response,
        "action": action,
        "status": status,
        "latency": latency,
        "timestamp": time.time()
    }

    logging.info(json.dumps(log_data))
