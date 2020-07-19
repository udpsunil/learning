# write your code here
with open('salary.txt') as salary_file:
    for salary in salary_file:
        yearly_salary = str(int(salary) * 12)
        with open('salary_year.txt', 'a') as salary_year_file:
            salary_year_file.write(yearly_salary+"\n")
