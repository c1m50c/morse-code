from morse_code import encode, decode
from rich.console import Console


def main() -> None:
    console: Console = Console()
    console.print("[magenta][bold]Morse Code[/bold], Encode & Decode Morse Code.[/magenta]\n")
    
    while True:
        inp: str = console.input("[yellow][bold]message[/bold]:$[/yellow] ")
        
        if not inp:
            break
        
        encoded, decoded = encode(string=inp), decode(string=inp)
        
        console.print(f"[green bold]Encoded:[/green bold] [cyan bold]{encoded}[/cyan bold]")
        console.print(f"[red bold]Decoded:[/red bold] [cyan bold]{decoded}[/cyan bold]\n")


if __name__ == "__main__":
    main()