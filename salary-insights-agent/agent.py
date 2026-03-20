from analysis import load_data, basic_analysis
import matplotlib.pyplot as plt

def generate_insights_text(insights):
    text = "\n🧠 Key Insights:\n"

    # Insight 1: Experience Level
    junior = insights["salary_by_experience"]["Junior"]
    senior = insights["salary_by_experience"]["Senior"]

    diff = ((senior - junior) / junior) * 100

    text += f"\n- Senior professionals earn {diff:.0f}% more than Junior professionals."

    # Insight 2: Work Type
    highest_worktype = insights["salary_by_worktype"].idxmax()
    text += f"\n- {highest_worktype} jobs tend to offer the highest salaries."

    # Insight 3: Average Salary (simple comparison)
    avg = insights["average_salary"]
    if avg > 80000:
        text += "\n- Overall salaries are relatively high in this dataset."
    else:
        text += "\n- Overall salaries are moderate in this dataset."

    return text

def generate_report(insights):
    report = f"""
📊 Salary Insights Report

- Average Salary: ${insights["average_salary"]:.2f}
- Highest Paying Role: {insights["highest_paid_job"]} (${insights["top_salary"]:.2f})

📈 Salary by Experience:
"""
    
    for exp, salary in insights["salary_by_experience"].items():
        report += f"\n  - {exp}: ${salary:.2f}\n"

    report += "\n\n🏠 Salary by Work Type:\n"

    for wt, salary in insights["salary_by_worktype"].items():
        report += f"\n  - {wt}: ${salary:.2f}"

    report += "\n" + generate_insights_text(insights)

    return report

def plot_chart(insights):
    insights["salary_by_experience"].plot(kind="bar"), 
    plt.title =("Average Salary by Experience Level")
    plt.ylabel("Salary")
    plt.xlabel("Experience Level")
    
    plt.savefig("salary_chart.png")
    plt.show()

def save_report(report, path="report.txt"):
    with open(path, "w", encoding="utf-8") as f:
        f.write(report)

if __name__ == "__main__":
    df = load_data("data/salaries.csv")
    insights = basic_analysis(df)

    report = generate_report(insights)
    print(report)

    plot_chart(insights)
    save_report(report)
