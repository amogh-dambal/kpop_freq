# KPOP  Analysis

This project aims to apply NLP techniques used to analyze text to the world of popular music, specifically in the Korean language. 

Version 1.0: aims to identify the top-n phrases and words used by the most popular Korean pop songs at any given time.
The first iteration of the project was instantiated in July 2019, and the dataset consisted of the lyrics of the Top 100 most viewed Korean popular songs on YouTube. 

# Methodology

The project used web scraping technology to grab the lyrics and convert them into text files. The data sanitization process included removing all non-essential text, such as verse identifiers and non-Korean words. Furthermore, NLP preprocessing included tokenizing the text and removing stopwords and non-needed tokens such as punctuation. 

The NLP performed included performing basic counting of tokens and a frequency distribution of the top-N tokens. The N for the project was chosen at random (n=40), and the results should be posted below. 

# Results

# Upcoming

The later versions of this project aim to implement more features of NLP analysis such as part-of-speech tagging, stemming and lemmatization, and several forms of analysis such as LSA (latent semantic analysis) and LDA (latent dirichlet allocation). In the future, we hope to build a system that may be capable of automatically generating lyrics to songs in Korean based on the data we collect and analyze here.

We hope to understand the patterns and structures of music that tends to be popular to identify the particular features of any given track that are the cause of its popularity. This project could serve as a guide to differentiate songs based on popularity.

# Contact
All questions, suggestions, code reviews, and feature suggestions are welcome! Please contact me at the following email: amoghdambal@utexas.edu 

# Disclaimer

This project is not the work of professional developers. The team behind this project consists of students, attempting to learn and polish their CS skills, especially in the area of NLP. Mistakes will be made accordingly, and we ask for any and all polite and helpful corrections so we can improve more quickly and provide more accurate, up-to-date, and more powerful analysis. Thank you :)
