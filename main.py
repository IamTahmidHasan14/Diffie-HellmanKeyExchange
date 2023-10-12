def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primitive_root(p):
    if not is_prime(p):
        return None
    for alpha in range(2, p):
        powers = set()
        for j in range(1, p):
            powers.add(pow(alpha, j, p))
        if len(powers) == p - 1:
            return alpha
    return None

def compute_public_key(alpha, x, q):
    return pow(alpha, x, q)

def compute_shared_key(public_key, x, q):
    return pow(public_key, x, q)

q = int(input("Enter a prime number (q): "))
if not is_prime(q):
    print("Invalid input. Please enter a prime number.")
else:
    alpha = find_primitive_root(q)
    if alpha is None:
        print("No primitive root found for the given prime.")
    else:
        print("Primitive root (alpha):", alpha)
        xA = int(input("Enter secret key for A (less than q): "))
        xB = int(input("Enter secret key for B (less than q): "))
        if xA >= q or xB >= q:
            print("Invalid secret keys. They should be less than q.")
        else:
            yA = compute_public_key(alpha, xA, q)
            yB = compute_public_key(alpha, xB, q)
            
            Kab_A = compute_shared_key(yB, xA, q)
            Kab_B = compute_shared_key(yA, xB, q)
            
            print("Public key for A (yA):", yA)
            print("Public key for B (yB):", yB)
            print("Shared session key (KAB) computed by A:", Kab_A)
            print("Shared session key (KAB) computed by B:", Kab_B)
