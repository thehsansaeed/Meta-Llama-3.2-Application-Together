import os
from together import Together


# Set the API key as an environment variable
os.environ['TOGETHER_API_KEY'] = ''

def get_chatbot_response(image_url=None, user_question=None):
    if image_url:
        # Define the chatbot message for the image
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Describe this image"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url
                        }
                    }
                ]
            }
        ]
    elif user_question:
        # Define the chatbot message for a general question
        messages = [
            {
                "role": "user",
                "content": user_question
            }
        ]
    else:
        return "No input provided."

    # Call the Together API
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
        messages=messages,
        max_tokens=512,
        temperature=0.7,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>", "<|eom_id|>"],
        stream=False  # Stream as False for console
    )

    return response.choices[0].message.content

# Main function to run the chatbot in the console
def chatbot_console():
    while True:
        user_input = input("Enter 'image' for image URL or 'question' for a question (or type 'exit' to quit): ").strip().lower()
        if user_input == 'exit':
            print("Exiting chatbot...")
            break
        elif user_input == 'image':
            image_url = input("Enter image URL: ").strip()
            response = get_chatbot_response(image_url=image_url)
        elif user_input == 'question':
            user_question = input("Enter your question: ").strip()
            response = get_chatbot_response(user_question=user_question)
        else:
            response = "Invalid input."

        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot_console()