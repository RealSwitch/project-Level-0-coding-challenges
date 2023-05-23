def integer_to_time(integer):
    hours = integer//60
    minutes = integer%60
    string_minutes = str(minutes) 
    string_hours = str(hours)
    if hours !=  1:
        if minutes != 1:
            return string_hours + " hours, " + string_minutes + " minutes"
        else:
            return str(hours) + " hours, " + string_minutes + " minute"
    else:
        if minutes != 1:
            return string_hours + " hour, " + string_minutes + " minutes"
        else:
            return string_hours + "hour, " + string_minutes + " minute"
        

if __name__ == "__main__":
    print(integer_to_time(133))
    print(integer_to_time(71))
