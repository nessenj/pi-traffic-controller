import time
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.live import Live

# Create a Console instance
console = Console()

def get_system_stats():
    now = datetime.now()
    dt_string = now.strftime("%b %d, %Y %H:%M:%S")

    with open('/dev/shm/sigstate.txt', 'r') as sigstate:
       for line in sigstate:
          sigs = line.strip()

    with open('/dev/shm/pedstate.txt', 'r') as pedstate:
       for line in pedstate:
          peds = line.strip()

    with open('/dev/shm/mode.txt', 'r') as mode:
       for line in mode:
          curmode = line.strip()

    with open('/dev/shm/state.txt', 'r') as state:
       for line in state:
          curstate = line.strip()

    with open('/dev/shm/timer.txt', 'r') as timer:
       for line in timer:
          timeleft = line.strip()

    return {
        curstate: sigs,
        timeleft: peds,
        "": "",
        curmode: dt_string
    }

def create_dashboard(stats):
    # Create a rich table to display the stats
    table = Table(title="Traffic Signal Dashboard")

    table.add_column("Metric", justify="right")
    table.add_column("1 2 3 4 5 6 7 8", justify="center")

    for key, value in stats.items():
        table.add_row(key, f"{value} %") if isinstance(value, (int, float)) else table.add_row(key, str(value))

    return table

def main():
    # Start the live dashboard
    with Live(auto_refresh=True, refresh_per_second=1) as live:
        while True:
            stats = get_system_stats()
            dashboard = create_dashboard(stats)
            live.update(dashboard)
            time.sleep(1)

if __name__ == "__main__":
    main()
