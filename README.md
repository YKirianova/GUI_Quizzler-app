# Quizzler - Python Quiz Application

This is a Python-based quiz application that uses the Tkinter library for the graphical user interface (GUI). The quiz fetches True/False questions from the Open Trivia Database API and provides a simple, interactive way for users to test their knowledge.

## Game Overview

- **Objective**: Answer 10 True/False questions, and get immediate feedback on whether the answer is correct. The game keeps track of the score, and the final result is displayed once the quiz is completed.
- **Feedback**: The interface provides visual feedback by changing the background color to green for correct answers and red for incorrect ones.
- **Score**: The score is displayed and updated after each question.

## Controls

- Use the **True** and **False** buttons on the screen to answer the questions.

## Files

1. **`main.py`**: 
   - The main file that initializes the quiz interface and starts the game loop.
   - Initializes the quiz questions by fetching data from the Open Trivia Database API.
   - Creates instances of the `QuizBrain` and `QuizInterface` classes.
   - Controls the main game loop and checks if there are still questions remaining.

2. **`question_model.py`**:
   - Contains the `Question` class, which holds the question text and the correct answer.

3. **`data.py`**:
   - Handles the quiz data by fetching it from the Open Trivia Database API.
   - Sends a request to the API to retrieve 10 True/False questions.
   - Parses the JSON response and stores the questions in a format usable by the `Question` class.

4. **`quiz_brain.py`**:
   - Contains the `QuizBrain` class, which manages the logic of the quiz.
   - Handles displaying the next question.
   - Checks whether the answer is correct.
   - Keeps track of the user's score and the number of questions asked.
   - Escapes HTML entities in the questions to ensure proper display.

5. **`ui.py`**:
   - Contains the `QuizInterface` class, which builds the GUI using Tkinter.
   - Displays the current question and score.
   - Provides two buttons for answering (True/False).
   - Changes the background color based on whether the answer is correct.
   - Updates the question and score after each interaction.

## How to Run

1. Ensure Python is installed: You need Python 3.x installed on your machine.
2. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/quizzler.git
   cd quizzler
3.Install the required dependencies:
  pip install requests
4. Run the application:
  python main.py
5. Play the game: Use the buttons in the graphical interface to answer True/False questions and see your score.

## API
This application uses the Open Trivia Database API to fetch the quiz questions. The following parameters are used to configure the API request:

amount: 10 (retrieves 10 questions)
type: boolean (retrieves True/False questions)
