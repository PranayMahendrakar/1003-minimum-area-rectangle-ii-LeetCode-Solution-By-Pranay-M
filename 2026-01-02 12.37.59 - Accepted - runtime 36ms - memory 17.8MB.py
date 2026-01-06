class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        from collections import defaultdict
        import math
        
        n = len(points)
        if n < 4:
            return 0
        
        point_set = set(map(tuple, points))
        
        # Group pairs by (midpoint, diagonal length squared)
        diagonals = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                # Midpoint (use 2x to avoid float)
                mid = (x1 + x2, y1 + y2)
                # Diagonal length squared
                dist_sq = (x2 - x1) ** 2 + (y2 - y1) ** 2
                diagonals[(mid, dist_sq)].append((i, j))
        
        min_area = float('inf')
        
        for pairs in diagonals.values():
            for k in range(len(pairs)):
                for l in range(k + 1, len(pairs)):
                    i1, j1 = pairs[k]
                    i2, j2 = pairs[l]
                    
                    p1 = points[i1]
                    p2 = points[j1]
                    p3 = points[i2]
                    
                    # Vectors from p1 to p2 and p1 to p3
                    v1 = (p3[0] - p1[0], p3[1] - p1[1])
                    v2 = (p2[0] - p1[0], p2[1] - p1[1])
                    
                    # Area = |v1 x v2|
                    area = abs(v1[0] * v2[1] - v1[1] * v2[0])
                    if area > 0:
                        min_area = min(min_area, area)
        
        return min_area if min_area != float('inf') else 0