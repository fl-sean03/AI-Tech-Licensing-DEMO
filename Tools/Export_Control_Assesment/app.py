from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Load the export control assessment template
template_path = os.path.join(os.path.dirname(__file__), 'Export_Control_Assessment_Template.txt')
with open(template_path, 'r') as file:
    EXPORT_CONTROL_TEMPLATE = file.read()

# Load the export control requirements
requirements_path = os.path.join(os.path.dirname(__file__), 'Export_Control_Requirements.txt')
with open(requirements_path, 'r') as file:
    EXPORT_CONTROL_REQUIREMENTS = file.read()

# OpenAI API key
# OpenAI API key
api_key = 'your-openai-api-key-here'

client = OpenAI(
  api_key=api_key,
)

def generate_export_control_assessment(technology, requirements, template):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Generate an export control assessment report based on the provided template and analyzing the provided technology, make sure this is in a pretty html format, make sure the fact sheet layout is from top down NOT left to right. Return a filled template with information relevant to the technology. This assessment should be detailed and professional making sure to focus on information that connects directly to the technology. For each section, make sure to reference at least one specific aspect of the technology and connect it to the subject. \n\nTemplate:\n{template}\n\nTechnology Details:\n{technology}\n\nExport Control Requirements:\n{requirements}\n\nAssessment Report:"}
        ]
    )
    return response.choices[0].message.content

@app.route('/')
def index():
    return render_template('index.html', template=EXPORT_CONTROL_TEMPLATE, requirements=EXPORT_CONTROL_REQUIREMENTS)

@app.route('/generate_assessment', methods=['POST'])
def generate_assessment_route():
    data = request.get_json()
    technology = data['technology']
    requirements = data['requirements']
    assessment = generate_export_control_assessment(technology=technology, requirements=requirements, template=EXPORT_CONTROL_TEMPLATE)
    return jsonify({'assessment': assessment})

if __name__ == '__main__':
    app.run(debug=False)
