import argparse
import sys
import os
from .obfuscator import Obfuscator

def main():
    parser = argparse.ArgumentParser(
        description="texp – Privacy protector for LaTeX source: strip stylistic fingerprints from .tex files before sharing.",
        epilog="Example: texp paper.tex -s high -o paper_obf.tex"
    )
    parser.add_argument("input", help="Input .tex file path")
    parser.add_argument("-o", "--output", help="Output file path (default: input_obf.tex)")
    parser.add_argument("-s", "--strength", choices=["low", "medium", "high"], default="medium",
                        help="Obfuscation strength (default: medium)")
    parser.add_argument("--seed", type=int, help="Random seed for reproducibility")
    parser.add_argument("--no-comments", action="store_false", dest="comments",
                        help="Disable comment insertion")
    parser.add_argument("--no-spaces", action="store_false", dest="spaces",
                        help="Disable harmless spaces")
    parser.add_argument("--no-commands", action="store_false", dest="commands",
                        help="Disable command replacement")
    parser.add_argument("--no-options", action="store_false", dest="options",
                        help="Disable package option shuffling")
    parser.add_argument("--no-quotes", action="store_false", dest="quotes",
                        help="Disable quote variation")
    parser.add_argument("--no-macros", action="store_false", dest="macros",
                        help="Disable macro injection")

    args = parser.parse_args()

    # Check input file existence
    if not os.path.isfile(args.input):
        print(f"Error: Input file '{args.input}' not found.", file=sys.stderr)
        sys.exit(1)

    # Determine output file
    if args.output is None:
        base, ext = os.path.splitext(args.input)
        args.output = f"{base}_obf{ext}"

    # Read input
    with open(args.input, "r", encoding="utf-8") as f:
        content = f.read()

    # Obfuscate — each flag controls whether its transformation runs
    obf = Obfuscator(
        strength=args.strength, seed=args.seed,
        enable_comments=args.comments,
        enable_spaces=args.spaces,
        enable_commands=args.commands,
        enable_options=args.options,
        enable_quotes=args.quotes,
        enable_macros=args.macros,
    )
    obfuscated = obf.obfuscate(content)

    # Write output
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(obfuscated)

    print(f"Obfuscated LaTeX written to: {args.output}")
    print(f"Strength: {args.strength} | Seed: {args.seed if args.seed is not None else 'random'}")

if __name__ == "__main__":
    main()
