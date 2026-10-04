from diagnostics.cli import check_config
def test_not_set(monkeypatch):
    monkeypatch.delenv("DIAG_CONFIG", raising=False)
    assert check_config()["configured"] == False
def test_set(monkeypatch):
    monkeypatch.setenv("DIAG_CONFIG", "hello")
    assert check_config()["configured"] == True
