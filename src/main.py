from morse_code import encode, decode
from rich.console import Console



def main():
    console: Console = Console()
    console.print("[magenta][bold]Morse Code[/bold], Encode & Decode Morse Code.[/magenta]\n")
    
    while True:
        inp: str = console.input("[yellow][bold]message[/bold]:$[/yellow] ")
        
        if not inp: return
        
        console.print(f"[green bold]Encoded:[/green bold] [cyan bold]{encode(string=inp)}[/cyan bold]")
        console.print(f"[red bold]Decoded:[/red bold] [cyan bold]{decode(string=inp)}[/cyan bold]\n")


if __name__ == "__main__":
    main()