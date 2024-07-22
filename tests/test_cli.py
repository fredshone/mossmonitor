"""Tests for `mossmonitor` CLI."""

from click.testing import CliRunner

from mossmonitor import cli


def test_command_line_interface():
    """Example test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.cli)
    assert result.exit_code == 0
    assert "mossmonitor.cli.cli" in result.output
    help_result = runner.invoke(cli.cli, ["--help"])
    assert help_result.exit_code == 0
    assert (
        "Console script for mossmonitor.\n\nOptions:\n  "
        "--version  Show the version and exit.\n  "
        "--help     Show this message and exit.\n"
        in help_result.output
    )
