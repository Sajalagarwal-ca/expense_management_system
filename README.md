# Expense Management System

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server. This project is designed to take input from user for tracking their expenses, save them in a database which can postgres, mysql or SQL etc and do some analytics by simple charts.

## Screenshots

Here are some screenshots of the application:
### Screenshot 1
![Page-1](Screenshots/Page-1.jpeg)
### Screenshot 1
![Page-2](Screenshots/page-2.jpeg)
### Screenshot 1
![Page-3](Screenshots/page-3.jpeg)
## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.


## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/expense-management-system.git
   cd expense-management-system
   ```
1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server.server:app --reload
   ```
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py
   ```