import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {
    'Name': ['Vaibhav', 'Rajnish', 'Shivam', 'Bittu', 'Abhishek'],
    'OOPS':           [85, 90, 78, 92, 91],
    'Data Structure': [80, 85, 75, 95, 92],
    'MCA':            [78, 88, 70, 96, 95]
}
df = pd.DataFrame(data)
print(df)
df['Total'] = df[['OOPS', 'Data Structure', 'MCA']].sum(axis=1)
df['Average'] = np.mean(df[['OOPS', 'Data Structure', 'MCA']], axis=1)

print("\nUpdated Data:\n", df)
topper = df.loc[df['Total'].idxmax()]
print("\nTopper:\n", topper)
df['Result'] = df['Average'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
print("\nResult:\n", df[['Name', 'Result']])
plt.figure()
plt.bar(df['Name'], df['Total'])
plt.title("Student Total Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()