# NLP-Playground

## Introduction
The Poetry Generator is an interactive application that uses the OpenAI GPT-3.5-turbo model to generate poems based on user-inputted themes. Built with Python and Streamlit, this tool provides an easy-to-use interface for creative writing enthusiasts to explore automated poetry generation.

## Prerequisites
- Python 3.8
- Pip package manager
- openai==0.28

## Installation
conda create -env nlp
conda activate nlp
pip install streamlit openai==0.28

## API OpenAI Key Configuration
Before running the application, you need to set up your OpenAI API key. Replace your-api-key with your actual OpenAI API key in the .env file or export it as an environment variable:

## Run the apps
1. Go to the directory
2. Open terminal
3. streamlit run app.py <--- Change app.py with the name of the .py file you want to run

## Generating Poems

    Enter a theme or prompt for your poem in the text input field.
    Click on "Generate Poem" to see the poem generated by the AI.

## Features

    Theme-Based Poetry Generation: Enter any theme to inspire your poem.
    Interactive User Interface: Simple and easy-to-use interface powered by Streamlit.
    Dynamic Poem Refinement: The application first generates a poem and then refines it by expanding on the initial ideas.

## Contributions
Contributions are welcome! Please fork this repository and open a pull request to add more features, fix bugs, or enhance the documentation.
