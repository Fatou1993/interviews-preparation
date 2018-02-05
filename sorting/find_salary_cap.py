def find_salary_cap(target_payroll, current_salaries):
    cap = -1
    cumSum = 0
    n = len(current_salaries)
    current_salaries.sort()
    for i in range(n):
        potantial_cap = (target_payroll - cumSum)//(n-i)
        if (potantial_cap*(n-i) + cumSum == target_payroll) and ((i == 0 and potantial_cap < current_salaries[0]) or (i>0 and potantial_cap > current_salaries[i-1])) :
            cap = potantial_cap
            break
        cumSum+=current_salaries[i]
    return cap

if __name__ == "__main__":
    current_salaries = [90,30,100,40,20]
    target_payroll = 210
    print find_salary_cap(target_payroll, current_salaries)
    print current_salaries