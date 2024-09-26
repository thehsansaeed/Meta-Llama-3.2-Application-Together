# Together API Chatbot

This repository contains a console-based chatbot application that interacts with the Together API to answer questions or describe images provided by the user. The chatbot can accept both image URLs and general questions, utilizing the Together API to generate responses using the "meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo" model.

## Features

- **Image-based interaction**: Describe the content of an image by providing its URL.
- **Text-based interaction**: Ask the chatbot general questions.
- Uses the Together API to handle natural language and image understanding.
- Configurable model parameters, such as temperature and token limit, for enhanced response control.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. Install dependencies:

   This project requires the `together` Python package. You can install it by running:

   ```bash
   pip install together
   ```
3. Set the Together API key:

   In your code, make sure to set the API key as an environment variable or directly in the script as shown below:

   ```python
   import os
   os.environ['TOGETHER_API_KEY'] = 'your_api_key'
   ```

## Usage

1. Run the script:

   ```bash
   python app.py
   ```
2. When prompted, enter either:

   - `'image'` to provide an image URL and get a description.
   - `'question'` to ask a question.

   Example:

   ```bash
   Enter 'image' for image URL or 'question' for a question (or type 'exit' to quit): image
   Enter image URL: https://example.com/sample.jpg
   ```

   or

   ```bash
   Enter 'image' for image URL or 'question' for a question (or type 'exit' to quit): question
   Enter your question: What is the capital of France?
   ```

## Configuration

You can configure the chatbot response by adjusting the parameters in the `get_chatbot_response` function:

- **`max_tokens`**: Limits the length of the response.
- **`temperature`**: Controls the randomness of the response.
- **`top_p` and `top_k`**: Adjust the token sampling for diversity.
- **`repetition_penalty`**: Prevents repetitive responses.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributing

Feel free to submit issues and pull requests for any improvements or bug fixes.

## API Documentation

For more information on the Together API, visit the [Together API Documentation](https://docs.together.com/).

## Contact Information

https://www.linkedin.com/in/ahsensaeed/
