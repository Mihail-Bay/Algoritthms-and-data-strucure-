import sys
import os

from Lab6.utils import read_input, write_output, decorate
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def process_elections(rd):
    votes = {}

    infile = rd
    for line in infile:
        parts = line.strip().split()
        candidate = parts[0]
        num_votes = int(parts[1])

        # Добавляем голоса кандидату
        if candidate in votes:
            votes[candidate] += num_votes
        else:
            votes[candidate] = num_votes


    sorted_candidates = sorted(votes.items())

    out = ''
    for candidate, total_votes in sorted_candidates:
        out = out + f"{candidate} {total_votes}\n"
    return out

def main():
    out = process_elections(read_input(5))
    write_output(5, out)
    print(out)
    print()


if __name__ == '__main__':
    decorate(task=5, task_name='Process_elections')