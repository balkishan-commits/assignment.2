"""
Assigment 1 - Solutions

This script contains clear, runnable answers to the six questions:
1) Difference between basic data types (int, float, str, bool) with examples
2) Create three variables (name, age, city) and print them
3) Take a user's name as input (or use a sample when running non-interactively), print uppercase and length
4) Demonstrate five commonly used string methods with examples
5) Work with a list of five fruits and print required information
6) Work with a list of numbers: add and remove elements and print the updated list
7) What is Artificial Intelligence (AI)? Explain its importance and mention
any four real-life applications of AI.
8) Identify whether the following are examples of AI and explain why:
 ChatGPT, Google Maps route prediction, Calculator, Netflix recommendations, Voice assistants (Alexa/Siri).

"""
import sys


def q1_datatypes_examples():
        
        print("Q1. Data types with examples")
        an_int = 5
        """
        Assigment 1 - Solutions (clean beginner-friendly version)

        Each function answers one question in simple language. The sample name used is "Balkishan".
        """

        import sys


        def q1_datatypes_examples():
            """Show simple examples of int, float, str, and bool."""
            print("Q1. Data types with examples")
            an_int = 5
            print("Integer:", an_int)

            a_float = 2.5
            print("Float:", a_float)

            a_str = "Hello"
            print("String:", a_str)

            a_bool = False
            print("Boolean:", a_bool)
            print()


        def q2_person_variables():
            """Create three variables (name, age, city) and print them.

            Uses the name 'Balkishan' as requested.
            """
            print("Q2. Create and print three variables")
            name = "Balkishan"
            age = 20
            city = "Jaipur"

            print("Name:", name)
            print("Age:", age)
            print("City:", city)
            print()


        def q3_name_input_and_stats():
            """Take a user's name, print it in uppercase and show its length.

            If no input is available, use 'Balkishan' so the script does not stop.
            """
            print("Q3. Name input -> uppercase and length")
            try:
                user_name = input("Enter your name: ").strip()
                if not user_name:
                    user_name = "Balkishan"
            except EOFError:
                user_name = "Balkishan"

            print("Uppercase:", user_name.upper())
            print("Length:", len(user_name))
            print()


        def q4_string_methods_examples():
            """Show five common string methods with short examples."""
            print("Q4. Five commonly used string methods")
            s = "  hello, world  "
            print("Original:", repr(s))
            print("strip ->", repr(s.strip()))
            print("upper ->", s.upper())
            print("lower ->", s.lower())
            print("replace ->", s.replace('hello', 'hi'))
            print("split ->", s.split(','))
            print()


        def q5_fruits_list():
            """Create a list of five fruits and print information about it."""
            print("Q5. Fruits list")
            fruits = ["apple", "banana", "mango", "orange", "grapes"]
            print("List:", fruits)
            print("First item:", fruits[0])
            print("Last item:", fruits[-1])
            print("Total items:", len(fruits))
            print()


        def q6_modify_numbers_list():
            """Create a list, add 60, remove 20, and print the result."""
            print("Q6. Modify numbers list")
            numbers = [10, 20, 30, 40, 50]
            print("Start:", numbers)
            numbers.append(60)
            print("After adding 60:", numbers)
            if 20 in numbers:
                numbers.remove(20)
                print("After removing 20:", numbers)
            else:
                print("20 was not in the list")
            print()


        def q7_ai_explain():
            """Explain AI in very simple terms and list four applications."""
            print("Q7. What is Artificial Intelligence (AI)?")
            print("AI is making computers do tasks that need thinking, like learning or understanding words.")
            print("Why it matters:")
            print("- Automates boring or dangerous jobs")
            print("- Helps find patterns in data")
            print("- Makes services personal for each user")
            print()
            print("Four examples:")
            print("1. Medical diagnosis (help doctors)")
            print("2. Self-driving car features")
            print("3. Chatbots and virtual assistants")
            print("4. Recommendation systems (suggesting videos or products)")
            print()


        def q8_identify_examples():
            """Say whether each item is an AI example and why (short answers)."""
            print("Q8. Are these AI?")
            print("ChatGPT: Yes — uses machine learning to generate text.")
            print("Google Maps route prediction: Yes — uses data and models to predict traffic and routes.")
            print("Calculator: No — performs fixed arithmetic operations.")
            print("Netflix recommendations: Yes — learns from user choices to suggest shows.")
            print("Voice assistants (Alexa/Siri): Yes — use speech recognition and language understanding.")
            print()


        def main():
            q1_datatypes_examples()
            q2_person_variables()
            q3_name_input_and_stats()
            q4_string_methods_examples()
            q5_fruits_list()
            q6_modify_numbers_list()
            q7_ai_explain()
            q8_identify_examples()


        if __name__ == '__main__':
            main()
            main()

