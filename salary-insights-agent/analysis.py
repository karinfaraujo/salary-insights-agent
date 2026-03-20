import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def basic_analysis(df):
    insights = {}

    insights["average_salary"] = df["BasePay"].mean()

    insights["highest_paid_job"] = (
        df.groupby("JobTitle")["BasePay"]
        .mean()
        .idxmax()
    )
  
    insights["top_5_jobs"] = (
        df.groupby("JobTitle")["BasePay"]
        .mean()
        .sort_values(ascending=False)
        .head(5)
    )

    insights["salary_by_experience"] = (
        df.groupby("ExperienceLevel")["BasePay"]
        .mean()
    )

    insights["salary_by_worktype"] = (
        df.groupby("WorkType")["BasePay"]
        .mean()
    )
   
    insights["top_salary"] = (
    df.groupby("JobTitle")["BasePay"]
    .mean()
    .max()
    )
    
    return insights
