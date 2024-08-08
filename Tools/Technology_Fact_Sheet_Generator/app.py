from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# Load the fact sheet template
import os

template_path = os.path.join(os.path.dirname(__file__), 'factsheet_template.txt')
with open(template_path, 'r') as file:
    FACTSHEET_TEMPLATE = file.read()

# OpenAI API key
api_key = 'your-openai-api-key-here'

client = OpenAI(
  api_key=api_key,
)

def generate_fact_sheet(LLMclient, technology, template):
    response = LLMclient.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Generate a fact sheet, make sure this is in a pretty html format, make sure the fact sheet layout is from top down NOT left to right, for the following technology based on the template:\n\nTemplate:\n{template}\n\nTechnology: {technology}\n\nFact Sheet:"}
        ]
    )
    return response.choices[0].message.content  

@app.route('/')
def index():
    return render_template('index.html', template=FACTSHEET_TEMPLATE)

@app.route('/generate_fact_sheet', methods=['POST'])
def generate_fact_sheet_route():
    print("Generate Fact Sheet button pressed")
    technology = request.form['technology']
    template = request.form['template']
    import re
    fact_sheet = generate_fact_sheet(LLMclient=client, technology=technology, template=template).replace("```html", "").replace("```", "")
    fact_sheet = re.sub(r'\s+', ' ', fact_sheet).strip()

    return jsonify({'fact_sheet': fact_sheet})

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
