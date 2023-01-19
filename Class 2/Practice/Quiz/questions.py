from rich import print

score = 0
def quiz(score):
    question_1 = int(input("What is the 1099 K limit for 2022? "))
    if question_1 == 20000:
        print("[bold green]Correct[/bold green]!")
        score+1
    else:
        print("[bold red]Incorrect[/bold red]!")
    question_2 = int(input("What is the standard daduction  for singles in 2023?"))
    if question_2 == 13850:
        print("[bold green]Correct[/bold green]!")
        score+1
    else:
        print("[bold red]Incorrect[/bold red]!")
    question_3 = int(input("What is the current top marginal federal income tax rate for individuals?"))
    if question_3 == 37:
        print("[bold green]Correct[/bold green]!")
        score+1
    else:
        print("[bold red]Incorrect[/bold red]!")
    question_4 = int(input("What is the current top marginal federal income tax rate for corporations?"))
    if question_4 == 21:
        print("[bold green]Correct[/bold green]!")
        score+=1
    else:
        print("[bold red]Incorrect[/bold red]!")
    question_5 = int(input("What is the current top marginal federal income tax rate for pass-through entities?"))
    if question_5 == 37:
        print("[bold green]Correct[/bold green]!")
        score+=1
    else:
        print("[bold red]Incorrect[/bold red]!")
    return score


quiz(score)
print(F"Your score is {score} out of 5")



