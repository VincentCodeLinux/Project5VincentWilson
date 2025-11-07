import Project5Helpers
import colorama
from colorama import Fore, Back, Style
colorama.init()

data = Project5Helpers.get_job_data()

salary_input = float(input("What would you like your salary to be?"))

for jobs_ori in data:
    if jobs_ori["starting_salary"] >= salary_input:
        print(jobs_ori["job_class"], ":", jobs_ori["starting_salary"])

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
print(Back.BLUE + "Here are the jobs choices to choose from")
print(Style.RESET_ALL)
print()


for careers in data:
        if careers["job_class"] in jobs_offered:
            jobs_displayed = jobs_offered[careers['job_class']]
            print(jobs_displayed, ":", careers["starting_salary"])


print()
job_input = input("Which job would you like?")

for chosenjob in data:
    if chosenjob["job_class"] in jobs_offered:
        if jobs_offered[chosenjob["job_class"]] >= job_input:
            if chosenjob["starting_salary"] >= salary_input:
                print("The job above the salary you asked for")
            else:
                print(Back.RED + f"The job is below the salary you asked for. The salary for the job is {chosenjob['starting_salary']}")
                print(Style.RESET_ALL)
            break



