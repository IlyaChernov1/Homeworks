
def main(word):
    length = len(word)
    
    if length % 2 == 1:
        middle_index = length // 2
        return word[middle_index]
    else:
        middle_index1 = (length // 2) - 1
        middle_index2 = length // 2
        return word[middle_index1:middle_index2 + 1]




word = input("Введите слово из латинских букв: ")
middle_letters = main(word)
print("Средние буквы:", middle_letters)