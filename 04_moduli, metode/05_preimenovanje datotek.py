import os

extensions = [".avi", ".mpg", ".mkv", ".rm", ".mp4, .txt"]
notCapital = ["a", "an", "the",
              "above", "against", "along", "alongside", "amid", "amidst", "around", "as",
              "aside", "astride", "at", "athwart", "atop", "before", "behind", "below",
              "beneath", "beside", "besides", "between", "beyond", "but", "by", "down",
              "during", "for", "from", "in", "inside", "into", "of", "on", "onto", "out",
              "outside", "over", "per", "plus", "than", "through", "throughout", "till",
              "to", "toward", "towards", "under", "underneath", "until", "upon", "versus",
              "via", "with", "within", "without"]

for i in range(3):
    os.chdir('..')

os.chdir('Downloads/programiranje')

for fname in os.listdir('.'):
    fname = fname.lower()
    osnova, koncnica = os.path.splitext(fname)
    if koncnica not in extensions:
        continue
    osnova = osnova.replace('.', ' ')
    besede = osnova.split()
    for i in range(len(besede)):
        if i == 0 or besede[i-1] == '-' or besede[i] not in notCapital:
            besede[i] = besede[i].capitalize()
    osnova = ' '.join(besede)
    os.rename(fname, osnova + koncnica)