import spacy
nlp = spacy.load('en_core_web_md')

# Create a function for measuring the similarity between words
def word_similarity (word1, word2):
        nlp_word1 = nlp(word1)
        nlp_word2 = nlp(word2)
        return nlp_word1.similarity(nlp_word2)

# Similarity between individual words
cat_monkey = word_similarity ("cat", "monkey")
print(f"""The similarity between cat and monkey is {cat_monkey} which is 
      medium similarity and based on both being animals.""")

monkey_banana = word_similarity ("monkey", "banana")
print(f"""The similarity between monkey and banana is {monkey_banana} 
      which is a low similarity based on monkeys eating bananas.""")

cat_banana = word_similarity ("cat", "banana")
print(f"""The similarity between cat and banana is {cat_banana} which is 
      a very low similarity with no clear link between the two.""")

# Create an example of your own for individual words
table_bed = word_similarity ("table", "bed")
print(f"""The similarity between table and bed is {table_bed} which is 
      low similarity and only based on both being pieces of furniture.""")

bed_eating = word_similarity ("bed", "eating")
print(f"""The similarity between bed and eating is {bed_eating} which is 
      a very low similarity only due to a low link of eating in bed.""")

table_eating = word_similarity ("table", "eating")
print(f"""The similarity between table and eating is {table_eating} which 
      is medium similarity as you would often eat on a table.""")


# Similarity in words with vectors
tokens = nlp('cat apple monkey banana')

for token1 in tokens:
        for token2 in tokens:
            print(token1.text, token2.text, token1.similarity(token2))


# Similarity with sentences
sentence_to_compare = "Why is my cat on the car"

sentences = [
        "where did my dog go",
        "Hello, there is my car",
        "I\'ve lost my car in my car",
        "I\'d like my boat back",
        "I will name my dog Diana"
        ]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
        similarity = nlp(sentence).similarity(model_sentence)
        print(f"""'{sentence}': Similarity to '{sentence_to_compare}' is 
              {similarity}""")


# Run this code on the en_core_web_sm language model and note difference
print("""When you compare the similarity on the en_core_web_sm language 
      model compared to the md model there is a warning message to say 
      that the model has no word vectors loaded and it may not give 
      useful similarity judgements. We note that the values given in the 
      sm model tend to be in general higher, e.g. cat and monkey is 0.68 
      (vs 0.59 in md), monkey and banana is 0.72 vs 0.40 in md) and cat 
      and banana is 0.68 (vs 0.22 in md)""")
