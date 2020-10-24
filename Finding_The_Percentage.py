"""
PROBLEM STATEMENT

The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Example

marks key:value pairs are
'alpha':[20,30,40]
'beta':[30,50,70]
query_name = 'beta'
The query_name is 'beta'. beta's average score is (30+50+70)/3 = 50.0

Input Format

The first line contains the integer n, the number of students' records. The next n lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

Constraints

2 <= n <= 10
0 <= marks[i] <= 100
length of marks arrays = 3

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input 0

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output 0

56.00

Explanation 0

Marks for Malika are {52,56,60} whose average is (52+56+60)/3 = 56

Sample Input 1

2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh

Sample Output 1

26.50

"""

#SOLUTION

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
print("{0:.2f}".format(round(sum(student_marks[query_name]) / len(student_marks[query_name]), 2)))