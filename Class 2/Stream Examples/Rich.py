from rich import print
# import rich

print("[bold red]Hello[/bold red] World!")
print("[italic green]This is some new colored text[/italic green]")
print("[underline blue]This is some new colored text[/underline blue]")

answer = input("Is Python cool? ")
if answer == "yes":
    print("[bold green]Yes it is![/bold green]")
else:
    print("[bold red]you're not cool[/bold red]")
