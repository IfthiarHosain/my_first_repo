import re
pattern=r"[A-Z]+ormat"
text='''
Format
Academic Reading: Three long passages from books, journals, or articles, with 40 questions.
General Training Reading: Extracts from notices, advertisements, handbooks, and other everyday materials.
Preparation Tips
Develop Skimming and Scanning Skills:
Skim for main ideas and scan for specific information.
Understand Question Types:
True/False/Not Given, Matching Headings, Multiple Choice, Sentence Completion, etc.
Expand Your Reading:
Read newspapers, magazines, and academic texts to build vocabulary and speed.
Time Management:
Spend about 20 minutes per section.
Practice Paraphrasing:
Learn to recognize synonyms and rephrased ideas in the text.
'''
#match= re.search(pattern,text)
matches=re.finditer(pattern,text)
for match in matches:
    print(match.span())