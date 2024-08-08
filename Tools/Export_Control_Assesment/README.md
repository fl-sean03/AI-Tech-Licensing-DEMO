# Export Control Checker

This tool helps generate export control assessment reports for various technologies. It uses OpenAI's GPT-4 to generate detailed and professional reports based on a provided template and export control requirements.

## Setup

1. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

2. Set your OpenAI API key in `app.py`:
    ```python
    api_key = 'your_openai_api_key_here'
    ```

3. Run the application:
    ```bash
    python app.py
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:5000/`.
2. Fill in the technology details and requirements.
3. Click "Generate Assessment" to get the export control assessment report.
