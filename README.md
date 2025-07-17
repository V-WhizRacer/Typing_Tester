# Typing Speed Tester

-----

Welcome to the *Typing Speed Tester*, a simple yet effective application built with Python's Tkinter library. This tool helps you improve your typing speed and accuracy through engaging practice sessions. Whether you're a beginner looking to build foundational skills or an experienced typist aiming for higher WPM (Words Per Minute), this application provides a straightforward way to track your progress.

-----

## Features

  * *Interactive Typing Interface*: Type along with displayed paragraphs and see your input in real-time.
  * *Performance Metrics: Get instant feedback on your **Words Per Minute (WPM)* and *Accuracy*.
  * *Wrong Key Counter*: Track the number of incorrect keystrokes to identify areas for improvement.
  * *Adjustable Test Duration*: Choose between 30, 60, 90, or 120-second tests to fit your practice needs.
  * *Typing History*: Keep a record of your past test results to monitor your progress over time.
  * *Dynamic Text Highlighting*: See your correct characters highlighted in green and incorrect ones in red as you type.
  * *Theme Toggle*: Switch between a light and dark theme for comfortable typing in any environment.
  * *Randomized Paragraphs*: Practice with a variety of texts to keep your sessions fresh and challenging.

-----

## Getting Started

To get this typing speed tester up and running on your local machine, follow these simple steps:

### Prerequisites

You'll need Python installed on your system. This project is compatible with Python 3.x.

### Installation

1.  *Clone the repository (or download the source code):*
    If you're using Git, you can clone the repository to your local machine:

    bash
    git clone <repository_url>
    cd <repository_folder>
    

    (Replace <repository_url> and <repository_folder> with the actual URL and folder name if this were a public repository.)

2.  *Ensure Tkinter is available:*
    Tkinter usually comes pre-installed with Python. If you encounter any issues, you might need to install it separately, depending on your operating system:

      * *For Debian/Ubuntu:*
        bash
        sudo apt-get install python3-tk
        
      * *For Fedora:*
        bash
        sudo dnf install python3-tkinter
        
      * *For Windows/macOS:*
        Tkinter is typically included with the standard Python installation from python.org.

### Running the Application

Navigate to the project directory in your terminal and run the Python script:

bash
python your_script_name.py


(Replace your_script_name.py with the actual name of your Python file, e.g., Typing_speed_tester.py)

-----

## How to Use 🎮

1.  *Start Test*: Click the "Start Test" button to begin a new typing session.
2.  *Select Duration*: Use the dropdown menu to choose your desired test duration (30, 60, 90, or 120 seconds).
3.  *Type Away*: As the timer begins, start typing the displayed text in the input box.
      * Correct characters will appear *green*.
      * Incorrect characters will appear *red*.
      * Pressing *Enter* will move you to the next line.
4.  *Monitor Progress*: Your WPM, Accuracy, and Wrong Keys will update in real-time.
5.  *Test Completion*: Once the timer runs out, a pop-up will display your final results, and your score will be added to the history list.
6.  *Reset*: Click "Reset" to clear your current progress and prepare for a new test.
7.  *Toggle Theme*: Use the "Toggle Theme" button to switch between light and dark modes for a comfortable viewing experience.

-----

## Project Structure

The project is contained within a single Python file, demonstrating a clear and organized structure using a class-based approach for the Tkinter application.

  * TypingSpeedTester Class: Encapsulates all the GUI elements and application logic, including:
      * __init__: Initializes the main window and sets up the UI.
      * setup_ui: Arranges all the widgets (labels, entry box, buttons, etc.).
      * reset: Resets the test state for a new session.
      * update_display_line: Updates the text displayed for typing.
      * start_test: Initiates the timer and test.
      * countdown: Manages the test timer.
      * handle_enter: Processes the user's input when Enter is pressed.
      * evaluate_current_line: Calculates correct/wrong characters for the current line.
      * track_typing: Provides real-time feedback by coloring typed characters.
      * finish_test: Calculates final WPM and accuracy, and updates the history.
      * toggle_theme: Switches the application's visual theme.

-----

## Contributing

This project is a great starting point for anyone interested in GUI development with Tkinter. Feel free to fork the repository, suggest improvements, or add new features.

-----

## Acknowledgments

A big thank you to the open-source community for the resources and knowledge that make projects like this possible. 
