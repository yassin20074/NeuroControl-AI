from fastapi import FastAPI, Depends
from pydantic import BaseModel
from auth import (
    create_user,
    authenticate_user,
    create_access_token,
    get_current_user
)
from agent import assistant
from executor import execute
from memory_short import add_to_short_memory, get_short_memory
from memory_vector import store_vector, retrieve_vector
from context_builder import build_context

app = FastAPI(title="NeuroControl Secure AI")

class UserRegister(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserInput(BaseModel):
    message: str
    session_id: str

# Register
@app.post("/register")
def register(user: UserRegister):
    create_user(user.username, user.password)
    return {"msg": "User created successfully"}

# Login
@app.post("/login")
def login(user: UserLogin):
    db_user = authenticate_user(user.username, user.password)
    if not db_user:
        return {"error": "Invalid credentials"}

    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token}

# Secure AI Endpoint
@app.post("/ask")
def ask_ai(data: UserInput, current_user: str = Depends(get_current_user)):

    # Session ownership check
    if not data.session_id.startswith(current_user):
        return {"error": "Unauthorized session access"}

    short_mem = get_short_memory(data.session_id)
    vector_mem = retrieve_vector(data.session_id, data.message)

    full_prompt = build_context(short_mem, vector_mem, data.message)

    ai_response = assistant.run(full_prompt)
    result = execute(ai_response, data.session_id, data.message)

    add_to_short_memory(data.session_id, "User", data.message)
    add_to_short_memory(data.session_id, "Assistant", ai_response)

    store_vector(data.session_id, f"User: {data.message}")
    store_vector(data.session_id, f"Assistant: {ai_response}")

    return {
        "ai_response": ai_response,
        "system_result": result
    }
