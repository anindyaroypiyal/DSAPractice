def median(a: int, b: int) -> float:
    # Write the function here.
    n = a + b
    x = sorted(n)

    if len(n) % 2 != 0:
        ans = (len(n) - 1) // 2
        return (float(x[ans])) 
    else:
        ans = len(n) // 2
        l = (x[ans] + x[ans-1]) / 2 
        return (float(l)) 