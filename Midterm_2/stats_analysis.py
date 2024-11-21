import pandas as pd
import statsmodels.formula.api as smf
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from analyze_visits import new_data
dt, mean1, mean2, correlation, season_speed = new_data()
dt['education_level'] = dt['education_level'].astype('category')

pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_rows', None)  # Show all rows (optional)

model_ols = smf.ols("walking_speed ~ age + C(education_level)", data=dt).fit()
print(model_ols.summary())

cost_summary = dt.groupby('insurance_type')['visit_cost'].describe()
print("\nSummary Statistics for Costs by Insurance Type:\n", cost_summary)
sns.boxplot(x='insurance_type', y='visit_cost', data=dt)
plt.title("Visit Cost by Insurance Type")
plt.xlabel("Insurance Type")
plt.ylabel("Visit Cost")
plt.show()
insurance_groups = dt.groupby('insurance_type')['visit_cost'].apply(list)
f_statistic_cost, p_value_cost = stats.f_oneway(*insurance_groups)
print("ANOVA F-statistic for cost by insurance type:", f_statistic_cost)
print("ANOVA p-value for cost by insurance type:", p_value_cost)

model_interaction = smf.ols("walking_speed ~ age * C(education_level)", dt).fit()
print("\nInteraction Effects between Education and Age on Walking Speed")
print(model_interaction.summary())
model_confounded = smf.ols("walking_speed ~ age * C(education_level) + insurance_type", dt).fit()
print("\nConfounded Model with Insurance Type:")
print(model_confounded.summary())