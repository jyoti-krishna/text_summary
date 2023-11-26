import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
text="""Time is all relative based on age and experience. When you are a child an hour is a long time to wait but a very short time when that’s all the time you are allowed on your iPad. As a teenager time goes faster the more deadlines you have and the more you procrastinate. As a young adult, you think you have forever to live and don’t appreciate the time you spend with others. As a middle-aged adult, time flies by as you watch your children grow up. And finally, as you get old and you have fewer responsibilities and fewer demands on you, time slows. You appreciate each day and are thankful you are alive. An hour is the same amount of time for everyone yet it can feel so different in how it goes by.
"""
def summarizer(text):
    stopwords=list(STOP_WORDS)
    nlp=spacy.load('en_core_web_sm')
    doc=nlp(text)
    tokens=[token.text for token in doc]
    word_freq={}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text]=1
            else:
                word_freq[word.text]+=1
    max_freq=max(word_freq.values())
    for word in word_freq.keys():
        word_freq[word]/=max_freq
    sent_tokens=[sent for sent in doc.sents]
    sent_scores={}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent]=word_freq[word.text]
                else:
                    sent_scores[sent]+=word_freq[word.text]

    select_len=int(len(sent_tokens)*0.25)
    summary=nlargest(select_len,sent_scores,key=sent_scores.get)
    final_summary=[word.text for word in summary]
    summary=' '.join(final_summary)
    return summary, doc , len(summary.split(' ')), len(text.split(' '))

        