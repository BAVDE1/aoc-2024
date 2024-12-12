

def read_file(day: int):
    with open(f'_{day}') as fh:
        return fh.read().strip()