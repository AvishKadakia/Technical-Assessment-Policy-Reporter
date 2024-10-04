import unittest
from assignment_1 import find_best_threshold

class TestFindBestThreshold(unittest.TestCase):
    """
    Unit tests for the find_best_threshold function.
    """

    def test_normal_case(self):
        """
        Test with standard input data where multiple thresholds meet the recall criterion.
        Expect the function to return the threshold with the highest precision.
        """
        data = [
            # Each dictionary represents model performance at a specific threshold
            {'threshold': 0.1, 'tp': 95, 'fp': 50, 'tn': 850, 'fn': 5},
            {'threshold': 0.2, 'tp': 90, 'fp': 40, 'tn': 860, 'fn': 10},
            {'threshold': 0.3, 'tp': 85, 'fp': 30, 'tn': 870, 'fn': 15},
            {'threshold': 0.4, 'tp': 80, 'fp': 25, 'tn': 875, 'fn': 20},
            {'threshold': 0.5, 'tp': 75, 'fp': 20, 'tn': 880, 'fn': 25},
            {'threshold': 0.6, 'tp': 70, 'fp': 15, 'tn': 885, 'fn': 30},
            {'threshold': 0.7, 'tp': 65, 'fp': 10, 'tn': 890, 'fn': 35},
            {'threshold': 0.8, 'tp': 60, 'fp': 5,  'tn': 895, 'fn': 40},
            {'threshold': 0.9, 'tp': 55, 'fp': 2,  'tn': 898, 'fn': 45},
        ]
        expected_threshold = 0.2  # Expected best threshold based on criteria
        result = find_best_threshold(data)
        self.assertEqual(result, expected_threshold)

    def test_no_threshold_meets_recall(self):
        """
        Test case where no threshold meets the recall requirement of >= 0.9.
        Expect the function to return None.
        """
        data = [
            # All thresholds have recall less than 0.9
            {'threshold': 0.1, 'tp': 50, 'fp': 50, 'tn': 850, 'fn': 50},
            {'threshold': 0.2, 'tp': 45, 'fp': 40, 'tn': 860, 'fn': 55},
            {'threshold': 0.3, 'tp': 40, 'fp': 30, 'tn': 870, 'fn': 60},
        ]
        result = find_best_threshold(data)
        self.assertIsNone(result)  # Expecting None since recall criterion isn't met

    def test_multiple_best_precisions(self):
        """
        Test when multiple thresholds have the same highest precision and meet recall >= 0.9.
        Expect the function to return the highest threshold among them.
        """
        data = [
            # Multiple thresholds with same precision and recall
            {'threshold': 0.1, 'tp': 90, 'fp': 10, 'tn': 890, 'fn': 10},  # Precision: 0.9, Recall: 0.9
            {'threshold': 0.2, 'tp': 90, 'fp': 10, 'tn': 890, 'fn': 10},  # Precision: 0.9, Recall: 0.9
            {'threshold': 0.3, 'tp': 85, 'fp': 5,  'tn': 895, 'fn': 15},  # Precision: ~0.944, Recall: ~0.85
            {'threshold': 0.4, 'tp': 95, 'fp': 20, 'tn': 880, 'fn': 5},   # Precision: ~0.826, Recall: 0.95
        ]
        expected_threshold = 0.2  # Highest threshold among those with same precision and recall
        result = find_best_threshold(data)
        self.assertEqual(result, expected_threshold)

    def test_empty_data(self):
        """
        Test with empty data input.
        Expect the function to return None.
        """
        data = []
        result = find_best_threshold(data)
        self.assertIsNone(result)  # No thresholds to evaluate

    def test_zero_division(self):
        """
        Test for edge cases that may cause division by zero in precision or recall calculations.
        Expect the function to handle division by zero and return None.
        """
        data = [
            # Edge case where tp + fp = 0 and tp + fn = 0
            {'threshold': 0.1, 'tp': 0, 'fp': 0, 'tn': 1000, 'fn': 0},
        ]
        result = find_best_threshold(data)
        self.assertIsNone(result)  # Cannot calculate precision or recall; expect None

    def test_all_zero_metrics(self):
        """
        Test when all metric values are zero.
        Expect the function to handle this gracefully and return None.
        """
        data = [
            # All counts are zero
            {'threshold': 0.1, 'tp': 0, 'fp': 0, 'tn': 0, 'fn': 0},
        ]
        result = find_best_threshold(data)
        self.assertIsNone(result)  # No data to compute metrics; expect None

if __name__ == '__main__':
    unittest.main()
