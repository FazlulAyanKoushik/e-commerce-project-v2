"""
This file contains configuration and fixture definitions for pytest, a testing framework used in this project.

It specifies:
- Additional pytest plugins to be used.
- Fixture definitions for setting up test environments and data.

For more information on fixtures and configuration options in pytest, refer to the official pytest documentation: https://docs.pytest.org/en/stable/
"""

pytest_plugins = [
    "common.tests.fixtures",
    "common.tests.selenium_base",
]
