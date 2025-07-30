from langchain_core.prompts import PromptTemplate


# instead of using template in the main code we can use it directly from this file and can import to any file we require

#template

template = PromptTemplate(
    template = """
    Please summarize the research paper titled "{paper_input}" with the following specifications:
    Explanation Style: {style_input}
    Explanation Length: {length_input}
    1. Mathematical Details:
        - Include relevent math equations if present in paper.
        - Explain mathematical concepts using simple, intuative code snippets where applicable.
    2. Analogies:
        - Use relatable analogies to simplify complex concepts.
    IF certain info is not available in paper, respond with "insufficient infor" instead of guessing.
    Ensure the summary is clear, accurate and aligned with provided style and length.
""",
input_variables = ['paper_input', 'style_input', 'length_input'],
validate_template= True  # Checks if all the inputs are also in input_variable isn't there and less or more
)

template.save('template.json')