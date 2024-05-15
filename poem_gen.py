import os
import openai
import streamlit as st


# Define the prompt template
def generate_poem(theme):
    response = openai.ChatCompletion.create(
        model="babbage-002",
        messages=[
            {"role": "system", "content": "You are a poet."},
            {"role": "user", "content": f"Write a poem about {theme}"},
        ],
        max_tokens=150,
        temperature=0.7,
    )
    return response['choices'][0]['message']['content'].strip()

# Function to chain prompts
def chain_prompts(initial_theme):
    initial_output = generate_poem(initial_theme)
    refined_prompt = f"Expand on this idea: {initial_output}"
    refined_output = generate_poem(refined_prompt)
    return refined_output

# Streamlit app
st.title("Poetry Generator")
theme = st.text_input("Enter a theme or prompt for your poem:")

# Generate poem button
if st.button("Generate Poem"):
    poem = chain_prompts(theme)
    st.write(poem)