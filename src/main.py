from morse_code import encode, decode
from rich.console import Console



def main():
    console: Console = Console()
    console.print("[magenta][bold]Morse Code[/bold], Encode & Decode Morse Code.[/magenta]\n")
    
    while True:
        inp: str = console.input("[yellow][bold]message[/bold]:$[/yellow] ")
        
        if not inp: return
        
        console.print(f"[green bold]Encoded:[/green bold] [blue bold]{encode(string=inp)}[/blue bold]")
        console.print(f"[red bold]Decoded:[/red bold] [blue bold]{decode(string=inp)}[/blue bold]\n")


if __name__ == "__main__":
    main()