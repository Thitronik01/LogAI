"""Whatever is passed on the command line, the program answers with a status, not a traceback."""

from hypothesis import given
from hypothesis import strategies as st

from logai_scan.cli import main

# Lone surrogates cannot be written to the captured output streams of the test runner.
# A real terminal receives them escaped, so excluding them here loses nothing.
_ARGUMENT = st.text(alphabet=st.characters(exclude_categories=["Cs"]), max_size=40)


@given(argv=st.lists(_ARGUMENT, max_size=6))
def test_arbitrary_arguments_end_in_an_exit_status(argv: list[str]) -> None:
    try:
        status = main(argv)
    except SystemExit as raised:
        status = raised.code

    assert status in (0, 2)
