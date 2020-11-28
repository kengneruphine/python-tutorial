prices = [1, 12, 5 ,111 ,200, 1000, 10]

k = 50 #amount to spend


def maximumToys(prices, k):
    count = 0
    total = 0 
    prices = sorted(prices)
    for i in range(len(prices)):
        total += prices[i]
        if total < k:
            count += 1
        else:
            break
            
    return count
        

print('Number of toys bought is {}'.format(maximumToys(prices, k)))

