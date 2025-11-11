import Project5Helpers
import colorama
from colorama import Fore, Back, Style #This is importing the needed tools for text modification later in the code
colorama.init()

data = Project5Helpers.get_job_data()

#This is where I put the code for the input where the user tells the program what they want for a starting salary
salary_input = float(input("What would you like your salary to be?"))

#Heres where it checks the staring salary and compares it to jobs that align with it.
for jobs_ori in data:
    if jobs_ori["starting_salary"] >= salary_input:
        print(jobs_ori["job_class"], ":", jobs_ori["starting_salary"])

#Heres my job map where it maps the jobs in job_class to the job options that are given to the user
jobs_offered = {"Information Security Analysts": "Software Security (Cyber Security)",
                       "Computer Network Support Specialists": "Penetration Tester (Cyber Security)",
                       "Computer Network Architects": "Penetration Tester (Cyber Security)",
                       "Computer Occupations, All Other": "Digital Forensics (Cyber Security)",
                       "Software Developers": "Software Developer (Computer Science)",
                       "Software Quality Assurance Analysts and Testers": "Software Testing SDET (Computer Science)",
                       "Database Administrators": "Database Professional (Mostly Computer Science and Some Cyber Security)",
                       "Web Developers": "Web Developer (Computer Science)",
                       "Computer Systems Analysts": "DevOps/Those who can talk with humans and understand code and infrastructure deeply"}

print()
print(Back.BLUE + "Here are the jobs choices to choose from") #This is the text telling the user that these are the jobs to choose from
print(Style.RESET_ALL)
print()

#This prints the jobs in the job map with there starting salary
for careers in data:
        if careers["job_class"] in jobs_offered:
            jobs_displayed = jobs_offered[careers['job_class']]
            print(jobs_displayed, ":", careers["starting_salary"])

#This is asking the user to pick a job from the list
print()
job_input = input("Which job would you like?")

#This is my big for loop that cycles through all the code in the second having of the project according to the job chosen
for chosenjob in data:
    salary_diff = chosenjob["ave_annual_salary"] - chosenjob["median_annual_salary"] #Difference in average/median salary variable
    percent_diff = round((salary_diff / chosenjob["median_annual_salary"]) * 100, 3) #Percentage difference variable pulling from salary_diff variable divided ny median salary of job chosen
    if chosenjob["job_class"] in jobs_offered:
        if jobs_offered[chosenjob["job_class"]] == job_input:
            if chosenjob["starting_salary"] >= salary_input: #This checks if the salary is within range of what the user inputted
                print("The job above the salary you asked for")
                print()
                print(f"There are around {chosenjob["ma_emp_num"]} in this field") #This tells how many jobs are in the job chosen
            else:
                print(Back.RED + f"The job is below the salary you asked for. The starting salary for the job is {chosenjob['starting_salary']}") #States the starting salary if it meets a certain criteria
                print(Style.RESET_ALL)

            if chosenjob["median_annual_salary"] > salary_input: #Checks if the median salary is greater or equal to the salary inputted
                    print(Fore.GREEN + Style.BRIGHT + f"The median salary is above the salary you asked for, which is {chosenjob['median_annual_salary']}")
                    print(Style.RESET_ALL)
            else:
                    print(f"The median salary is {chosenjob['median_annual_salary']}, which is below the salary you inputed.") #States its below the salary inputed if it doesnt meet any other criteria
                    print(f"There are around {chosenjob["ma_emp_num"]} in this field")

            if chosenjob["ave_annual_salary"] > chosenjob["median_annual_salary"] * 1.05:  #Compares average and median * 5 percent to see if its within that 5 percent range in the project guildlines
                salary_diff = chosenjob["ave_annual_salary"] - chosenjob["median_annual_salary"] # Subtracts the average salary of the job minus the median salary of the job
                percent_diff = round((salary_diff / chosenjob["median_annual_salary"]) * 100, 3)
                print(Fore.BLUE + Style.BRIGHT + f"The average salary which for the job is {chosenjob['ave_annual_salary']}, and is {percent_diff}% higher than the median salary which is {chosenjob['median_annual_salary']}.") #Tells the user the average is higher than the median
                print(f"This means that there are a few people that are getting paid higher than usual causing an inflation in the numbers") #Gives a reason why its higher
                print(Style.RESET_ALL)  #resets the bold and color
            if chosenjob["ave_annual_salary"] < chosenjob["median_annual_salary"]: #Sees if average is less than or equal to the median
                salary_diff = chosenjob["ave_annual_salary"] - chosenjob["median_annual_salary"]
                percent_diff = round((salary_diff / chosenjob["median_annual_salary"]) * 100, 3)
                print(Fore.YELLOW + f"The median salary of {chosenjob["median_annual_salary"]} is {percent_diff}% higher than {chosenjob['ave_annual_salary']}.") #Prints that the median is higher than the average
                print(f"This means that there are a few low paid workers that are pulling down the average") #Prints a reason why its higher
                print(Style.RESET_ALL)
            if chosenjob["ave_annual_salary"] > chosenjob["median_annual_salary"] and chosenjob["ave_annual_salary"] < chosenjob["median_annual_salary"] * 1.05: #This sees if the average salary is within the 5 percent range of the median salary but still greater than the base median salary
                print(Fore.MAGENTA + f"The average salary which for the job is {chosenjob['ave_annual_salary']}, and is {percent_diff}% higher than the median salary which is {chosenjob['median_annual_salary']}.")
                print(Style.RESET_ALL)
            if chosenjob["top_salary"] > salary_input: #This checks and sees if the top salary is higher than the original salary inputted
                print(Back.RED + Style.BRIGHT + f"The top salary for the job is {chosenjob['top_salary']} which is greater than the starting salary you inputed")
                print(Style.RESET_ALL)

input("Press Enter/Return to see skills needed for the job you chose")
count = 0 # Sets the variable of count to 0
for chosenjob in data:
        if chosenjob["job_class"] in jobs_offered:
            if jobs_offered[chosenjob["job_class"]] == job_input: #Checking to see the job that was input according to the job map
                if "needed_skills" in chosenjob: #Using if in seeing the skills in the job that was chosen
                    for skill in chosenjob['needed_skills']:
                        print(skill['skill']) #Prints the skills
                        count += 1 # Adds to the count variable
                        if count % 30 == 0: # Checks to see how many skills it has looped through to try and see if it should end or not
                            input("Press Enter/Return to see more skills needed for the job you chose")