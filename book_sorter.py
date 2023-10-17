import pandas as pd
import numpy

file_path = "books.csv"
data_dataframe = pd.read_csv(file_path)
data = data_dataframe.to_numpy()

def sort_title(data):
    size = len(data)
    for j in range(size - 1):
        for i in range(size - 1):
            first_title = data[i][0]
            second_title = data[i+1][0]
            if ord(second_title[0]) < ord(first_title[0]):

                temp = data[i][0]
                data[i][0] = data[i+1][0]
                data[i+1][0] = temp

                temp = data[i][1]
                data[i][1] = data[i+1][1]
                data[i+1][1] = temp

                temp = data[i][2]
                data[i][2] = data[i+1][2]
                data[i+1][2] = temp

    return data

def sort_author(data):
    size = len(data)
    for j in range(size - 1):
        for i in range(size - 1):
            first_title = data[i][1]
            second_title = data[i+1][1]
            if ord(second_title[0]) < ord(first_title[0]):

                temp = data[i][0]
                data[i][0] = data[i+1][0]
                data[i+1][0] = temp

                temp = data[i][1]
                data[i][1] = data[i+1][1]
                data[i+1][1] = temp

                temp = data[i][2]
                data[i][2] = data[i+1][2]
                data[i+1][2] = temp

    return data

def sort_date(data):
    size = len(data)
    for j in range(size - 1):
        for i in range(size - 1):
            first_title = data[i][2]
            second_title = data[i+1][2]
            if second_title < first_title:
                
                temp = data[i][0]
                data[i][0] = data[i+1][0]
                data[i+1][0] = temp

                temp = data[i][1]
                data[i][1] = data[i+1][1]
                data[i+1][1] = temp

                temp = data[i][2]
                data[i][2] = data[i+1][2]
                data[i+1][2] = temp

    return data

print("press 1 to sort books for title")
print("press 2 to sort books for author")
print("press 3 to sort books for date")
choice_type = int(input())
print("press 1 to sort books ascendingly (A-Z, 1-9)")
print("press 2 to sort books decendingly (Z-A, 9-1)")
choice_order = int(input())
print("################################################")

if choice_type == 1 and choice_order == 1:
        result = sort_title(data)
        result =pd.DataFrame(result)
        result.to_csv("books_sorted.csv", index = False)

if choice_type == 1 and choice_order == 2:
        result = sort_title(data)
        reversed_result = numpy.flip(result, axis=0)
        reversed_dataframe = pd.DataFrame(reversed_result)
        reversed_dataframe.to_csv("books_sorted.csv", index=False)

if choice_type == 2 and  choice_order == 1:
        result = sort_author(data)
        result =pd.DataFrame(result)
        result.to_csv("books_sorted.csv", index = False)

if choice_type == 2 and choice_order == 2:
        result = sort_author(data)
        reversed_result = numpy.flip(result, axis=0)
        reversed_dataframe = pd.DataFrame(reversed_result)
        reversed_dataframe.to_csv("books_sorted.csv", index=False)

if choice_type == 3 and choice_order == 1:
        result = sort_date(data)
        result =pd.DataFrame(result)
        result.to_csv("books_sorted.csv", index = False)

if choice_type == 3 and choice_order == 2:
        result = sort_date(data)
        reversed_result = numpy.flip(result, axis=0)
        reversed_dataframe = pd.DataFrame(reversed_result)
        reversed_dataframe.to_csv("books_sorted.csv", index=False)
