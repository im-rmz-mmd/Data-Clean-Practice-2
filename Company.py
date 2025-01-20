# Import Python Libraries
import pandas as pd
import numpy as np
from colorama import Fore

# Import Data
df = pd.read_csv("datset.csv")

# Remove Extra Columns
df = df.drop(['Income', 'id', 'Salary', 'Quote'], axis= 1)

# Change Columns Name
df = df.rename(columns= {'Full Name': 'Full_Name', 'Date of Birth': 'Date_of_Birth', 'email': 'Email',
                         'gender': 'Gender', 'Income.1': 'Income'})

# Fill Empty Rows and Change Unbelievable Data!
df['Country'] = df['Country'].str.split(pat= ' and').str[0]
df['Country'] = df['Country'].fillna('Traveler')

# Change and Fill Empty Rows
df['Income'] = df['Income'].replace({'$': np.nan})
df['Income'] = df['Income'].str.split(pat= '$').str[1]
df['Income'] = df['Income'].str.split(pat= '.').str[0]
df['Income'] = df['Income'].fillna(0)

# Change Columns Type
df = df.astype({'Income': 'int'})

# Output and illustration
print(df,
      Fore.BLUE + "\nMost of employess are %s" %(df['Gender'].value_counts().first_valid_index()),
      Fore.GREEN + "\nMost of employess work as %s" %(df['Job'].value_counts().first_valid_index()),
      Fore.CYAN + "\nMost of employess work in %s" %(df['Company'].value_counts().first_valid_index()),
      Fore.MAGENTA + "\nMost of employess are from %s" %(df['Country'].value_counts().first_valid_index()),
      Fore.YELLOW + "\nThe highest income of employess is %s" %(df['Income'].max()))