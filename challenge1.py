
def evaluate_user_premium(age, driving_violations, vehicle_risk, driving_experience):
    reasons = []

    if age < 25:
        reasons.append("Under 25")

    if driving_violations:
        reasons.append("Has driving violations")

    if vehicle_risk:
        reasons.append("Owns high risk vehicle")
    
    if reasons:
    
        return "Premium: High-risk", ", ".join(reasons)

    if not driving_violations and not vehicle_risk and driving_experience >= 5:
        return "Premium: Standard"
    
    else:
        return "Premium: Review required", "Complex Case- Further review required."


try:
    age = int(input("Enter your age: "))

    driving_violations = input("Any driving violations (Yes or No)? ").strip().lower() == 'yes'

    vehicle_risk = input("Do you own a high-risk vehicle (Yes or No)? ").strip().lower() == 'yes'
    driving_experience = int(input("Enter years of driving experience: "))

    category, reason = evaluate_user_premium(age, driving_violations, vehicle_risk, driving_experience)
    print(category)
    print("Reason: ", reason)
except:
    print("Invalid input. Enter integers for age and driving experience!")
    

