# Structured Report Generation
Structured report generation using agentic AI for any given topic by automatically planning then conducting research and writing sections simultaneously with concurrent processing.

The Agent takes in user defined topics and structure, then plans the topics of the section indicated in the structure. The Agent then perform web search on the given topics and uses this information to write the sections and synthesize the final report. The report is written in strategic sequence by writing research-based sections in parallel then write introductions and conclusions afterwards before connecting each of the sections. 

This project uses [llama-3.3-70b](https://build.nvidia.com/meta/llama-3_3-70b-instruct) via NVIDIA NIM API for invoking the LLM and Tavily API for web search.

**Phase 1 - Planning**
* Analyzes user inputs
* Maps out report sections

**Phase 2 - Research**
* Conducts parallel web research
* Processes relevant data for each section

## Architecture
The architecture of this project is inspired and adapted from this repository [Report mAIstro](https://github.com/langchain-ai/report-mAIstro) 

![image](https://github.com/user-attachments/assets/a1cb48e6-55bc-4217-834d-d2d8fe7ab6c4)
<p align="center">
  <img src="https://github.com/user-attachments/assets/d60fd48a-67b7-443f-8b36-c38a3ec6cfe5" width="179" alt="image">
</p>
