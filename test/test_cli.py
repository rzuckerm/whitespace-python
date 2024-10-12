from unittest.mock import patch
from whitespace.cli import main


def test_main_with_no_errors(caplog):
    assert main(["test/fixtures/hello.ws"]) == 0

    assert not caplog.text


def test_main_with_parser_error(caplog):
    assert main(["test/fixtures/parse-error.ws"]) == 1

    assert "parsing" in caplog.text


def test_main_with_runtime_error(caplog):
    assert main(["test/fixtures/runtime-error.ws"]) == 2

    assert "executing" in caplog.text


@patch("whitespace.cli.run")
def test_main_with_other_error(mock_run, caplog):
    mock_run.side_effect = Exception("Something else")

    assert main(["test/fixtures/parse-error.ws"]) == 3

    assert "unexpected" in caplog.text
