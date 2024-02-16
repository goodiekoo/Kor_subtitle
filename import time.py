from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn , BarColumn, TimeRemainingColumn,TaskProgressColumn
import time

with Progress(f"output message",BarColumn(),TaskProgressColumn(), SpinnerColumn(), TimeElapsedColumn() ) as progress:
    task = progress.add_task("",total = 1)
    cnt = 0
    while not progress.finished:
        cnt = cnt +1
        print(cnt)
        time.sleep(0.1)
        progress.update(task, advance=0.1)