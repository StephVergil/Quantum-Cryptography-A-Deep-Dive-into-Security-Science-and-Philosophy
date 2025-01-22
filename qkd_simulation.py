import numpy as np  # Importing the NumPy library for numerical operations
from random import choice  # Importing choice function to select random elements

def generate_bits(n):
    """
    Generate a sequence of random bits (0s and 1s) of length n.

    Parameters:
    n (int): Number of bits to generate.

    Returns:
    numpy.ndarray: Array of randomly generated bits.
    """
    return np.random.randint(2, size=n)  # Generate an array of 0s and 1s

def random_bases(n):
    """
    Generate a sequence of random measurement bases ('+' or 'x') of length n.

    Parameters:
    n (int): Number of bases to generate.

    Returns:
    list: List of randomly chosen bases.
    """
    return np.random.choice(['+', 'x'], size=n)  # Select random bases from '+' and 'x'

def encode_qubits(bits, bases):
    """
    Encode qubits based on the chosen bases.

    If the base is '+', the qubit remains the same as the bit.
    If the base is 'x', the qubit is flipped (0 to 1, 1 to 0).

    Parameters:
    bits (numpy.ndarray): Array of bits to encode.
    bases (list): List of bases used for encoding.

    Returns:
    list: Encoded qubits based on the bases.
    """
    return [bit if base == '+' else (1 - bit) for bit, base in zip(bits, bases)]

# Number of bits to be transmitted
n = 10

# Step 1: Alice generates a random sequence of bits
alice_bits = generate_bits(n)
print("Alice's bits:", alice_bits.tolist())  # Convert to standard Python list for clean output

# Step 2: Alice randomly selects measurement bases
alice_bases = random_bases(n)
print("Alice's bases:", alice_bases.tolist())

# Step 3: Encode qubits using the chosen bases
alice_qubits = encode_qubits(alice_bits, alice_bases)
print("Alice's encoded qubits:", [int(q) for q in alice_qubits])  # Convert to standard integers

# Step 4: Bob randomly selects measurement bases
bob_bases = random_bases(n)
print("Bob's bases:", bob_bases.tolist())

# Step 5: Bob measures qubits (assumption: same encoding process)
bob_qubits = encode_qubits(alice_bits, bob_bases)
print("Bob's measured qubits:", [int(q) for q in bob_qubits])  # Convert to standard integers

# Step 6: Alice and Bob compare bases to keep matching ones
matching_indices = [i for i in range(n) if alice_bases[i] == bob_bases[i]]
final_key = [alice_bits[i] for i in matching_indices]
print("Final secret key:", [int(k) for k in final_key])  # Convert to standard integers

