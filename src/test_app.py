import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unittest.mock import patch
from app import process_lead_file, LeadTriageSchema

class TestLeadTriageApp(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.payload_path = os.path.join(self.base_dir, "test_payload.json")

    @patch("app.dispatch_webhook")
    def test_process_lead_payload_high_urgency(self, mock_dispatch):
        mock_dispatch.return_value = True
        result = process_lead_file(self.payload_path)
        self.assertIsInstance(result, LeadTriageSchema)
        self.assertEqual(result.urgency_level, "HIGH")
        self.assertEqual(result.lead_name, "John Sterling")
        mock_dispatch.assert_called_once()

    def test_malformed_payload(self):
        invalid_path = os.path.join(self.base_dir, "non_existent.json")
        with self.assertRaises(FileNotFoundError):
            process_lead_file(invalid_path)

if __name__ == "__main__":
    unittest.main()
