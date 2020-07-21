import argparse

parser = argparse.ArgumentParser(description='Add film star ratings')
parser.add_argument('--film-name', help='the film name', required=True)
parser.add_argument('--stars', type=int, help='star rating of the film', required=True)

args = parser.parse_args()

line = f"{args.film_name},{args.stars}\n"

with open("reviews.txt", "a+") as f:
    f.write(line)

print(f"Added: {line}")