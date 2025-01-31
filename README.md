# Structured Report Generation
Structured report generation using LLM powered agentic AI for any given topic by automatically planning then conducting research and writing sections simultaneously with concurrent processing. Integrated TTS API using the report to generate podcasts in audio format.  

The Agent takes in user defined topics and structure, then plans the topics of the section indicated in the structure. The Agent then perform web search on the given topics and uses this information to write the sections and synthesize the final report. The report is written in strategic sequence by writing research-based sections in parallel then write introductions and conclusions afterwards before connecting each of the sections.

View example of generated report [final_report.md](final_report.md)

This project uses [llama-3.3-70b](https://build.nvidia.com/meta/llama-3_3-70b-instruct) via NVIDIA NIM API for invoking the LLM and Tavily API for web search.

## Agentic Workflow
**Phase 1 - Planning**
* Analyzes user inputs
* Maps out report sections

**Phase 2 - Research**
* Conducts parallel web research
* Processes relevant data for each section

## Architecture
The architecture of this project is inspired and adapted from this repository [Report mAIstro](https://github.com/langchain-ai/report-mAIstro) 

![image](https://github.com/user-attachments/assets/a1cb48e6-55bc-4217-834d-d2d8fe7ab6c4)

### LangGraph Agentic Workflow:

![image](https://github.com/user-attachments/assets/dcf187d7-9c28-4023-a06f-2b5b148ce0cb)

## LangSmith Tracing  
