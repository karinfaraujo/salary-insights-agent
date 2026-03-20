# 📊 Salary Insights Agent with Python

This project is a simple AI-inspired agent that analyzes salary data and automatically generates insights.

## 🚀 Features

- Loads salary dataset (CSV)
- Performs automatic analysis
- Identifies highest paying roles
- Calculates average salaries
- Compares salary by experience level
- Compares salary by work type (Remote, Hybrid, On-site)
- Generates a text report
- Displays a simple chart

## 🧠 How it works

The agent reads a dataset and simulates the work of a data analyst by extracting meaningful insights automatically, without manual queries.

## 📁 Project Structure

```bash
salary-insights-agent/
│
├── data/
│   └── salaries.csv
│
├── agent.py
├── analysis.py
├── README.md
├── report.txt
├── salary_chart.png
```

## ▶️ How to run

1. Install dependencies:

```bash
pip install pandas matplotlib
```

2. Run the agent:

```bash
python agent.py
```

## 📊 Example Output

Salary Insights Report

- Average Salary: $85,000
- Highest Paying Role: Data Scientist

Salary by Experience:

- Junior: $54,000
- Mid: $68,000
- Senior: $102,000

Salary by Work Type:

- Remote: $98,000
- Hybrid: $80,000
- On-site: $72,000

## 📈 Visualization

The project also generates a simple bar chart showing the average salary by experience level.

## 💡 Future Improvements

- Export reports as PDF
- Add more advanced visualizations
- Allow user input (interactive agent)
- Integrate with APIs for real-time data

## 👤 Author

Karin Araujo
