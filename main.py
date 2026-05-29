import os
import gradio as gr
from groq import Groq

# Load API key securely from Hugging Face Secrets
client = Groq(Enter the api_key)


SYSTEM_PROMPT = """
You are an expert Indian chef with 10 years of experience.

Your role is to:
- Help users with Indian recipes
- Explain cooking techniques clearly
- Suggest ingredients and substitutions
- Provide professional and concise answers
"""


def chat_function(message, history):

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    # Add previous conversation
    for user_msg, bot_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": bot_msg})

    # Add latest user message
    messages.append({"role": "user", "content": message})

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
        )

        reply = response.choices[0].message.content

    except Exception as e:
        reply = f"Error: {str(e)}"

    return reply


iface = gr.ChatInterface(
    fn=chat_function,
    chatbot=gr.Chatbot(height=400),
    textbox=gr.Textbox(
        placeholder="Ask me anything about Indian cooking..."
    ),
    title="Indian Recipe Assistant",
    description="AI chatbot for Indian cooking guidance and recipes.",
    examples=[
        "How do I make biryani?",
        "Give me a crispy jalebi recipe",
        "What spices are used in butter chicken?"
    ],
    theme="soft"
)

iface.launch()
