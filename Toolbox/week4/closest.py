import math

def minimum_distance(points):
    def get_distance(point1, point2):
        d = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
        return d

    def brute_force(points):
        n = len(points)
        d = get_distance(points[0], points[1])
        for i in range(n - 1):
            for j in range(i + 1, n):
                d = min(d, get_distance(points[i], points[j]))
        return d

    def strip_min(points_x_sorted, min_d):
        len_p = len(points_x_sorted)
        mid = len_p // 2
        mid_value = points_x_sorted[mid][0]
        points_y_sorted = [point for point in points_x_sorted if abs(point[0] - mid_value) < min_d]
        points_y_sorted.sort(key=lambda p: p[1])
        len_strip = len(points_y_sorted)
        if len_strip < 2:
            return min_d
        else:
            min_d2 = get_distance(points_y_sorted[0], points_y_sorted[1])
            for i in range(len_strip - 1):
                for j in range(i + 1, min(i + 7, len_strip)):
                    min_d2 = min(min_d2, get_distance(points_y_sorted[i], points_y_sorted[j]))
            return min_d2

    def min_distance_recursive(points_x_sorted):
        len_p = len(points_x_sorted)
        if len_p <= 3:
            return brute_force(points_x_sorted)
        else:
            mid = len_p // 2
            min_d_l = min_distance_recursive(points_x_sorted[:mid])
            min_d_r = min_distance_recursive(points_x_sorted[mid:])
            min_d = min(min_d_l, min_d_r)
            min_d2 = strip_min(points_x_sorted, min_d)
            return min(min_d, min_d2)

    points_x_sorted = sorted(points)
    result = min_distance_recursive(points_x_sorted)
    return result

if __name__ == '__main__':
    n = int(input())
    points = []
    for i in range(n):
        ipt = input()
        coordinate = tuple(map(int, ipt.split()))
        points.append(coordinate)
    
    result = minimum_distance(points)
    print("{0:.9f}".format(result))
