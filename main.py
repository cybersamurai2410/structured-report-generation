from planning import generate_report_plan
from research_writer import section_builder_graph, graph

import os 
import base64
import translators as ts
from elevenlabs.client import ElevenLabs
from openai import OpenAI

oai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
el_client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

# Tavily search parameters
tavily_topic = "general"
tavily_days = None # Only applicable for news topic instead of general

# Topic 
report_topic = "Give an overview of capabilities and specific use case examples for these processing units: CPU, GPU."

# Structure
plan_report_structure = """This report type focuses on comparative analysis.

The report structure should include:
1. Introduction (no research needed)
   - Brief overview of the topic area
   - Context for the comparison

2. Main Body Sections:
   - One dedicated section for EACH offering being compared in the user-provided list
   - Each section should examine:
     - Core Features (bulleted list)
     - Architecture & Implementation (2-3 sentences)
     - One example use case (2-3 sentences)
   
3. No Main Body Sections other than the ones dedicated to each offering in the user-provided list

4. Conclusion with Comparison Table (no research needed)
   - Structured comparison table that:
     * Compares all offerings from the user-provided list across key dimensions
     * Highlights relative strengths and weaknesses
   - Final recommendations"""

# Structure
report_structure = """This report type focuses on comparative analysis.

The report structure should include:
1. Introduction (no research needed)
   - Brief overview of the topic area
   - Context for the comparison

2. Main Body Sections:
   - One dedicated section for EACH offering being compared in the user-provided list
   - Each section should examine:
     - Core Features (bulleted list)
     - Architecture & Implementation (2-3 sentences)
     - One example use case (2-3 sentences)
   
3. No Main Body Sections other than the ones dedicated to each offering in the user-provided list

4. Conclusion with Comparison Table (no research needed)
   - Structured comparison table that:
     * Compares all offerings from the user-provided list across key dimensions
     * Highlights relative strengths and weaknesses
   - Final recommendations"""

async def display_plan():
    # Generate report plan
    sections = await generate_report_plan({
        "topic": report_topic, 
        "report_structure": plan_report_structure, 
        "number_of_queries": 2, 
        "tavily_topic": tavily_topic, 
        "tavily_days": tavily_days
        })

    # Print sections
    for section in sections['sections']:
        print(f"{'='*50}")
        print(f"Name: {section.name}")
        print(f"Description: {section.description}")
        print(f"Research: {section.research}")
    
    return sections

async def display_section(plan):
    # Test with one section
    sections = plan['sections'] 
    test_section = sections[1]
    print(f"{'='*50}")
    print(f"Name: {test_section.name}")
    print(f"Description: {test_section.description}")
    print(f"Research: {test_section.research}")
    print()

    # Run section builder
    report_section = await section_builder_graph.ainvoke({
        "section": test_section, 
        "number_of_queries": 2, 
        "tavily_topic": tavily_topic, 
        "tavily_days": tavily_days
    })
    section = report_section['completed_sections'][0]
    
    return section

async def generate_report():
    report = await graph.ainvoke({ # The other parameters from ReportState class are populated during the execution 
        "topic": report_topic, 
        "report_structure": report_structure, 
        "number_of_queries": 2, 
        "tavily_topic": tavily_topic, 
        "tavily_days": tavily_days
    })
    
    try:
        report_text = report["final_report"]
        with open("report.md", "w", encoding="utf-8") as file:
            file.write(report_text)
    except Exception as e:
        print(f"[WARNING] Could not write to file: {e}")

    return report

async def podcast_from_report(voice="", language="en", duration=1):
    with open("report.md", "r", encoding="utf-8") as md_file:
        report_text = md_file.read()
    
    if language.lower() != "en":
        report_text = ts.deepl(report_text, to_language=language)

    completion = oai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "developer", "content": "You are an expert personal tutor turning written reports into professional spoken lectures."},
            {"role": "user", "content": f"Convert this report into a well-structured spoken lecture with duration around {duration} minutes:\n\n{report_text}"}
        ]
    )
    speech_script = completion.choices[0].message.content

    audio = el_client.text_to_speech.convert_with_timestamps( # dict_keys(['audio_base64', 'alignment', 'normalized_alignment'])
        voice_id=voice,
        output_format="mp3_44100_128",
        text=speech_script,
        model_id="eleven_multilingual_v2"
    )

    audio_base64 = audio["audio_base64"]  # Extract Base64 MP3
    audio_bytes = base64.b64decode(audio_base64)  # Decode into MP3 bytes

    # Save MP3 file
    with open("speech_script_el.mp3", "wb") as audio_file:
        audio_file.write(audio_bytes)

async def main():
    plan = await display_plan()

    section = await display_section(plan)
    print(section.content, "\n")

    report = await generate_report()
    print(report)

    await podcast_from_report(voice="JBFqnCBsd6RMkjVDRZzb", language="en")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main()) # Start event loop 
