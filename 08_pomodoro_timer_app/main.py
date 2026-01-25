import argparse
import time

from rich import print
from rich.console import Console
from rich.live import Live
from rich.progress import Progress


def time_text(minutes: int, seconds: int, color: str = "green"):
    return f"[bold {color}]{minutes:02d}:{seconds:02d}[/bold {color}]"


def countdown(live, seconds):
    if seconds > 59:
        seconds = 59
    if seconds < 3:
        seconds = 3

    live.update("[bold green]Preparing to start...[/bold green]")
    time.sleep(1)
    while seconds >= 0:
        text = time_text(0, seconds)
        live.update(text)
        seconds -= 1
        time.sleep(1)
    live.update("[bold green]Let's start![/bold green]")
    time.sleep(1)


def main():
    # Parser
    parser = argparse.ArgumentParser(description="Pomodoro Timer")
    # Arguments
    parser.add_argument("--work", type=int, default=25, help="Work time in minutes")
    parser.add_argument("--rest", type=int, default=5, help="Rest time in minutes")
    parser.add_argument("--cycles", type=int, default=4, help="Number of cycles")
    parser.add_argument(
        "--countdown", type=int, default=5, help="Countdown time in seconds"
    )
    args = parser.parse_args()
    # Total times
    work_time = args.work * args.cycles
    rest_time = args.rest * (0 if args.cycles == 1 else args.cycles - 1)
    total_time = work_time + rest_time
    # Print information
    print(f"Work time: [bold red]{args.work}[/bold red] minutes")
    print(f"Rest time: [bold blue]{args.rest}[/bold blue] minutes")
    print(f"Number of cycles: [bold yellow]{args.cycles}[/bold yellow]")
    print(f"Total time: [bold purple]{total_time}[/bold purple] minutes")
    print("-" * 20)
    # Console
    console = Console()
    # Countdown
    with Live(console=console, screen=False, vertical_overflow="visible") as live:
        countdown(live, args.countdown)

    with Progress() as progress:
        task = progress.add_task("Working", total=work_time * 60)
        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(1)


if __name__ == "__main__":
    main()
