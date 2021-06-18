def solution(numbers, hand):
    answer = ''
    tmp_r = '#'
    tmp_l = '*'
    for n in numbers:
        if n in [3, 6, 9]: #right
            answer += 'R'
            tmp_r = n
        elif n in [1, 4, 7]: #left
            answer += 'L'
            tmp_l = n
        elif n in [2, 5, 8, 0]: #middle
            d_r = distance(tmp_r, n)
            d_l = distance(tmp_l, n)
            if d_r > d_l:
                answer += 'L'
                tmp_l = n
            elif d_r < d_l:
                answer += 'R'
                tmp_r = n
            elif d_r == d_l:
                if hand == 'right':
                    answer += 'R'
                    tmp_r = n
                else:
                    answer += 'L'
                    tmp_l = n
    return answer

def distance(hand, number):
    location = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
                '4': (1, 0), '5': (1, 1), '6': (1, 2),
                '7': (2, 0), '8': (2, 1), '9': (2, 2),
                '*': (3, 0), '0': (3, 1), '#': (3, 2)}
    hand = str(hand)
    number = str(number)
    x_h, y_h = location[hand]
    x_n, y_n = location[number]
    return abs(x_h - x_n) + abs(y_h - y_n)