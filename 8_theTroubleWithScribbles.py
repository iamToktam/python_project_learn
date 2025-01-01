class CustomInputException(Exception):
    def __init__(self, message="Invalid input provided. Please check your input and try again."):
        self.message = message
        super().__init__(self.message)


class CustomProgrammingException(Exception):
    def __init__(self, message="A programming error occurred. Please check the code and try again."):
        self.message = message
        super().__init__(self.message)


def process_input(user_input):
    if not isinstance(user_input, str) or not user_input.strip():
        raise CustomInputException("Input must be a non-empty string.")

    try:
        # Simulating some processing
        if user_input == "error":
            raise ValueError("Simulated processing error")
    except ValueError as e:
        raise CustomProgrammingException(f"Programming error: {str(e)}")


try:
    process_input("error")  # Change this to test different inputs
except CustomInputException as cie:
    print(f"Input Error: {cie}")
except CustomProgrammingException as cpe:
    print(f"Programming Error: {cpe}")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")