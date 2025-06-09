# life in weeks
def life_in_weeks(current_age):
    years_left = 60 - current_age
    print(f"You have {years_left * 52} weeks left.")
    
    

# Love score calculator
def calculate_love_score(name1, name2):
    combined_name = name1 + name2
    metric1 = "true"
    metric2 = "love"
    score1 = 0
    score2 = 0
    for i in range(len(metric1)):
        score1 += combined_name.lower().count(metric1[i])
        
    for i in range(len(metric2)):
        score2 += combined_name.lower().count(metric2[i])
    print(str(score1) + "" + str(score2))

# life_in_weeks(30)
calculate_love_score("Romeo", 'juliet')