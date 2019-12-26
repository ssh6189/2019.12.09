score = [38, 65, 89, 16, 95, 71, 63, 48, 49, 66, 47]

i = 0

while i < len(score):
    if score[i] >= 95:
        print(score[i], "A+")
    else:
        print(score[i], "F")

    i = i + 1

str(input())
