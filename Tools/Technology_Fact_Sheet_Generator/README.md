# Fact Sheet Generator

## Description
The Fact Sheet Generator is a web application that allows users to generate fact sheets for various technologies using a predefined template. The application leverages OpenAI's GPT-4 model to generate the content based on user input.

## Installation
To install and run the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/fact-sheet-generator.git
    cd fact-sheet-generator
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your OpenAI API key:
    - Open `app.py` and replace `#Insert your OpenAI API Key Here` with your actual OpenAI API key.

5. Run the application:
    ```bash
    python app.py
    ```

6. Open your web browser and navigate to `http://127.0.0.1:5000` to access the application.

## Usage
1. Enter the technology details in the provided textarea.
2. Optionally, modify the template if needed.
3. Click the "Generate Fact Sheet" button to generate the fact sheet.
4. The generated fact sheet will be displayed in the output section.

## Contributing
If you would like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with a descriptive message.
4. Push your changes to your fork.
5. Create a pull request to the main repository.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
