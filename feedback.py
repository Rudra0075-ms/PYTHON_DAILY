feedback = input("Enter customer feedback: ")

words = feedback.lower().split()

positive = ["good", "excellent", "nice", "happy"]
negative = ["bad", "poor", "slow", "worst"]

positive_count = 0
negative_count = 0

for word in words:
    if word in positive:
        positive_count += 1
    elif word in negative:
        negative_count += 1

print("Total words:", len(words))
print("Total characters:", len(feedback))
print("Positive words:", positive_count)
print("Negative words:", negative_count)

if positive_count > negative_count:
    print("Overall Feedback: Positive")
elif negative_count > positive_count:
    print("Overall Feedback: Negative")
else:
    print("Overall Feedback: Neutral")