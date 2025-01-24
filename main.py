from planning import generate_report_plan
from research_writer import section_builder_graph, graph

# Tavily search parameters
tavily_topic = "general"
tavily_days = None # Only applicable for news topic

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

# Topic 
plan_report_topic = "Give an overview of capabilities and specific use case examples for these processing units: CPU, GPU."

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

# Topic 
report_topic = "Give an overview of capabilities and specific use case examples for these processing units: CPU, GPU."

async def display_plan():
    # Generate report plan
    sections = await generate_report_plan({"topic": plan_report_topic, "report_structure": plan_report_structure, "number_of_queries": 2, "tavily_topic": tavily_topic, "tavily_days": tavily_days})

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
    report = await graph.ainvoke({
        "topic": report_topic, 
        "report_structure": report_structure, 
        "number_of_queries": 2, 
        "tavily_topic": tavily_topic, 
        "tavily_days": tavily_days
    })
    
    with open("report.md", "w", encoding="utf-8") as file:
        file.write(report)

    return report

async def main():
    plan = await display_plan()

    section = await display_section(plan)
    print(section.content, "\n")

    report = await generate_report()
    print(report)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
