import json
from flask import Flask, request, jsonify, render_template
from src.Source_Code.chat_interface import get_chatCompletion, messages
from Tools.Technology_Fact_Sheet_Generator.app import generate_fact_sheet, FACTSHEET_TEMPLATE, client
from Tools.Export_Control_Assesment.app import generate_export_control_assessment, EXPORT_CONTROL_TEMPLATE, EXPORT_CONTROL_REQUIREMENTS

def load_tools():
    with open('Tools/tools.json', 'r') as file:
        tools = json.load(file)
    return tools

tools = load_tools()

app = Flask(__name__)

@app.route('/')
def index():
    print("Index page loaded")
    return render_template('index.html', tools=tools)

@app.route('/tools')
def get_tools():
    return jsonify(tools)

@app.route('/tool_html/<tool_endpoint>')
def get_tool_html(tool_endpoint):
    if tool_endpoint == 'fact_sheet_generator':
        print("Fact Sheet Generator page loaded")
        return render_template('fact_sheet_generator.html', template=FACTSHEET_TEMPLATE)
    elif tool_endpoint == 'export_control_assessment':
        print("Export Control Assessment page loaded")
        #print("Template:", EXPORT_CONTROL_TEMPLATE)
        #print("Requirements:", EXPORT_CONTROL_REQUIREMENTS)
        return render_template('export_control_assessment.html', template=EXPORT_CONTROL_TEMPLATE, requirements=EXPORT_CONTROL_REQUIREMENTS)
    return "Tool not found", 404

@app.route('/chat', methods=['POST', 'GET'])
def chat():
    if request.method == 'POST':
        print("Chat button pressed")
        print("Chat form submitted")
        user_input = request.form.get("message")
        messages.append({"role": "user", "content": user_input})
        response = get_chatCompletion(messages)
        messages.append({"role": "assistant", "content": response})
        return render_template('index.html', user_input=user_input, response=response, tools=tools)
    return render_template('index.html', tools=tools)

@app.route('/chat_ajax', methods=['POST'])
def chat_ajax():
    print("Chat AJAX button pressed")
    print("Chat AJAX request received")
    user_input = request.json.get("message")
    messages.append({"role": "user", "content": user_input})
    response = get_chatCompletion(messages)
    messages.append({"role": "assistant", "content": response})
    return jsonify({"user_input": user_input, "response": response})

@app.route('/generate_fact_sheet', methods=['POST'])
def generate_fact_sheet_route():
    print("Generate Fact Sheet button pressed")
    technology = request.form['technology']
    template = request.form['template']
    fact_sheet = generate_fact_sheet(LLMclient=client, technology=technology, template=template).replace("```html", "").replace("```", "")
    return jsonify({'fact_sheet': fact_sheet})

@app.route('/generate_export_control_assessment', methods=['POST'])
def generate_export_control_assessment_route():
    print("Generate Export Control Assessment button pressed")
    technology = request.form['technology']
    requirements = request.form['requirements']
    template = request.form['template']
    assessment = generate_export_control_assessment(technology, requirements, template)
    return jsonify({'assessment': assessment})

app.add_url_rule('/generate_fact_sheet', 'generate_fact_sheet_route', generate_fact_sheet_route, methods=['POST'])
app.add_url_rule('/generate_export_control_assessment', 'generate_export_control_assessment_route', generate_export_control_assessment_route, methods=['POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
