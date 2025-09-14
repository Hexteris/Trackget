# Trackget - Budget Feedback Web App

## Video Demo

https://trackget.pythonanywhere.com/

## Objective of Trackget

The objective of Trackget is to help users manage their finances by providing a clear and visual representation of their budget, encouraging them to save more and spend wisely.

## Usage
Upon arriving at the webpage, users only need to enter three inputs:

- **Monthly Income**
- **Desired Savings**
- **Expenses**

After that, the webpage will generate a detailed summary to assist them with their monthly budgeting.

## How the Program Works
This web application provides feedback on users' monthly budgets by analyzing their income, savings, and expenses. It presents the data in a structured dashboard with tables and graphs.

## Features
- User input validation for income, savings, and expenses.
- Real-time budget performance feedback.
- Interactive summary table and visualizations.
- Template inheritance with Jinja.
- Flask-based backend with session storage.
- Graphs generated using Matplotlib.
- Alerts and error messages to guide users in budgeting.

## File Structure

### `layout.html`
This file establishes the layout of the web page. It includes:
- The `<head>` section with metadata and Bootstrap CSS for styling.
- A navbar with links to `about.html` and `tracker.html`.
- A Jinja-based template inheritance structure allowing other pages to extend `layout.html`.
- A conditional statement ensuring `tracker.html` is only rendered when the user has provided valid data.
- A `<div>` container where dynamic content from different routes is displayed.
- A footer with contact information for feedback and support.

### `info.html`
This page inherits `layout.html` and requests three user inputs:
- **Monthly income**
- **Savings**
- **Expenses**

Input validation ensures:
- The sum of savings and expenses equals the user's income.
- No fields are left empty.

If validation fails, an alert message is shown. User inputs are stored in a session so they remain accessible until the browser is closed. This ensures users can return to their budget summary without re-entering their data.

### `trackget.html`
This page provides a budget summary with a **dashboard-style layout** using Bootstrap grids:
- **Top left**: A message analyzing the user's budget based on their savings percentage. Various messages are displayed depending on how well the user is saving.
- **Top right**: A summary table displaying income, expenses, savings, and the percentage saved, allowing users to quickly assess their financial situation.
- **Bottom left**: A line graph visualizing budget trends over time, helping users track changes in income and expenses.
- **Bottom right**: A pie chart displaying expense distribution, offering a visual representation of where money is being spent.

This dashboard ensures that users can easily interpret their financial standing at a glance.

### `about.html`
This page answers common user questions about how to use the application and budgeting tips. It also provides an email for feedback and support. Users can contact the developer to report bugs, request features, or ask for clarification regarding budget analysis.

## Backend (`app.py`)
This is the core logic of the web application, implemented using Flask:
- **Library imports**: `Flask`, `Matplotlib`, `io`, and `base64` for handling sessions and graph rendering.
- **Flask app initialization**:
  ```python
  app = Flask(__name__)
  if __name__ == "__main__":
      app.run(debug=True)
  ```
- **Session handling**: `SESSION_PERMANENT` is set to `False` to clear data when the browser is closed.

### Routes
#### `@app.route("/trackget")`
- Retrieves stored user inputs from the session.
- Ensures inputs are valid before performing calculations.
- Computes:
  - Savings ratio
  - Savings percentage
  - Estimated yearly savings
- Generates a pie chart and line graph using Matplotlib, encoding them in Base64 for display.
- Passes computed variables to `trackget.html` for rendering.
- Ensures that messages reflect different saving habits, encouraging users to save at least 20% of their income.

#### `@app.route("/", methods=["GET", "POST"])`
- Stores user inputs in the session.
- Displays alerts for missing fields or incorrect calculations.
- Redirects to `trackget.html` if all inputs are valid.
- Prevents users from proceeding without correctly balancing their budget.

#### `@app.route("/about", methods=["GET"])`
- Renders `about.html` when the user clicks "About" in the navbar.
- Provides additional context on how budget calculations work.

## Installation & Usage
1. Install dependencies:
   ```bash
   pip install flask matplotlib
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Open `http://127.0.0.1:5000/` in a browser.

### Future Improvements
- **User Authentication**: Allow users to save their budget data across sessions.
- **Data Export**: Provide an option to download budget summaries in CSV or PDF format.
- **Enhanced Charts**: Include interactive graphs with filtering options.
- **AI Insights**: Offer AI-generated insights based on spending patterns.

## Contact
For any questions, reach out via email provided in `about.html`. Feedback is welcome to improve the functionality and usability of the web app.
