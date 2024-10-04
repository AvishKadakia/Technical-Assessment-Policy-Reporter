def find_best_threshold(data):
    """
    Finds the best threshold that yields recall >= 0.9.
    'Best' is defined as the threshold with the highest precision.
    If multiple thresholds have the same precision, the highest threshold is selected.

    Parameters:
    data (list): A list of dictionaries, each containing 'threshold', 'tp', 'fp', 'tn', 'fn'.

    Returns:
    float: The best threshold.
    """
    candidates = []
    for entry in data:
        threshold = entry['threshold']
        tp = entry['tp']
        fp = entry['fp']
        tn = entry['tn']
        fn = entry['fn']
        # Calculate recall and precision
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        # Check if recall meets the threshold
        if recall >= 0.9:
            candidates.append({
                'threshold': threshold,
                'precision': precision,
                'recall': recall
            })
    if not candidates:
        return None  # No threshold meets the recall criterion
    # Sort candidates by precision and then by threshold
    candidates.sort(key=lambda x: (x['precision'], x['threshold']), reverse=True)
    best_threshold = candidates[0]['threshold']
    return best_threshold

# Example usage with realistic input data
data = [
    {'threshold': 0.1, 'tp': 95, 'fp': 50, 'tn': 850, 'fn': 5},
    {'threshold': 0.2, 'tp': 90, 'fp': 40, 'tn': 860, 'fn': 10},
    {'threshold': 0.3, 'tp': 85, 'fp': 30, 'tn': 870, 'fn': 15},
    {'threshold': 0.4, 'tp': 80, 'fp': 25, 'tn': 875, 'fn': 20},
    {'threshold': 0.5, 'tp': 75, 'fp': 20, 'tn': 880, 'fn': 25},
    {'threshold': 0.6, 'tp': 70, 'fp': 15, 'tn': 885, 'fn': 30},
    {'threshold': 0.7, 'tp': 65, 'fp': 10, 'tn': 890, 'fn': 35},
    {'threshold': 0.8, 'tp': 60, 'fp': 5, 'tn': 895, 'fn': 40},
    {'threshold': 0.9, 'tp': 55, 'fp': 2, 'tn': 898, 'fn': 45},
]

best_threshold = find_best_threshold(data)
print("Best Threshold:", best_threshold)
