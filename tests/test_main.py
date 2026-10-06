import subprocess
import sys


def test_script_prints_hello_world():
    result = subprocess.run(
        [sys.executable, "main.py"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == "Hello World!"


def test_script_exits_cleanly():
    result = subprocess.run(
        [sys.executable, "main.py"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert result.stderr == ""
