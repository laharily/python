def computeMongoAge(birthYear, birthMonth, birthDay, currentYear, currentMonth, currentDay):
    """input --> int
    Finds the age of someone in Mongo"""
    birthMonth *= 26
    birthYear *= 390
    currentMonth *= 26
    currentYear *= 390
    birth = birthYear + birthMonth + birthDay
    current = currentYear + currentMonth + currentDay
    age = current-birth
    return age/390

print(computeMongoAge(2879,8,11,2892,2,21))
