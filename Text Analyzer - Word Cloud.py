import os
import sys
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer

ps = PorterStemmer()

looper = 0

# os change directory
dir_path = "--DIRECTORY REDACTED FOR PRIVACY--"
print(os.getcwd())


while looper == 0:
    while dir_path == "--DIRECTORY REDACTED FOR PRIVACY--":
        folder_input = input("Enter folder name (type 'exit' to close window): ")
        dir_path = dir_path+folder_input
    if folder_input.lower() == "exit":
        exit()
        sys.exit()
    try:    
        os.chdir(dir_path)
        looper = 1
    except FileNotFoundError:
        print("Folder not found...")
        dir_path = "--DIRECTORY REDACTED FOR PRIVACY--"

print("\nAnalyzing files in: "+os.getcwd())

stop_words = stopwords.words('english')
add_stops = ["towards", "need", "work", "achieve", "effectively", "skills", "strong", "effective", "excellent", "good", "knowledge", "experience", "proficiency", "proficient", "ability", "demonstrates", "demonstrated", "solid", "and/or", "exceptional", "understanding", "expert", "desir"]
stop_words = set(stop_words+add_stops)
stem_stops = []

for i in stop_words:
    stem_stops.append(ps.stem(i))
stem_stops = set(stem_stops)

full_dict = dict()
valid_files = ['.doc', '.docx', '.txt']
# open files and analyze text

for filename in os.listdir(os.getcwd()):
    if filename[filename.index("."):] in valid_files:
#        print("\nAnalyzing text in:          "+filename)
        f = open(filename, "r+")
        a_list = []
        del_punc = ['.', ',', '?', '!', ';', ':', '(', ')', '[', ']', "•"]
        
        # pre-processing ---
        
        for line in f:
            line = line.replace("-", " ")
            line = line.replace("/", " ")
            line_split = line.split()
            for i in line_split:
                for j in del_punc:
                    i = i.replace(j, "")
                if i.isdigit() == 0:
                    a_list.append(i.lower())
                    
        for i in a_list:
            if i.strip() == "•":
                a_list.remove(i)
            if i in stop_words:
                a_list.remove(i)


        while("" in a_list):
            a_list.remove("")
            
                    
        # remove stop words
        filtered = []
        stem_list = []
                        
        for word in a_list:
            word = ps.stem(word)
            stem_list.append(word)
            
        for i in stem_list:
            if i not in stem_stops:
                filtered.append(i)
        
        
        bigrm = list(nltk.bigrams(filtered))
        
        for i in bigrm:
            if i[0] or i[-1] == "•":
                bigram = bigrm.remove(i)
        
        for i in bigrm:
                i = ' '.join(i)
                filtered.append(i)
                        
#        # create list of words with counts for file
#        word_count = dict()
#        
#        for word in filtered:
#            if word in word_count:
#                word_count[word] += 1
#            else:
#                word_count[word] = 1 
#        for w in sorted(word_count, key=word_count.get, reverse=True):
#            print(w, word_count[w])
       
        # append to full list of words for all files
        for word in filtered:
            if word in full_dict:
               full_dict[word] += 1
            else:
                full_dict[word] = 1    
        f.close()
    
    else:
        pass
    
#print full list of words with counts
print("\n-------Full List: \n")
for w in sorted(full_dict, key=full_dict.get, reverse=True):
    print(w, full_dict[w])           


from wordcloud import WordCloud
import matplotlib.pyplot as plt


wordcloud = WordCloud(width=1600, height=800).generate(', '.join(filtered))
plt.figure(figsize=(20,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

wordcloud = WordCloud(background_color="white", width=1600, height=800).generate(', '.join(filtered))
plt.figure(figsize=(20,10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

input("\nProcess complete; Press Enter to close application...")