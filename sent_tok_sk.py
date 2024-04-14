import re

class SentTokSK:
    def __init__(self):
        # Define patterns for sentence boundaries
        self.sentence_end_patterns = [
            r'(?<=[.!?]) +',
            r'(?<=[.!?])"',
            r'(?<=[.!?]\w)\'(?=\s)',
            r'(?<=[.!?]")\'(?=\s)',
            r'(?<=[.!?])\'(?=\w)',
            r'(?<=[.!?]")\'(?=\w)',
            r'(?<=[.!?])[\n]+',
            r'(?<=[.!?])$',  # handles end of text
        ]
        # Compile the regular expressions
        self.sentence_end_regex = re.compile('|'.join(self.sentence_end_patterns))

    def tokenize(self, text):
        # Apply the sentence boundary rules
        sentences = self.sentence_end_regex.split(text)
        # Filter out empty strings and strip whitespace
        sentences = [s.strip() for s in sentences if s.strip()]
        # Post-process to handle abbreviations and cases with lowercase letters
        i = 0
        while i < len(sentences) - 1:
            # Check if the token is a title
            if re.match(r'\b(?:|mr\.|mrs\.|ms\.|dr\.|doc\.|rndr\.|mudr\.|paeddr\.|judr\.|phdr\.|ing\.|mgr\.|rcdr\.|rsdr\.|MR\.|MRS\.|MS\.|DR\.|DOC\.|RNDR\.|MUDR\.|PAEDDR\.|JUDR\.|PHDR\.|ING\.|MGR\.|RCDR\.|RSDR\.|Mr\.|Mrs\.|Ms\.|Dr\.|Doc\.|RNDr\.|MUDr\.|PaedDr\.|JUDr\.|PhDr\.|Ing\.|Mgr\.|RcDr\.|RsDr\.)\s*$', sentences[i].split()[-1]):
                # If the title is followed by an uppercase letter or another title
                if i + 1 < len(sentences) and (re.match(r'\b[A-Z]', sentences[i + 1].lstrip()) or re.match(r'\b(?:|mr\.|mrs\.|ms\.|dr\.|doc\.|rndr\.|mudr\.|paeddr\.|judr\.|phdr\.|ing\.|mgr\.|rcdr\.|rsdr\.|MR\.|MRS\.|MS\.|DR\.|DOC\.|RNDR\.|MUDR\.|PAEDDR\.|JUDR\.|PHDR\.|ING\.|MGR\.|RCDR\.|RSDR\.|Mr\.|Mrs\.|Ms\.|Dr\.|Doc\.|RNDr\.|MUDr\.|PaedDr\.|JUDr\.|PhDr\.|Ing\.|Mgr\.|RcDr\.|RsDr\.)\s*$', sentences[i + 1].lstrip())):
                    # Combine into one sentence
                    sentences[i] += ' ' + sentences[i + 1]
                    del sentences[i + 1]
                else:
                    # Otherwise, move to the next sentence
                    i += 1 

            # PhD, CSC titles
            elif re.match(r'\b(?:|PhD\.|CsC\.|phd\.|csc\.)\s*$', sentences[i].split()[-1]):
                # If the next token is a lowercase letter or name
                if i + 1 < len(sentences) and (re.match(r'\b[a-z]', sentences[i + 1].lstrip()) or re.match(r'\b(?:|CsC\.)\s*$', sentences[i + 1].lstrip())):
                    # Combine into one sentence
                    sentences[i] += ' ' + sentences[i + 1]
                    del sentences[i + 1]
                else:
                    # Otherwise, move to the next sentence
                    i += 1

            # PhD, CSC titles
            elif re.match(r'\b(?:|PHD\.|CSC\.)\s*$', sentences[i].split()[-1]):
                # If the next token is an uppercase letter or name
                if i + 1 < len(sentences) and (re.match(r'\b[A-Z]', sentences[i + 1].lstrip()) or re.match(r'\b(?:|CSC\.)\s*$', sentences[i + 1].lstrip())):
                    # Combine into one sentence
                    sentences[i] += ' ' + sentences[i + 1]
                    del sentences[i + 1]
                else:
                    # Otherwise, move to the next sentence
                    i += 1

            # If the token is an abbreviation like mil., mld., tis., expecting a lowercase letter or name after it
            elif re.match(r'\b(?:|mil\.|mld\.|tis\.)\s*$', sentences[i].split()[-1]):
                # If the next token is a lowercase letter or name
                if i + 1 < len(sentences) and (re.match(r'\b[a-z]', sentences[i + 1].lstrip()) or re.match(r'\b(?:|sk\.|czk\.|Sk\.|Czk\.|SK\.|CZK\.)\s*$', sentences[i + 1].lstrip())):
                    # Combine into one sentence
                    sentences[i] += ' ' + sentences[i + 1]
                    del sentences[i + 1]
                else:
                    # Otherwise, move to the next sentence
                    i += 1

            # If the token is an abbreviation like MIL., MLD., TIS., expecting an uppercase letter or name after it
            elif re.match(r'\b(?:|MIL\.|MLD\.|TIS\.)\s*$', sentences[i].split()[-1]):
                # If the next token is an uppercase letter or name
                if i + 1 < len(sentences) and (re.match(r'\b[A-Z]', sentences[i + 1].lstrip()) or re.match(r'\b(?:|SK\.|CZK\.)\s*$', sentences[i + 1].lstrip())):
                    # Combine into one sentence
                    sentences[i] += ' ' + sentences[i + 1]
                    del sentences[i + 1]
                else:
                    # Otherwise, move to the next sentence
                    i += 1

            # If the token is a name
            elif re.match(r'\b(?:|sk\.|czk\.|Sk\.|Czk\.|SK\.|CZK\.)\s*$', sentences[i].split()[-1]):
                if i + 1 < len(sentences) and (re.match(r'\b[a-z]', sentences[i + 1].lstrip())):
                    # Combine the current sentence with the next one
                    sentences[i] += ' ' + sentences[i + 1]
                    del sentences[i + 1]
                else:
                    # Move to the next sentence
                    i += 1 

            # If the token is a name
            elif re.match(r'\b(?:|SK\.|CZK\.)\s*$', sentences[i].split()[-1]):
                if i + 1 < len(sentences) and (re.match(r'\b[A-Z]', sentences[i + 1].lstrip())):
                    # Combine the current sentence with the next one
                    sentences[i] += ' ' + sentences[i + 1]
                    del sentences[i + 1]
                else:
                    # Move to the next sentence
                    i += 1

            # If the token is an abbreviation
            elif re.match(r'\b(?:|atď\.|kol\.|pod\.|i\.|cit\.|č\.|comp\.|p\.|pp\.|pnl\.|n\.l\.|tj\.|tzv\.|vol\.|vyd\.|zodp\.|red\.|j\.|a\.|s\.|t\.)\s*$', sentences[i].split()[-1]):
                if i + 1 < len(sentences) and (re.match(r'\b[a-z]|[0-9]', sentences[i + 1].lstrip())):
                    # Combine the current sentence with the next one
                    sentences[i] += ' ' + sentences[i + 1]
                    del sentences[i + 1]
                else:
                    # Move to the next sentence
                    i += 1    

            # If the token is an abbreviation
            elif re.match(r'\b(?:|ATĎ\.|KOL\.|POD\.|I\.|CIT\.|Č\.|COMP\.|P\.|PP\.|PNL\.|N\.L\.|TJ\.|TZV\.|VOL\.|VYD\.|ZODP\.|RED\.|J\.|A\.|S\.|T\.)\s*$', sentences[i].split()[-1]):
                if i + 1 < len(sentences) and (re.match(r'\b[A-Z]|[0-9]', sentences[i + 1].lstrip())):
                    # Combine the current sentence with the next one
                    sentences[i] += ' ' + sentences[i + 1]
                    del sentences[i + 1]
                else:
                    # Move to the next sentence
                    i += 1    

            elif re.match(r'\d+\.?$', sentences[i].split()[-1]):
                # Check if the next sentence starts with a lowercase letter or is another abbreviation
                if i + 1 < len(sentences) and (re.match(r'\b[a-z]|[0-9]', sentences[i + 1].lstrip()) or re.match(r'\b(?:|mr\.|mrs\.|ms\.|dr\.|doc\.|rndr\.|mudr\.|paeddr\.|judr\.|phdr\.|ing\.|mgr\.|rcdr\.|rsdr\.|MR\.|MRS\.|MS\.|DR\.|DOC\.|RNDR\.|MUDR\.|PAEDDR\.|JUDR\.|PHDR\.|ING\.|MGR\.|RCDR\.|RSDR\.|Mr\.|Mrs\.|Ms\.|Dr\.|Doc\.|RNDr\.|MUDr\.|PaedDr\.|JUDr\.|PhDr\.|Ing\.|Mgr\.|RcDr\.|RsDr\.|Csc\.|csc\.|CSC\.|PhD\.|phd\.|PHD\.|atď\.|kol\.|mil\.|sk\.|czk\.|mld\.|tis\.|pod\.|i\.|cit\.|č\.|comp\.|p\.|pp\.|pnl\.|n\.l\.|tj\.|tzv\.|vol\.|vyd\.|zodp\.|red\.|j\.|a\.|s\.|t\.|ATĎ\.|KOL\.|MIL\.|SK\.|CZK\.|MLD\.|TIS\.|POD\.|I\.|CIT\.|Č\.|COMP\.|P\.|PP\.|PNL\.|N\.L\.|TJ\.|TZV\.|VOL\.|VYD\.|ZODP\.|RED\.|J\.)\b', sentences[i + 1].lstrip())):
                    # Combine the current sentence with the next one
                    sentences[i] += ' ' + sentences[i + 1]
                    del sentences[i + 1]
                elif i + 1 < len(sentences) and (re.match(r'\.\s*$', sentences[i].split()[-1]) and re.match(r'\b[a-z]', sentences[i + 1].lstrip())):
                    # Combine the current sentence with the next one
                    sentences[i] += ' ' + sentences[i + 1]
                    del sentences[i + 1]
                else:
                    # Move to the next sentence
                    i += 1

            else:
                # Move to the next sentence
                i += 1

        return sentences

