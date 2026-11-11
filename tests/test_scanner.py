import os
from app.scanner import scan_file

def test_aws_key_detection():
    # Create a mock file with a fake secret
    test_file = "mock_code.py"
    with open(test_file, "w") as f:
        f.write('aws_access_key = "AKIA1234567890ABCDEF"\n')
    
    # Run our scanner
    results = scan_file(test_file)
    
    # Clean up the test file
    os.remove(test_file)
    
    # Assertions to prove our code works
    assert len(results) == 1
    assert results[0]["type"] == "AWS Access Key"
    assert results[0]["line"] == 1