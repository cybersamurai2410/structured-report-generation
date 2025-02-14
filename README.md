# Structured Report Generation
Structured report generation using LLM powered agentic AI for any given topic by automatically planning then conducting research and writing sections simultaneously with concurrent processing. Integrated TTS API using the report to generate podcasts in audio format with language translation.  

The Agent takes in user defined topics and structure, then plans the topics of the section indicated in the structure. The Agent then perform web search on the given topics and uses this information to write the sections and synthesize the final report. The report is written in strategic sequence by writing research-based sections in parallel then write introductions and conclusions afterwards before connecting each of the sections.

View example of generated report [final_report.md](final_report.md)

This project uses [o3-mini](https://platform.openai.com/docs/models#o3-mini) reasoning model via OpenAI API for the planning phase then [llama-3.3-70b](https://build.nvidia.com/meta/llama-3_3-70b-instruct) LLM via NVIDIA NIM API and Tavily API for the research and report writing phase.

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
<img width="1916" alt="image" src="https://github.com/user-attachments/assets/4564635b-2567-445e-a88f-0adc50730b42" />

## Application UI
<img width="936" alt="image" src="https://github.com/user-attachments/assets/030c47c3-510a-4632-93e4-13b92f101f8e" />
