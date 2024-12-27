# Create-SQL-query-from-plain-english

This project is a simple Streamlit web application that uses Google Gemini (a generative AI model) to convert natural language questions into SQL queries. The queries are then executed on a SQLite database to retrieve results.

### Features
- Convert natural language questions into SQL queries using Google Gemini.
- Execute SQL queries on a SQLite database.
- Display the results in a user-friendly format via Streamlit.

### Technologies Used
- **Google Gemini API** for natural language processing and query generation.
- **Streamlit** for the web interface.
- **SQLite** for the database.

---

## Prerequisites

Before running this project, ensure you have the following installed:

- **Python 3.x** 
- **SQLite3**
- **Streamlit**: For the frontend.
- **Google Gemini API**: For query generation.

---

## Setup Instructions

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/yourprojectname.git
cd yourprojectname
```

### Step 2: Install required libraries

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install dependencies:

```bash
pip install -r requirements.txt
```

**Note:** You will need to create a `.env` file to store your `GEMINI_API_KEY` for the Google Gemini API.

### Step 3: Create the `.env` file

Create a `.env` file in the root directory and add your API key:

```
GEMINI_API_KEY=your-google-gemini-api-key
```

### Step 4: Run the Streamlit App

Start the Streamlit app by running:

```bash
streamlit run app.py
```

This will launch a web app that allows you to input questions, which will be converted into SQL queries and executed on the SQLite database.

---

## Database Setup

The project uses a SQLite database `student.db` with a table `STUDENT` that includes the following columns:

- `NAME` (VARCHAR)
- `CLASS` (VARCHAR)
- `SECTION` (VARCHAR)
- `MARKS` (INT)

If the database and table do not exist, they will be created automatically when running the code. The database is pre-populated with sample student data.

---

## Usage

1. **Input a Question**: Enter any question related to the student data, such as:
   - "How many students are in the Data Science class?"
   - "What students scored more than 80 marks?"
   
2. **Receive SQL Query**: The system will generate the SQL query that corresponds to your question using Google Gemini.

3. **View Results**: The query is then executed against the SQLite database, and the results are displayed on the Streamlit interface.

---

## Example Questions

Here are a few example questions you can ask:

- "How many entries of records are present?"
- "Tell me all the students studying in Data Science class?"
- "Which students scored more than 80 marks?"

---

## Contributing

If you’d like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request with a description of your changes.

---


