score1 = float(input("Enter your score 1: "))
credits1 = int(input("Enter credits for score 1: "))

score2 = float(input("Enter your score 2: "))
credits2 = int(input("Enter credits for score 2: "))

average = (score1 * credits1 + score2 * credits2) / (credits1 + credits2)
print(average)

result = "excellent" if average >= 17 else "accepted" if average >= 12 else "not accepted"
print(result)
