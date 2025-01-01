from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--output', '-o', required=True, help='help')
parser.add_argument('--text', '-t', required=True, help='help text')

args = parser.parse_args()

with open(args.text, 'w') as f:
    f.write(args.text+'\n')

print(f'Wrote "{args.text}" to "{args.output}"')

