> **COMP-801 Integrated Computing Practice**
# Homework 1

## H1 Start Due Dates
- Assigned Week 4
- Due before Wednesday midnight, before Week 5 class
    - Upload to Canvas the PDF of the DESIGN.md
    - Push to the remote all the changes made to the local repo

## H1 Start Requirements

Use test-driven incremental development
- Document:
  - Modules `sentence.py` and `client.py`
  - Design document `DESIGN.md`
- Write test cases for the methods in class `Sentence`
- Design the four methods in `DESIGN.md` 
- Apply version control to demonstrate the development steps: document, test, and design.

**Note**: Do NOT proceed with implementing the methods for this assignment. 

## H1 Start Getting Started

1. Open `git-bash` (in Windows OS) or `terminal` utility (in MacOS or Linux)
2. Clone remote repo into your **comp801/homework** directory 
- Do NOT make directory **h1**. Cloning will do that. 
- Use the `clone` command with TWO arguments as shown below:
```
git clone <URL of your remote repo> h1
```
3. Open **h1** folder in VS Code.
4. Run `client.py` in two ways:
  - In the VS Code integrated terminal, run `python client.py`
  - OR, use the Run Python File button in the upper right corner. 
5. Create 4 testing modules, `test_xxx.py`, where `xxx` is the name of the `Sentence` method that the module is testing. 
6. Check the errors reported in the **Problems** tab of the VS Code integrated terminal
  - Format each file with the Black Formatter tool.  


## Evaluation

### h1start (60 pts)
#### H1 Start Documentation (14 pts)

This is a *all or nothing* requirement. This means that missing to document the DESIGN.md file or any of the Python module results in no credit for documentation.

The project has one DESIGN.md and 6 modules: 
- `client.py`, `sentence.py`, and 4 **testing modules**, corresponding to the 4 methods in the `Sentence` class.

Documentation must include your name as the sole developer of this homework assignment. 

#### H1 Start Testing Functions Implementation (16 pts)**

- 8 testing functions, at 2 pts each
- 2 testing functions in each testing module.
    
#### H1 Start Methods Design (16 pts)

In DESIGN.md: 4 designs, at 4 pts each

#### H1 Start Code Analysis and Styling (5 pts)

#### H1 Start Incremental Development (9 pts)

Follow the development process and apply version control correctly to each development step. 

- 1 commit for documentation
- 1-2 commits for each testing module
- 1 commit for each design
- Minimum of 9 commits total, with meaningful commit messages, and in the correct
order.

---

### h1final (40 pts)
Due on **Monday** midnight, following **Week 5 Exam 1** class.

#### H1 Final Requirements
- Continue the work in H1 Start by implementing, testing, and debugging the Sentence methods.
- Apply version control.
- Resolve all the Problems reported in VS Code by running the code analysis tools.

#### H1 Final Getting Started
You already have the local repot for this assignment from **h1start** assignment. 

#### H1 Final Implementation (24 pts)
- 4 methods, at 6 pts each

#### H1 Final Incremental Development (8 pts)

Version control must show correct order and meaningful commit messages. 

- 4 commits, 1 commit for each method
- 1 commit for code analysis, if needed.

This is a *all or nothing* requirement. 


#### H1 Final Code Analysis and Styling (8 pts)

This is a *all or nothing* requirement. 


## Guidelines
### h1start

#### H1 Start Document** 
ALL modules with properly written docstrings. 
  - Version control this step.

#### H1 Start Understand
Understand what each method is supposed to do, based on the `docstring` 
   description, BEFORE writing the test cases.

#### H1 Start Test
Write **test cases** to demonstrate your understanding of each method.
  - Version control this step.

#### H1 Start Design
In `DESIGN.md` design each method BEFORE coding.
  - Version control this step.

#### H1 Start Incremental Development
Repeat steps 2 to 4 for each method (4 times total) to complete this phase of the homework.

#### H1 Start Code Analysis and Styling 
- When implementation is complete, do a thorough code analysis with the tools installed in VS Code. 
  - Fix all the **Problems** reported by running these tools. 

### h1final
#### H1 Final Implment

Implement the methods in `Sentence` class according to the **design** you submitted for **H1 Start**

#### H1 Final Test, Debug, Fix
- Test your implementation based on the testing functions you developed in **H1 Start**.
- If there are errors, debug and fix the errors. This might require changes to:
  - Method design in DESIGN.md
  - Method implementation in the Sentence class. 

#### H1 Final Incremental Development
- Apply version control to demonstrate the changes you have made to:
  - method design
  - method implementation.

#### H1 Final Code Analysis
- When implementation is complete, do a thorough code analysis with the tools installed in VS Code. 
  - Fix all the **Problems** reported by running these tools. 


## Collaboration
- No collaboration with peers or other people is allowed, EXCEPT for the CAs and course instructors
- No other sources of content (internet, GPT tools, etc.) are allowed.
- You are NOT allowed to give your work on this assignment to somebody else, or to do it for someone else. 

## Submission

The commit history of the development of the  h1final local repo is pushed to GitHub.
