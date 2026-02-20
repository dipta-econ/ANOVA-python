# Import Library
from scipy import stats
import pandas as pd

# Data Input
df = pd.read_csv('ANOVA3.csv')

# Define Treatement
T1 = df['Treatement1'].tolist()
T2 = df['Treatement2'].tolist()
T3 = df['Treatement3'].tolist()

# Set Hypothesis
print('H0: μ = μ₂ = μ₃')
print('H1: All means are not equal')

# Calculation
f_test, p_value = stats.f_oneway(T1, T2, T3)

# Result
print(f'F_Statistics: {f_test:.4f}')
print(f'P_Value: {p_value:.4f}')

# Interpreate
if p_value < 0.05:
    print('H0 is rejected and H1 is accepted.')
    print('All means are not equal')
else:
    print('H0 is accepted and H1 in rejected')
    print('μ = μ₂ = μ₃')
