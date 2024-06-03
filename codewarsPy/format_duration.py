def format_duration(seconds):
    if seconds == 0:
        return "now"
    
    intervals = (
        ('years', 31536000),
        ('days', 86400),
        ('hours', 3600),
        ('minutes', 60),
        ('seconds', 1),
    )
    
    result = []
    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                result.append(f"{value} {name[:-1]}")
            else:
                result.append(f"{value} {name}")
    
    return ', '.join(result[:-1]) + ' and ' + result[-1] if len(result) > 1 else result[0]

print(format_duration(215536000))
