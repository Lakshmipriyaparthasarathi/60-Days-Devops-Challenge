import argparse

parser = argparse.ArgumentParser(description="Demo for argument parsing")
parser.add_argument("name", help="Your name")
parser.add_argument("--age", type=int, help="Your age", default=18)

args = parser.parse_args()
print(f"Hello {args.name}, you are {args.age} years old.")
