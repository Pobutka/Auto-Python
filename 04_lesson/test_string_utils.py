import pytest
from StringUtils import StringUtils


class TestStringUtils:

    def setup_method(self):
        self.utils = StringUtils()

    def test_capitalize(self):
        assert self.utils.capitilize("hello") == "Hello"
        assert self.utils.capitilize("Hello") == "Hello"
        assert self.utils.capitilize("") == ""
        assert self.utils.capitilize("123") == "123"

    def test_trim(self):
        assert self.utils.trim("  hello  ") == "hello  "
        assert self.utils.trim("hello") == "hello"
        assert self.utils.trim("") == ""
        assert self.utils.trim("   ") == ""

    def test_to_list(self):
        assert self.utils.to_list("a,b,c") == ["a", "b", "c"]
        assert self.utils.to_list("a;b;c", ";") == ["a", "b", "c"]
        assert self.utils.to_list("", ",") == []
        assert self.utils.to_list("a b c", ",") == ["a b c"]

    def test_contains(self):
        assert self.utils.contains("hello", "e") is True
        assert self.utils.contains("hello", "x") is False
        assert self.utils.contains("", "x") is False

    def test_delete_symbol(self):
        assert self.utils.delete_symbol("hello", "l") == "heo"
        assert self.utils.delete_symbol("hello", "x") == "hello"
        assert self.utils.delete_symbol("", "x") == ""

    def test_starts_with(self):
        assert self.utils.starts_with("hello", "h") is True
        assert self.utils.starts_with("hello", "x") is False
        assert self.utils.starts_with("", "x") is False

    def test_end_with(self):
        assert self.utils.end_with("hello", "o") is True
        assert self.utils.end_with("hello", "x") is False
        assert self.utils.end_with("", "x") is False

    def test_is_empty(self):
        assert self.utils.is_empty("   ") is True
        assert self.utils.is_empty("hello") is False
        assert self.utils.is_empty("") is True

    def test_list_to_string(self):
        assert self.utils.list_to_string(["a", "b", "c"]) == "a, b, c"
        assert self.utils.list_to_string(["a", "b", "c"], "; ") == "a; b; c"
        assert self.utils.list_to_string([]) == ""
