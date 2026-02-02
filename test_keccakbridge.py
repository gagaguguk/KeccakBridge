# test_keccakbridge.py
"""
Tests for KeccakBridge module.
"""

import unittest
from keccakbridge import KeccakBridge

class TestKeccakBridge(unittest.TestCase):
    """Test cases for KeccakBridge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = KeccakBridge()
        self.assertIsInstance(instance, KeccakBridge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = KeccakBridge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
