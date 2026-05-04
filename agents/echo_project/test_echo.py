#!/usr/bin/env python3
"""
Test cases for echo_project
Verifies that the echo.py program runs correctly
"""

import subprocess
import sys
import os

# Path to the echo.py script
ECHO_PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
ECHO_PY_PATH = os.path.join(ECHO_PROJECT_DIR, "echo.py")


def run_echo_with_input(input_lines):
    """
    Run echo.py with given input lines and return the output.
    """
    input_text = "\n".join(input_lines) + "\n"
    result = subprocess.run(
        ["python", ECHO_PY_PATH],
        input=input_text,
        capture_output=True,
        text=True,
        timeout=5
    )
    return result.stdout, result.stderr, result.returncode


def test_echo_project_exists():
    """Test 1: Verify the echo.py file exists"""
    assert os.path.exists(ECHO_PY_PATH), f"echo.py not found at {ECHO_PY_PATH}"
    print("✓ Test 1 passed: echo.py exists")


def test_welcome_message():
    """Test 2: Verify welcome message is displayed"""
    stdout, stderr, returncode = run_echo_with_input(["quit"])
    assert "Echo Program" in stdout, "Welcome message not found in output"
    print("✓ Test 2 passed: Welcome message displayed")


def test_basic_echo():
    """Test 3: Verify basic echo functionality"""
    stdout, stderr, returncode = run_echo_with_input(["Hello", "quit"])
    assert "Echo:" in stdout and "Hello" in stdout, "Echo output not found"
    print("✓ Test 3 passed: Basic echo works")


def test_echo_preserves_input():
    """Test 4: Verify echo preserves exact input"""
    test_input = "Test input 123"
    stdout, stderr, returncode = run_echo_with_input([test_input, "quit"])
    assert f"Echo: {test_input}" in stdout, "Echo did not preserve exact input"
    print("✓ Test 4 passed: Echo preserves input exactly")


def test_quit_command():
    """Test 5: Verify 'quit' command exits the program"""
    stdout, stderr, returncode = run_echo_with_input(["quit"])
    assert returncode == 0, "Program should exit cleanly with 'quit'"
    print("✓ Test 5 passed: 'quit' command works")


def test_exit_command():
    """Test 6: Verify 'exit' command exits the program"""
    stdout, stderr, returncode = run_echo_with_input(["exit"])
    assert returncode == 0, "Program should exit cleanly with 'exit'"
    print("✓ Test 6 passed: 'exit' command works")


def test_q_command():
    """Test 7: Verify 'q' command exits the program"""
    stdout, stderr, returncode = run_echo_with_input(["q"])
    assert returncode == 0, "Program should exit cleanly with 'q'"
    print("✓ Test 7 passed: 'q' command works")


def test_multiple_inputs():
    """Test 8: Verify multiple inputs are all echoed"""
    inputs = ["First", "Second", "Third"]
    stdout, stderr, returncode = run_echo_with_input(inputs + ["quit"])
    
    for inp in inputs:
        assert f"Echo: {inp}" in stdout, f"Input '{inp}' was not echoed"
    print("✓ Test 8 passed: Multiple inputs echoed correctly")


def test_special_characters():
    """Test 9: Verify special characters are handled"""
    test_input = "Hello! @#$%^&*()"
    stdout, stderr, returncode = run_echo_with_input([test_input, "quit"])
    assert f"Echo: {test_input}" in stdout, "Special characters not handled"
    print("✓ Test 9 passed: Special characters handled")


def test_unicode_input():
    """Test 10: Verify Unicode input is handled"""
    test_input = "你好世界 🌍 αβγδ"
    stdout, stderr, returncode = run_echo_with_input([test_input, "quit"])
    assert f"Echo: {test_input}" in stdout, "Unicode input not handled"
    print("✓ Test 10 passed: Unicode input handled")


def test_empty_input():
    """Test 11: Verify empty input is handled"""
    stdout, stderr, returncode = run_echo_with_input(["", "quit"])
    assert "Echo:" in stdout, "Empty input should still produce echo"
    print("✓ Test 11 passed: Empty input handled")


def test_prompt_format():
    """Test 12: Verify proper prompt format"""
    stdout, stderr, returncode = run_echo_with_input(["test", "quit"])
    assert "You:" in stdout, "Prompt format 'You:' not found"
    assert "Echo:" in stdout, "Echo format 'Echo:' not found"
    print("✓ Test 12 passed: Prompt format correct")


def test_no_error_on_stderr():
    """Test 13: Verify no errors are written to stderr"""
    stdout, stderr, returncode = run_echo_with_input(["test", "quit"])
    assert stderr == "", f"Unexpected stderr output: {stderr}"
    print("✓ Test 13 passed: No errors in stderr")


def run_all_tests():
    """Run all test cases"""
    print("=" * 50)
    print("Running Echo Project Test Suite")
    print("=" * 50)
    
    tests = [
        test_echo_project_exists,
        test_welcome_message,
        test_basic_echo,
        test_echo_preserves_input,
        test_quit_command,
        test_exit_command,
        test_q_command,
        test_multiple_inputs,
        test_special_characters,
        test_unicode_input,
        test_empty_input,
        test_prompt_format,
        test_no_error_on_stderr,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} error: {e}")
            failed += 1
    
    print("=" * 50)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("=" * 50)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
