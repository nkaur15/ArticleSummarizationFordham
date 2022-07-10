'''Data Preprocessing (cleaning up the csv file, tokenizing will be done in the
summarizer model)
'''
import pandas as pd
import numpy as np
import csv

file = "scraped_articles.csv"
df = pd.read_csv(file)

#separate contents of first column (source and text should be separated)
source_text = df["|Source|Text"]

listOfText = []
listOfSources = []
listOfArticleNums = []

for line in df.index:

    #split the words in the first column from Source and Text, start new csv file
    # keeping records of these values
    if (source_text[line] != "nan" and pd.isnull(source_text[line]) == False):
        split_at = str(source_text[line]).split("|")
    article_numbers = split_at[0]
    source = split_at[1]

    listOfSources.append(source)
    listOfArticleNums.append(article_numbers)

    #finding the number of columns with data for each row
    columns = len(df.columns)

    #combining all the text into one column
    #store all text in each row in a list
    text_vals = []
    text_start = split_at[2]
    text_vals.append(text_start)

    for i in range(1,columns):
        text_vals.append(df.iloc[line][i])

    text_vals = [i for i in text_vals if pd.isnull(i) == False and i != "nan"]

    #convert to single string
    complete_text = "".join(text_vals)

    #append to initial text list to insert into new_df
    listOfText.append(complete_text)

#new csv file to hold values
fields = ["Article_num","Source","Text"]
new_df = "article_data.csv"

data = []
for i in range(len(listOfArticleNums)):
    values = []
    values.append(listOfArticleNums[i])
    values.append(listOfSources[i])
    values.append(listOfText[i])
    data.append(values)

with open(new_df,"w",encoding="utf-8",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    writer.writerows(data)

#getting rid of duplicates
df =df.drop_duplicates(subset="Text",keep="first")
df.to_csv(file)

#remove tabs from text
for i in range(len(df["Text"])):
    string_text = df["Text"][i]
    re.sub("\s+"," ",string_text)

list_special=[]
#gets rid of nonenglish rows a
for i in range(len(df["Text"])):
    #print("works at" + str(i))
    text_check = df["Text"][i]

    if not (text_check.isascii()):
        df.drop(labels=i,axis=0,inplace=False)

    df["len_text"][i] = len(df["Text"][i])

    """getting rid of weird chars by counting normal amount of punctuation in each
    text and removing the rows that have more than the average"""
    special_chars = 0
    print(text_check)
    for j in range(len(text_check)):
        #if (text_check[j].isalpha()):
         #   continue
        if ((text_check[j]>="a" and text_check[j]<="z")or(text_check[j]>="A" and text_check[j]<="Z")):
            continue
        elif (text_check[j].isdigit()):
            continue
        elif (text_check[j] == " "):
            continue
        elif (text_check[j] == "."):
            continue
        elif (text_check[j] == ","):
            continue
        elif (text_check[j] == "'"):
            continue
        else:
            special_chars += 1
    print(len(text_check))
    print(special_chars)
    list_special.append(special_chars)
    df["num_spec_chars"][i] = special_chars


    #if more than 40% of the chars in the list are special remove from list
df = df.loc[0.4*df["len_text"] > df["num_spec_chars"]]
df.to_csv(file)
print(df)
