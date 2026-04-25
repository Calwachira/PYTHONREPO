
def evaluate_temp(temp):
    message ="Normal temperature"
    if temp < 38:
        message ="Normal temperature !"
    if temp<=39:
        message ="slightly elevated temperature"
    elif temp >= 40:
         message ="Fever ! seek medical attention"
    return message

print(evaluate_temp(39))
print(evaluate_temp(34))
print(evaluate_temp(40))