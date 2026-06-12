import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from openpyxl.styles.builtins import total
print("===STUDENTS ACADEMIC PERFORMANCES ANALYSIS===")
print("===FRIST 5 ROWS===\n")

df = pd.read_csv('C:/Users/Dhinakaran S/Desktop/Project 1/Student-performance-Analytics/data/Project 1.csv.csv')
print(df.head())
print('-'*100)

print("===SHAPE===")
print(df.shape)
print('-'*100)

print("===COLUMNS===")
print(df.columns)
print('-'*100)

print("===MISSING VALUES===")
print(df.isnull().sum())
print('-'*100)

print("===TOTAL & AVERAGE===")

df['total'] = (df['tamil']+
               df['english']+
               df['maths']+
               df['science'])
df['average'] = df['total']/4

print(df[['name','total','average']])
print('-'*100)

print("===NUMPY STATISTICS===")

marks = np.array(df['total'])

print('HIGHEST MARK :',np.max(marks))
print('LOWEST MARK:',np.min(marks))
print('AVERAGE MARK:',np.mean(marks))
print('TOTAL MARK:',np.sum(marks))
print('-'*100)

print("===BAR CHART===")
plt.figure(figsize=(10,5))
plt.bar(df['name'], df['total'],color='blue')
plt.title("STUDENT PERFORMANCE")
plt.xlabel("SUBJECT NAME")
plt.ylabel("STUDENT MARKS")
plt.savefig("C:/Users/Dhinakaran S/Desktop/Project 1/Student-performance-Analytics/charts/bar_chart.png")
plt.show()
print('-'*100)

print("===BEST STUDENTS===")
s = df[df['total'] == df['total'].max()]
print(s[['name','total']])
print('-'*100)

print("===NEED IMPROVEMENT===")
d =df[df['total'] == df['total'].min()]
print(d[['name','total']])

print("===LINE CHART===")

plt.plot(df['name'],df['average'],color='blue',marker='p',linestyle='dotted')
#plt.title("STUDENT PERFORMANCES")
#plt.xlabel("STUDENT NAME")
#plt.ylabel("AVERAGE MARK")
plt.savefig(r"C:/Users/Dhinakaran S/Desktop/Project 1/Student-performance-Analytics/charts/line_chart.png")
print('-'*100)
plt.show()

print("===PIE CHART===")
dept = df['department'].value_counts()
plt.pie(dept,labels=dept.index)
autopct='%1.1f%%'
colors=['blue','green','orange']
plt.title('DEPARTMENT DISTRIBUTIONS')
plt.savefig(r"C:/Users/Dhinakaran S/Desktop/Project 1/Student-performance-Analytics/charts/Pie_chart.png")
plt.show()

print("===HISTOGRAM CHART===")
plt.hist(df['total'],bins=5,color='orange')
plt.title('marks Distribution')
plt.xlabel('Total marks')
plt.ylabel('number of students')
plt.savefig(r"C:/Users/Dhinakaran S/Desktop/Project 1/Student-performance-Analytics/charts/Histogram_chart.png")
plt.show()

print("===DEPARTMENT ANALYSIS===")
dept_avg = df.groupby('department')['average'].mean()
print(dept_avg)

print("STUDENT GRADE===")

def assign_grade(avg):
    def assign_grade(avg):
        if avg >= 90:
            return "A GRADE"
        elif avg >= 80:
            return "B GRADE"
        elif avg >= 70:
            return "C GRADE"
        else:
            return "D GRADE"
df['grade'] = df['average'].apply(assign_grade)
print(df[['name','average','grade']])

print("===RESULT SAVED.CSV FILE===")

df.to_csv(r'C:\Users\Dhinakaran S\Desktop\Project 1\Student-performance-Analytics\output\RESULT.CSV.CSV',index=False)
print("success")

print("===RESULT SAVED.EXCEL FILE===")
df.to_excel(r'C:\Users\Dhinakaran S\Desktop\Project 1\Student-performance-Analytics\output/RESULT_EXCEL.xlsx',index=False)
print("success")

print("===RESULT SAVED.JSON FILE===")
df.to_json(r'C:\Users\Dhinakaran S\Desktop\Project 1\Student-performance-Analytics\output/RESULT.JSON.json',index=False)
print("success")

print("===STUDENT DETAILS===")
class student:
        def __init__(self, name, age, total, average):
            self.name = name
            self.age = age
            self.total = total
            self.average = average
        def display(self):
            print(f'Name:', self.name)
            print(f'Age:', self.age)
            print(f'total:', self.total)
            print(f'average:',self.average)
        def grade(self):
            if self.average>= 90:
                return "A Grade"
            elif self.average >= 80:
                return "B Grade"
            elif self.average>=70:
                return "C Grade"
            else:
                return "D GRADE"

s1 = student("Dhina",19,358,89.5)
s1.display()
print("Grade:",s1.grade())

print("===LOADING FILE===")

try:
    df =pd.read_csv(r'C:/Users/Dhinakaran S/Desktop/Project 1/RESULY.csv')
    print('FILE LOADED SUCCESSFULLY')
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print(f'error:{e}')
finally:
    print("program completed")

#plt.savefig("charts/Line_chart.png")