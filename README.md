BOOKXPERT Assignment

This repository contains two tasks:
1. Name Matching System
2. Recipe Suggestion Chatbot

---

## Task 1: Name Matching System

### What to Install
- Python 3.x
- Required library:

pip install rapidfuzz

### How to Run
Run the following command in terminal:

python name_matching.py

Output:
The output is displayed in the terminal and includes:
- Best matching name with similarity score
- Ranked list of similar names

Enter a name: Geeta

Best Match:
Geetha with similarity 95%

Top 5 Similar Names:
1. Geetha - 95%
2. Gita - 90%
3. Geetu - 85%
4. Gitu - 82%
5. Seeta - 78%

---

## Task 2: Recipe Chatbot

### What to Install
- Python 3.x
- Required dependencies:

pip install -r requirements.txt

### How to Run

#### Step 1: Start Backend Server
Run in terminal:

uvicorn app:app --reload

#### Step 2: Run Chatbot
Open a new terminal and run:

python cli_chatbot.py

### Output:
![image alt](https://github.com/sayalidp/BOOKXPERT_Assignment/blob/4ccd6ba00c8999492ae681454cd8ab4ce8b758a8/Task%202%3A%20Local%20LLM%20Integration%20%26%20Chatbot/Screenshot%202026-02-03%20170318.png)

