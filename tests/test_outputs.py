import json
from pathlib import Path

REPORT = Path("/app/report.json")


def _load():
    return json.loads(REPORT.read_text())


def test_report_is_valid_json_object():
    """Success criterion 1: /app/report.json exists and is a single valid JSON object."""
    assert REPORT.exists(), "no /app/report.json found"
    data = json.loads(REPORT.read_text())
    assert isinstance(data, dict), "report.json must be a single JSON object"


def test_total_requests():
    """Success criterion 2: total_requests equals the number of non-empty request lines (6)."""
    data = _load()
    assert data["total_requests"] == 6


def test_unique_ips():
    """Success criterion 3: unique_ips equals the number of distinct client IPs (3)."""
    data = _load()
    assert data["unique_ips"] == 3


def test_top_path():
    """Success criterion 4: top_path is the most frequently requested path (/index.html)."""
    data = _load()
    assert data["top_path"] == "/index.html"
