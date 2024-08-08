# AI-Tech-Licensing-DEMO

This project is a web application built using Flask. It provides various tools including a chat interface, a fact sheet generator, and an export control assessment tool.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Tools](#tools)
  - [Technology Fact Sheet Generator](#technology-fact-sheet-generator)
  - [Export Control Assessment](#export-control-assessment)
- [Contributing](#contributing)
- [License](#license)

## Directory Structure

```
AI-Tech-Licensing-DEMO/
├── Knowledge_Bases/
│   ├── KnowledgeBase1/
│   │   ├── Database.txt
│   │   └── README
│   ├── KnowledgeBase2/
│   │   ├── Database.txt
│   │   └── README
│   └── knowledge_bases.txt
├── Tools/
│   ├── Export_Control_Assesment/
│   │   ├── Export_Control_Assessment_Template.txt
│   │   ├── Export_Control_Requirements.txt
│   │   ├── README.md
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   ├── static/
│   │   │   └── style.css
│   │   └── templates/
│   │       └── index.html
│   ├── Technology_Fact_Sheet_Generator/
│   │   ├── README.md
│   │   ├── app.py
│   │   ├── factsheet_template.txt
│   │   ├── requirements.txt
│   │   ├── static/
│   │   │   └── style.css
│   │   └── templates/
│   │       └── index.html
│   └── tools.json
├── src/
│   └── Source_Code/
│       ├── .gitkeep
│       └── chat_interface.py
├── static/
│   ├── export_control_assessment_style.css
│   ├── fact_sheet_generator_style.css
│   └── index_style.css
├── templates/
│   ├── export_control_assessment.html
│   ├── fact_sheet_generator.html
│   └── index.html
├── app.py
├── requirements.txt
└── README.md
```

## Notes

- The sections can be resized to get a better view of each box.
- If a generated output does not come out with a nice layout, just regenerate it until it looks good.
- This is an extremely rudimentary demo.
- The knowledge bases located in the `Knowledge_Bases` directory are not currently being used in the application.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/AI-Tech-Licensing-DEMO.git
    cd ATLAS_DEMO_V4
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Update the OpenAI API key:
    Before running the application, you need to update the `api_key` variable in the following files with your OpenAI API key:
    - `Tools/Technology_Fact_Sheet_Generator/app.py`
    - `Tools/Export_Control_Assesment/app.py`
    - `src/Source_Code/chat_interface.py`

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://localhost:5000`.

### Using the Application

- **Index Page:** The index page lists all available tools. You can access it by navigating to `http://localhost:5000/`.
- **Chat Interface:** You can interact with the chat interface by navigating to `http://localhost:5000/chat`. Submit your message using the form, and the response will be displayed on the same page.
- **Fact Sheet Generator:** To generate a fact sheet, navigate to `http://localhost:5000/tool_html/fact_sheet_generator`. Fill in the required details and submit the form to get the generated fact sheet.
- **Export Control Assessment:** To generate an export control assessment, navigate to `http://localhost:5000/tool_html/export_control_assessment`. Fill in the required details and submit the form to get the generated assessment report.


## Endpoints

- `/` - Index page
- `/tools` - Get list of tools
- `/tool_html/<tool_endpoint>` - Get HTML for a specific tool
- `/chat` - Chat interface
- `/chat_ajax` - Chat interface with AJAX
- `/generate_fact_sheet` - Generate a fact sheet
- `/generate_export_control_assessment` - Generate an export control assessment

## Tools

### Technology Fact Sheet Generator

**Description:**
This tool generates fact sheets for various technologies. It uses a template to format the fact sheet and leverages the OpenAI API to generate the content based on the provided technology details.

**Key Components:**
- **Template Loading:** The fact sheet template is loaded from a file (`factsheet_template.txt`).
- **OpenAI API Integration:** The tool uses the OpenAI API to generate the fact sheet content.
- **Flask Routes:**
  - `/`: Renders the index page with the fact sheet template.
  - `/generate_fact_sheet`: Generates the fact sheet based on the provided technology and template.

**Code Location:**
- Configuration and routes are defined in `Tools/Technology_Fact_Sheet_Generator/app.py`.

### Export Control Assessment

**Description:**
This tool assesses export control requirements for various technologies. It uses a template and a set of requirements to generate a detailed export control assessment report.

**Key Components:**
- **Template Loading:** The export control assessment template is loaded from a file (`Export_Control_Assessment_Template.txt`).
- **Requirements Loading:** The export control requirements are loaded from a file (`Export_Control_Requirements.txt`).
- **OpenAI API Integration:** The tool uses the OpenAI API to generate the assessment report.
- **Flask Routes:**
  - `/`: Renders the index page with the export control template and requirements.
  - `/generate_assessment`: Generates the export control assessment based on the provided technology, requirements, and template.

**Code Location:**
- Configuration and routes are defined in `Tools/Export_Control_Assesment/app.py`.

## License

For anyone to use and incorporate for their own projects.
