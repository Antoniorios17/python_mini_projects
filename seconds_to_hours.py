# this function can convert seconds to hours and the minutes and seconds leftover

def convert_seconds(seconds):
    hours = seconds //3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours , minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours ,"hour(s)", minutes , "minute(s)", seconds, "second(s)")