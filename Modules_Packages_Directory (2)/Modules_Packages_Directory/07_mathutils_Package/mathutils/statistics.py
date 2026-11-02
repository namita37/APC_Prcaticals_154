# mathutils/statistics.py - Statistical operations
def mean(data): return sum(data) / len(data) if data else 0
def maximum(data): return max(data) if data else None
def minimum(data): return min(data) if data else None
