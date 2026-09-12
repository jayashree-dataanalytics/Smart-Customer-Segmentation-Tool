import json


from google import genai




def prepare_segment_data(segment_summary):
    """
    Convert the segment summary DataFrame
    into JSON for the AI model.
    """


    segment_data = segment_summary.to_dict(
        orient="records"
    )


    return json.dumps(
        segment_data,
        indent=2,
        default=str
    )




def generate_insights(segment_summary, api_key):
    """
    Send segment summary to Gemini
    and generate business insights.
    """


    # Create Gemini client
    client = genai.Client(
        api_key=api_key
    )


    # Convert DataFrame to JSON
    segment_data = prepare_segment_data(
        segment_summary
    )


    # Business-focused prompt
    prompt = f"""
You are a business analyst for an e-commerce company.


Analyze the following customer segment summary:


{segment_data}


Provide a concise business analysis covering:


1. Key observations
2. Most valuable customer segment
3. Segment that needs attention
4. Marketing recommendations
5. Suggested business actions


Use simple, practical business language.


Important:
- Use only the information provided.
- Do not invent numbers.
- Mention relevant numbers when useful.
- Keep the response concise and easy to understand.
"""


    # Generate response
    response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)


    return response.text

