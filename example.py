from sent_tok_sk import SentenceTokenize
tokenizer = SentenceTokenize()
text = '''Moja veta. Moja druhá veta.'''
sentences = tokenizer.tokenize(text)

for i, sentence in enumerate(sentences, 1):
    print(f"Sentence {i}: {sentence}")