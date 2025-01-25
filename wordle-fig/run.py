import subprocess

first = ['crane']
target = ['silly', 'rower','squid', 'icing', 'reach', 'upper', 'crepe', 'crisp']

second = ['sloth', 'betel', 'icing', 'react', 'creme', 'stoop']

for f in first:
    for t in target:

        outfile = f"wordle-fig-{f}-{t}.pdf"

        subprocess.run(f"python gen-wordle-fig.py {f} {t}", shell=True, check=True)

        subprocess.run(f"pdflatex wordle-fig.tex", shell=True, check=True)

        subprocess.run(f"mv wordle-fig.pdf {outfile}", shell=True, check=True)

for s in second:

    outfile = f"wordle-fig-try-{s}.pdf"

    subprocess.run(f"python gen-blank-wordle-fig.py {s}", shell=True, check=True)

    subprocess.run(f"pdflatex wordle-fig.tex", shell=True, check=True)

    subprocess.run(f"mv wordle-fig.pdf {outfile}", shell=True, check=True)