import pandas as pd
import matplotlib.pyplot as plt

# ================== 1. UPLOAD CSV DATASET ==================
# File ka naam: StudentsPerformance.csv
df = pd.read_csv('StudentsPerformance.csv')

# ================== 2. DATA CLEANING ==================
df = df.dropna()
df = df.drop_duplicates()
df.columns = df.columns.str.strip()

# Columns rename - Math, English, Science
df = df.rename(columns={
    'math score': 'Math',
    'reading score': 'English', 
    'writing score': 'Science'
})

subjects = ['Math', 'English', 'Science']

# ================== 3. CALCULATE AVERAGE MARKS ==================
df['Total'] = df[subjects].sum(axis=1)
df['Average'] = df['Total'] / 3
df['Result'] = df['Average'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')

# ================== 4. HIGHEST AND LOWEST MARKS ==================
highest_avg = df['Average'].max()
lowest_avg = df['Average'].min()
topper = df.loc[df['Average'].idxmax()]
weakest = df.loc[df['Average'].idxmin()]

# ================== 5. PASS/FAIL PERCENTAGE ==================
pass_count = (df['Result']=='Pass').sum()
fail_count = len(df) - pass_count
pass_percentage = (pass_count / len(df)) * 100
fail_percentage = (fail_count / len(df)) * 100

# ================== 6. SUBJECT-WISE PERFORMANCE ==================
subject_avg = df[subjects].mean()
subject_max = df[subjects].max()
subject_min = df[subjects].min()

# ================== 7. PERFORMANCE REPORT ==================
print("="*50)
print("STUDENT RESULT ANALYSIS REPORT")
print("="*50)
print(f"Total Students: {len(df)}")
print(f"\nAVERAGE MARKS: {df['Average'].mean():.2f}")
print(f"HIGHEST AVERAGE: {highest_avg:.2f} | LOWEST AVERAGE: {lowest_avg:.2f}")
print(f"\nPASS/FAIL STATS:")
print(f"Pass: {pass_count} students ({pass_percentage:.1f}%)")
print(f"Fail: {fail_count} students ({fail_percentage:.1f}%)")
print(f"\nSUBJECT-WISE AVERAGE:")
for sub in subjects:
    print(f"{sub}: {subject_avg[sub]:.2f}")
print("="*50)

print("\nTop 5 Students:")
print(df.nlargest(5, 'Average')[['Math','English','Science','Average','Result']])

# 8. CHARTS AND GRAPHS ==================

# CHART 1: BAR CHART - Subject Wise Average
plt.figure(figsize=(10,6))
bars = plt.bar(subjects, subject_avg, color=['#2196F3', '#FF9800', '#9C27B0'], edgecolor='black')
plt.title('Subject-Wise Average Performance', fontsize=16, fontweight='bold')
plt.ylabel('Average Marks', fontsize=12)
plt.ylim(0, 100)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 1,
             f'{height:.1f}', ha='center', va='bottom', fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.savefig('subject_bar_chart.png', dpi=300, bbox_inches='tight')
plt.show()

# CHART 2: PIE CHART - Pass/Fail Percentage
plt.figure(figsize=(8,8))
result_counts = df['Result'].value_counts()
colors = ['#4CAF50', '#F44336']
plt.pie(result_counts, labels=result_counts.index, autopct='%1.1f%%',
        colors=colors, startangle=90, explode=(0.05, 0))
plt.title('Pass vs Fail Percentage', fontsize=16, fontweight='bold')
plt.savefig('pass_fail_pie.png', dpi=300, bbox_inches='tight')
plt.show()

# CHART 3: BAR CHART - Highest vs Lowest Marks Per Subject
plt.figure(figsize=(10,6))
x = range(len(subjects))
plt.bar([i - 0.2 for i in x], subject_max, width=0.4, label='Highest', color='#4CAF50', edgecolor='black')
plt.bar([i + 0.2 for i in x], subject_min, width=0.4, label='Lowest', color='#F44336', edgecolor='black')
plt.xticks(x, subjects)
plt.title('Highest vs Lowest Marks Per Subject', fontsize=16, fontweight='bold')
plt.ylabel('Marks', fontsize=12)
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.savefig('high_low_bar.png', dpi=300, bbox_inches='tight')
plt.show()

# CHART 4: HISTOGRAM - Average Marks Distribution
plt.figure(figsize=(10,6))
plt.hist(df['Average'], bins=20, color='#673AB7', edgecolor='black', alpha=0.7)
plt.title('Average Marks Distribution', fontsize=16, fontweight='bold')
plt.xlabel('Average Marks', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.axvline(df['Average'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["Average"].mean():.1f}')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.savefig('marks_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n✅ ALL OUTPUTS GENERATED:")
print("1. subject_bar_chart.png - Bar Chart")
print("2. pass_fail_pie.png - Pie Chart")
print("3. high_low_bar.png - Bar Chart")
print("4. marks_distribution.png - Histogram")
print("5. Terminal Performance Report")