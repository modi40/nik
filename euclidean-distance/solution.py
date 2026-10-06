import math

def calculate_euclidean_distance(point1, point2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

def main():
    p1 = [2, 3, 4]
    p2 = [5, 7, 6]
    
    distance = calculate_euclidean_distance(p1, p2)
    
    print(f'Data Point  : {p1}')
    print(f'Data Point : {p2}')
    print(f'Euclidean Distance  = {distance:.3f}')

if __name__ == '__main__':
    main()
