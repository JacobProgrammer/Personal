import webbrowser
import sys

print("Welcome to DreamCollege!")
print("We are going to ask you several questions to determine which college is the best for you!")

major = input("What is your major of interest?")

if major.lower() == "STEM" or "Stem" or "stem" or "Engineering" or "engineering":
    print("Great! Next question...")
elif major.lower() == "Mathematics" or "mathematics":
    print("Great! Next question...")
elif major.lower() == "English" or "english" or "ELA":
    print("Great! Next question...")
elif major.lower() == "Medicine" or "medicine" or "Med" or "med":
    print("Great! Next question...")
elif major.lower() == "Law" or "law":
    print("Great! Next question...")

interest = input("What is your desired speciality in your desired major?")

if interest.lower() == "Mechanical Engineering" or interest.lower() == "mechanical engineering":
    print("Excellent! Here are the best colleges in 2023 for Mechanical Engineering")
    webbrowser.open("https://www.usnews.com/best-graduate-schools/top-engineering-schools"
                    "/mechanical-engineering-rankings")
    sys.exit()

elif interest.lower() == "Chemical Engineering" or interest.lower() == "chemical engineering":
    print("Excellent! Here are the best colleges in 2023 for Chemical Engineering")
    webbrowser.open("https://www.usnews.com/best-graduate-schools/"
                    "top-engineering-schools/chemical-engineering-rankings")
    sys.exit()

if interest.lower() == "Algebra" or interest.lower() == "Educational":
    print("Excellent! Here are the best colleges in 2023 for Algebra")
    webbrowser.open("https://www.usnews.com/education/"
                    "best-global-universities/united-states/mathematics")
    sys.exit()

elif interest.lower() == "Calculus" or interest.lower() == "calculus":
    print("Excellent! Here are the best colleges in 2023 for Calculus")
    webbrowser.open("https://www.usnews.com/education/"
                    "best-global-universities/united-states/mathematics")
    sys.exit()

elif interest.lower() == "Educational Mathematics":
    print("Excellent! Here are the best colleges in 2023 for Educational Mathematics")
    webbrowser.open("https://www.collegefactual.com/majors/education/teacher-education"
                    "-and-development/mathematics-education/rankings/top-ranked/")
    sys.exit()

if interest.lower() == "Journalism" or interest.lower() == "journalism":
    print("Excellent! Here are the best colleges in 2023 for Journalism")
    webbrowser.open("https://www.collegefactual.com/majors/"
                    "communication-journalism-media/journalism/rankings/top-ranked/")
    sys.exit()
