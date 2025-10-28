episodes = [
    ["Home", "Coffee", "Coffee", "Chat", "Chat", "Coffee", "Computer", "Computer", "Home"],
    ["Computer", "Computer", "Chat", "Chat", "Coffee", "Computer", "Computer", "Computer"],
    ["Home", "Home", "Coffee", "Chat", "Computer", "Coffee", "Coffee"],
]

if __name__ == '__main__':
    matrix = {}
    for episode in episodes:
        for src, tgt in zip(episode[:-1], episode[1:]):
            table = matrix.setdefault(src, {})
            table[tgt] = table.get(tgt, 0) + 1
    matrix = {s: {k: v / sum(t.values()) for k, v in t.items()} for s, t in matrix.items()}

    for source, targets in matrix.items():
        print(source, "->", targets)
        