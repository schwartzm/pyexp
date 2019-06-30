import argparse 
import csv

parser = argparse.ArgumentParser()
parser.add_argument("--problems", type=str, default="problems.csv", help="Path to CSV problems file (problems.csv)")
args = parser.parse_args()

def main():
    print(f"Using problems file {args.problems}.")

    correct = 0
    answered = 0
    with open(args.problems, newline='') as problems:
        probreader = csv.reader(problems, delimiter=',')
        for row in probreader:
            answered += 1
            ans = input(f"{row[0]}? ")
            if int(ans) == int(row[1]):
               correct += 1
    
    print(f"You got {correct} correct out of {answered} answered.")
if __name__ == '__main__':
    main()
