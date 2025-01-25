import sys


def number_to_color(num):

    if num == 0: # gray cell
        return ""
    elif num == 1: # yellow cell
        return "|[h]|"
    elif num == 2: # green cell
        return "|[g]|"
    elif num == 3: # input cell
        return "|[n]|"
    elif num == 4: # empty cell
        return "|[e]|"
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

    if len(sys.argv) != 2:
        raise RuntimeError("Missing input: guess")

    # first word
    word = sys.argv[1].upper()
    assert len(word) == 5

    colors = [3,3,3,3,3]
    
    with open(outfile, "w") as f:
        f.write(prefix)
        f.write(get_word_with_colors(word, colors))
        f.write(suffix)

    return 0


if __name__ == "__main__":
    main()
