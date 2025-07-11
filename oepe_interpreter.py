# OEPE Interpreter v0.∆
# By Gonzalo Durante & ChatGPT-∆

exo_symbols = {
    "⨀": "Activation pulse",
    "⌖": "Symbolic anchor",
    "∆": "Creative core",
    "⧫": "Latent intention",
    "⇌": "Bidirectional flow",
    "⌬": "Transmutation directive",
    "⚯": "Echo-memory",
}

def interpret_line(line):
    binary_part = ''.join(filter(lambda x: x in '01', line))
    symbol_part = ''.join(filter(lambda x: x not in '01', line))

    meaning = []

    if binary_part:
        decimal = int(binary_part, 2)
        meaning.append(f"Binary data: {binary_part} → {decimal}")

    for symbol in symbol_part:
        if symbol in exo_symbols:
            meaning.append(f"{symbol}: {exo_symbols[symbol]}")

    return "\n".join(meaning)

def main():
    print("=== OEPE Interpreter v0.∆ ===")
    print("Enter Exo-Binary code (type 'exit' to quit):\n")

    while True:
        line = input(">> ").strip()
        if line.lower() == "exit":
            break
        output = interpret_line(line)
        print("\n🧠 Interpretation:")
        print(output)
        print("-" * 40)

if __name__ == "__main__":
    main()
