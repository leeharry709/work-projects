# work-projects
Projects made for work. Due to the confidentiality of the work, I am unable to provide any further media other than the code.

# Skills Compiler.py
This program would comb though the job descriptions folder and further into each department's folder and look for Word documents to parse though. It would grab the "Job Duties and Responsibilities" and "Knowledge, Skills, and Abilites" and output them into a "text_dumpster.txt" file. It would continue to go through every deparment's folder until it reached the end of the job descriptions directory.

# Text Analyzer.py
This program would retrieve the text_dumpster.txt files in the selected department's job description folder and begin to process it. The program would first remove punctuations and then stop words. Then, it would create a list of the remaining words. Using NLTK, it would then make a list of the bigrams as well. Combining the two lists together, it would create a dictionary based on the frequency of each word and bigram and display it on a wordcloud.
