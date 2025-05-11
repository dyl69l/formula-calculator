def velocity():
    c = 299792458  # Speed of light

    u_input = input("Enter U (in m/s): ").lower()
    v_input = input("Enter V (in m/s): ").lower()

    if "c" in u_input:
        u = float(u_input.replace("c", "")) * c
    else:
        u = float(u_input)

    if "c" in v_input:
        v = float(v_input.replace("c", "")) * c
    else:
        v = float(v_input)


    u_prime = (u + v) / (1 + (u * v) / c**2)

    if u_prime >= c:
        print("It is impossible")
    else:
        print(f"Resulting velocity: {u_prime:.4f} m/s")
        print(f"As a fraction of the speed of light: {u_prime / c:.8f} c")

velocity()
