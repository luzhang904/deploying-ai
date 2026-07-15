import gradio as gr
from openai import OpenAI

from guardrails import check_guardrails
from memory import add_memory

from services.weather_service import get_weather
from services.semantic_service import semantic_search
from services.calculator_service import calculate



client=OpenAI()


SYSTEM_PROMPT="""

You are Nova, a friendly AI research assistant.

You can:
1. Answer general questions
2. Provide weather information
3. Search knowledge documents
4. Calculate math expressions

Keep answers concise and friendly.

"""



def chat(message, history):


    allowed,reason=check_guardrails(message)


    if not allowed:
        return reason



    lower=message.lower()



    # Service 1
    if "weather" in lower:

        if "toronto" in lower:

            answer=get_weather("Toronto")

        elif "new york" in lower:

            answer=get_weather("New York")

        else:

            answer="Please specify Toronto or New York."


    # Service 3
    elif any(
        symbol in message
        for symbol in ["+","-","*","/"]
    ):

        answer=calculate(message)



    # Service 2
    elif (
        "what is chromadb" in lower
        or "what is langchain" in lower
        or "semantic" in lower
        or "embedding" in lower
    ):

        answer=semantic_search(message)


    else:


        response=client.chat.completions.create(

            model="gpt-4o-mini",

            messages=[
                {
                    "role":"system",
                    "content":SYSTEM_PROMPT
                },

                {
                    "role":"user",
                    "content":message
                }
            ]
        )


        answer=response.choices[0].message.content



    add_memory(message,answer)


    return answer



demo=gr.ChatInterface(

    fn=chat,

    title="Nova - AI Research Assistant",

    description=
    """
    A conversational AI assistant with:
    - Weather API
    - Semantic document search
    - Calculator tools
    """
)


demo.launch()