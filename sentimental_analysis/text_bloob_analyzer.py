import textblob
from textblob import TextBlob

def analysis():
    analysis = TextBlob("La mesa  estupida")
    print(analysis.sentiment)

    print(analysis.tags)

    print(analysis.translate(to='es'))

    print(dir(analysis))

if __name__ == '__main__':
    analysis()