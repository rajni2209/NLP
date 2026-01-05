import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import PromptRequest
from service.openai import Call_openai
from service.claude import Call_claude
from service.gemmini import Call_gemmini

app = FastAPI(title="LLM Comparison API")

@app.post9("/compare")
async def compare_llms(data: PromptRequest):
    prompt = data.prompt
    
    loop = asyncio.get_event_loop()

    openai_task = loop.run_in_executor(None, Call_openai, prompt)
    claude_task = loop.run_in_executor(None, Call_claude, prompt)
    gemmini_task = loop.run_in_executor(None, Call_gemmini, prompt)

    openai_response, claude_response, gemmini_response = await asyncio.gather(
        openai_task, claude_task, gemmini_task
    )
    return {
        "openai": openai_response,
        "claude": claude_response,
        "gemmini": gemmini_response
    }