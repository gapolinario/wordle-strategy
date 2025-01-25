import sys


def number_to_color(num):

    if num == 0:
        return ""
    elif num == 1:
        return "|[h]|"
    elif num == 2:
        return "|[g]|"
    else:
        raise ValueError(f"Invalid number. Received {num}")


def get_word_with_colors(word, colors):

    out = ""
    for letter, color in zip(word[:-1], colors[:-1]):
        out += number_to_color(color) + letter + r" \& "

    out += number_to_color(colors[-1]) + word[-1]

    return out


def main():

    outfile = "word.tex"

    prefix = r"\matrix(titlewordle)[wordlematrix, ampersand replacement=\&]{"
    suffix = r"\\};"

    if len(sys.argv) != 3:
        raise RuntimeError("Missing input: first guess and solution")

    # first word
    word = sys.argv[1].upper()
    assert len(word) == 5
    # solution
    target = sys.argv[2].upper()
    assert len(target) == 5

    colors = [0, 0, 0, 0, 0]

    for i, letter in enumerate(word):

        if letter == target[i]:
            colors[i] = 2
        elif letter in target:
            colors[i] = 1

    with open(outfile, "w") as f:
        f.write(prefix)
        f.write(get_word_with_colors(word, colors))
        f.write(suffix)

    return 0


if __name__ == "__main__":
    main()
