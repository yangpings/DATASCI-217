import pandas as pd
import numpy as np
def new_data():
    dt = pd.read_csv('ms_data.csv')
    dt['visit_date'] = pd.to_datetime(dt['visit_date'])
    dt = dt.sort_values(by=['patient_id', 'visit_date']).reset_index(drop=True)

    insurance_types = pd.read_csv('insurance.lst', header=0, names=['insurance_type'])
    insurance_labels = insurance_types['insurance_type'].unique()
    patient_ids = dt['patient_id'].unique()
    np.random.seed(42)
    insurance_mapping = {pid: np.random.choice(insurance_labels) for pid in patient_ids}
    dt['insurance_type'] = dt['patient_id'].map(insurance_mapping)

    base_costs = {
    'Basic': 100,
    'Premium': 200,
    'Platinum': 300
    }
    dt['visit_cost'] = dt['insurance_type'].map(base_costs) + np.random.normal(0, 20, size=len(dt))
    mean1 = dt.groupby('education_level')['walking_speed'].mean()
    mean2 = dt.groupby('insurance_type')['visit_cost'].mean()
    correlation = dt['age'].corr(dt['walking_speed'])
    dt['month'] = dt['visit_date'].dt.month
    season_speed = dt.groupby('month')['walking_speed'].mean()
    return dt, mean1, mean2, correlation, season_speed
if __name__ == "__main__":
    dt, mean1, mean2, correlation, season_speed = new_data()
    print("Mean Walking Speed by Education Level:\n", mean1)
    print("\nMean Visit Costs by Insurance Type:\n", mean2)
    print("\nCorrelation between Age and Walking Speed:\n", correlation)
    print("\nSeasonal Variations in Walking Speed (by Month):\n", season_speed)


