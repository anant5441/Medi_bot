from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn
from ai_agent import graph, SYSTEM_PROMPT, parse_response

app = FastAPI()

class Query(BaseModel):
    message: str

@app.post("/ask")
async def ask_question(query: Query):
    inputs = {"messages": [("system", SYSTEM_PROMPT), ("user", query.message)]}
    
    stream = graph.stream(inputs, stream_mode="updates")
    tool_called_name, final_response = parse_response(stream)

    # Step3: Send response to the frontend
    return {"response": final_response,
            "tool_called": tool_called_name}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)