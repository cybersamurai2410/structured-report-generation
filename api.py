from fastapi import FastAPI
from main import generate_report, podcast_from_report
from mangum import Mangum  # AWS Lambda adapter

app = FastAPI()

@app.post("/generate_report")
async def generate_report_api(report_topic: str, number_of_queries: int = 2):
    report = await generate_report(report_topic, number_of_queries)
    return {"report": report.get("final_report", "Report generation failed")}

@app.post("/podcast_from_report")
async def podcast_from_report_api(voice: str = "", language: str = "en", duration: int = 1):
    await podcast_from_report(voice, language, duration)
    return {"message": "Podcast generated successfully"}

# AWS Lambda Handler
handler = Mangum(app)
