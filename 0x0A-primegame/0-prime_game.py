def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False

        # Sieve of Eratosthenes to mark non-prime numbers
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1

        # Simulate the game rounds
        maria_turn = True
        while True:
            # Find the next available prime number
            prime_num = None
            for i in range(2, n + 1):
                if primes[i]:
                    prime_num = i
                    break

            if prime_num is None:
                # No prime number left, the current player loses
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            # Remove the prime number and its multiples
            for i in range(prime_num, n + 1, prime_num):
                primes[i] = False

            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
