from textblob import TextBlob
from textblob import Word
# from gensim.summarization import summarize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import spacy
from flair.models import TextClassifier
from flair.data import Sentence
from google.cloud import translate_v2 as translate
from langdetect import detect, DetectorFactory

class TextFeature():
    def __init__(self):
        pass
    
    @staticmethod
    async def extract_text_features(text):
        try:
            pass
        except Exception as e:
            pass
    
    @staticmethod
    async def summarize_text_by_sumy(text, num_sentences=2):
        try:
            # Parse the input text
            parser = PlaintextParser.from_string(text, Tokenizer("english"))

            # Create a LexRank summarizer
            summarizer = LexRankSummarizer()

            # Get a summary consisting of 2 sentences
            summary = summarizer(parser.document, num_sentences)

            summary_text = " ".join([str(sentence) for sentence in summary])
            return summary_text
        except Exception as e:
            pass
    
    @staticmethod
    async def summarize_text_by_spacy(text, num_sentences=3):
        # Load the spaCy model
        nlp = spacy.load('en_core_web_sm')

        doc = nlp(text)
        # Extract sentences
        sentences = list(doc.sents)

        # Rank sentences by length (as a simple heuristic)
        ranked_sentences = sorted(sentences, key=lambda sent: len(sent), reverse=True)

        # Join the top N longest sentences into a summary
        summary = " ".join([str(sent) for sent in ranked_sentences[:num_sentences]])
        return summary

    @staticmethod
    async def sentiment_analysis(text):
        try:
            sentiment_context = TextBlob("Textblob is amazingly simple to use. What great fun!")
            # print("sentiment_context.sentiment  :   ",sentiment_context.sentiment)
            # print("\nsentiment_context.sentiment.polarity  :   ", sentiment_context.sentiment.polarity)
            return sentiment_context.sentiment.polarity
        except Exception as e:
            raise Exception(f"Error sentiment_analysis: {str(e)}")  
    
    @staticmethod
    async def sentiment_analysis_by_flair(text):
        try:
            # Step 3: Load the sentiment analysis model
            classifier = TextClassifier.load('en-sentiment')

            # Step 5: Create a Sentence object
            sentence = Sentence(text)
            # Step 6: Predict sentiment
            print("Predict  :   ",classifier.predict(sentence))

            # Step 4: Extract sentiment label and score
            sentiment_label = sentence.labels[0].value  # This gives you the sentiment label (e.g., 'POSITIVE', 'NEGATIVE')
            sentiment_score = sentence.labels[0].score  # This gives you the score (e.g., 1.0)

            return sentiment_label, sentiment_score
        except Exception as e:
            raise Exception(f"Error sentiment_analysis_by_flair: {str(e)}")  

    @staticmethod
    async def fill_missing(text):
        try:
            pass
        except Exception as e:
            pass

    @staticmethod
    async def word_context(word:str):
        try:
            return Word(word).definitions
        except Exception as e:
            raise Exception(f"Error word_context: {str(e)}")

    @staticmethod
    async def spelling_correction_sent(text:str):
        """Spelling correction is based on Peter Norvig’s “How to Write a Spelling Corrector”[1] as implemented in the pattern library. It is about 70% accurate """
        try:
            b = TextBlob(text)
            # print(b.correct())
            return b.correct()
        except Exception as e:
            raise Exception(f"Error spelling_correction_sent: {str(e)}")

    @staticmethod
    async def spelling_correction_word(word: str):
        """Spelling correction is based on Peter Norvig’s “How to Write a Spelling Corrector”[1] as implemented in the pattern library. It is about 70% accurate """
        try:
            w = Word(word)
            return w.spellcheck()
        except Exception as e:
            raise Exception(f"Error spelling_correction_word: {str(e)}")

    @staticmethod
    async def sentence_separate(text):
        try:
            blob = TextBlob(text)
            sentences = []
            for s in blob.sentences:
                print(s)
                # print(s.classify())
                sentences.append(s)
            return sentences
        except Exception as e:
            raise Exception(f"Error sentence_separate: {str(e)}")

    @staticmethod
    async def detect_language_by_blob(text):
        try:
            blob = TextBlob(text)
            language = blob.detect_language()
            return f"The detected language is: {language}"
        except Exception as e:
            raise Exception(f"Error detect_language_by_blob: {str(e)}")

    @staticmethod
    async def detect_language_by_google(text):
        try:
            translate_client = translate.Client()
            result = translate_client.detect_language(text)
            return result
        except Exception as e:
            raise Exception(f"Error detect_language_by_google: {str(e)}")

    @staticmethod
    async def detect_language_by_lang(text):
        try:
            DetectorFactory.seed = 0
            language = detect(text)
            return language
        except Exception as e:
            raise Exception(f"Error detect_language_by_lang: {str(e)}")

    @staticmethod
    async def pluralize_text(text):
        try:
            sentence = TextBlob(text)
            print("\npluralize word: ", sentence.words[-1].pluralize())
        except Exception as e:
            raise Exception(f"Error pluralize_text: {str(e)}")
    
    @staticmethod
    async def singualize_text(text):
        try:
            sentence = TextBlob(text)
            print("\nsingual word: ", sentence.words[2].singularize())
        except Exception as e:
            raise Exception(f"Error singualize_text: {str(e)}")