import math
import sys
import argparse

VERSION = "1.0.0"

class Calculator:
    def __init__(self):
        self.history = []
        # Register math functions in a dictionary for easy access
        self.supported_names = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'sqrt': math.sqrt,
            'log': math.log,
            'log10': math.log10,
            'exp': math.exp,
            'pi': math.pi,
            'e': math.e,
            'pow': math.pow,
            'abs': abs,
            'round': round,
        }

    def evaluate(self, expression):
        try:
            # Use a limited scope for eval to provide some safety
            # though restricted eval is never fully safe in Python, 
            # for a CLI calculator it's standard unless we write a full parser.
            result = eval(expression, {"__builtins__": None}, self.supported_names)
            self.history.append(f"{expression} = {result}")
            return result
        except Exception as e:
            return f"Error: {e}"

    def show_history(self):
        if not self.history:
            print("No history yet.")
        for item in self.history:
            print(item)

    def interactive_mode(self):
        print(f"OmniCalc CLI v{VERSION}")
        print("Type 'help' for instructions, 'history' to see past calculations, or 'quit' to exit.")
        
        while True:
            try:
                expr = input("calc > ").strip()
                if not expr:
                    continue
                if expr.lower() in ['quit', 'exit', 'q']:
                    break
                if expr.lower() == 'help':
                    self.show_help()
                    continue
                if expr.lower() == 'history':
                    self.show_history()
                    continue
                
                result = self.evaluate(expr)
                print(result)
            except (KeyboardInterrupt, EOFError):
                print("\nExiting...")
                break

    def show_help(self):
        print("\n--- OmniCalc Help ---")
        print("Basic Operations: +, -, *, /, **, %")
        print("Functions: sqrt(x), sin(x), cos(x), tan(x), log(x), log10(x), exp(x), abs(x), round(x)")
        print("Constants: pi, e")
        print("Example: (pi * 2**2) + sqrt(16)")
        print("Commands: history, help, quit\n")

def main():
    parser = argparse.ArgumentParser(description="OmniCalc: An Advanced CLI Calculator")
    parser.add_argument("expression", nargs="?", help="The math expression to evaluate")
    parser.add_argument("-v", "--version", action="version", version=f"OmniCalc {VERSION}")
    
    args = parser.parse_args()
    
    calc = Calculator()
    
    if args.expression:
        # Command line mode
        print(calc.evaluate(args.expression))
    else:
        # Interactive mode
        calc.interactive_mode()

if __name__ == "__main__":
    main()
