from utils import list_utils

import unittest

class ListUtilsTests(unittest.TestCase):

    #
    # alternate_unordered_list_delimiters
    #

    def test_alternateUnorderedListDelimiters(self):

        text = """- item 1
    * sub item
        - sub sub item
* item 2"""

        expected = """- item 1
    + sub item
        * sub sub item
- item 2"""
        actual = list_utils.alternate_unordered_list_delimiters(text)

        self.assertEqual(actual, expected)

    def test_alternateUnorderedListDelimiters_withDelimiters(self):

        text = """- item 1
    * sub item
        - sub sub item
* item 2"""
        delimiters = ['+', '*', '-']

        expected = """+ item 1
    * sub item
        - sub sub item
+ item 2"""
        actual = list_utils.alternate_unordered_list_delimiters(text, delimiters)

        self.assertEqual(actual, expected)

    def test_alternateUnorderedListDelimiters_spaces(self):

        text = '- item\n    - subitem\n        - subsubitem'
        delimiters = ['-', '+', '*']

        expected = '- item\n    + subitem\n        * subsubitem'
        actual = list_utils.alternate_unordered_list_delimiters(text, delimiters)

        self.assertEqual(actual, expected)

    def test_alternateUnorderedListDelimiters_tabs(self):

        text = '- item\n\t- subitem\n\t\t- subsubitem'
        delimiters = ['-', '+', '*']

        expected = '- item\n\t+ subitem\n\t\t* subsubitem'
        actual = list_utils.alternate_unordered_list_delimiters(text, delimiters)

        self.assertEqual(actual, expected)

    def test_alternateUnorderedListDelimiters_tabsAndSpaces(self):

        text = '- item\n\t- subitem\n\t    - subsubitem\n    \t- subsubitem\n    \t    - subsubsubitem'
        delimiters = ['-', '+', '*']

        expected = '- item\n\t+ subitem\n\t    * subsubitem\n    \t* subsubitem\n    \t    - subsubsubitem'
        actual = list_utils.alternate_unordered_list_delimiters(text, delimiters)

        self.assertEqual(actual, expected)

    def test_alternateUnorderedListDelimiters_rollOver(self):

        text = '+ item\n\t+ subitem\n\t\t+ subsubitem\n\t\t\t+ subsubsubitem'
        delimiters = ['-', '+', '*']

        expected = '- item\n\t+ subitem\n\t\t* subsubitem\n\t\t\t- subsubsubitem'
        actual = list_utils.alternate_unordered_list_delimiters(text, delimiters)

        self.assertEqual(actual, expected)

    def test_alternateUnorderedListDelimiters_convertToSingleDelimiter(self):

        text = "* item one\n* item two\n* item three"
        delimiters = ['-']

        expected = "- item one\n- item two\n- item three"
        actual = list_utils.alternate_unordered_list_delimiters(text, delimiters)

        self.assertEqual(actual, expected)

    def test_alternateUnorderedListDelimiters_convertToSingleDelimiter_withSubItems(self):

        text = """- item
    * sub item
        + sub sub item"""
        delimiters = ['-']

        expected = """- item
    - sub item
        - sub sub item"""
        actual = list_utils.alternate_unordered_list_delimiters(text, delimiters)

        self.assertEqual(actual, expected)

    def test_alternateUnorderedListDelimiters_allSameLevel_oneOfEach(self):

        text = "- item one\n+ item two\n* item three"
        delimiters = ['-', '+', '*']

        expected = "- item one\n- item two\n- item three"
        actual = list_utils.alternate_unordered_list_delimiters(text, delimiters)

        self.assertEqual(actual, expected)

    def test_alternateUnorderedListDelimiters_doesNothing(self):

        text = 'item one'

        expected = text
        actual = list_utils.alternate_unordered_list_delimiters(text)

        self.assertEqual(actual, expected)


    #
    # _is_unordered_list_item
    #

    def test__isUnorderedListItem_dash(self):

        text = '- item'
        is_item = list_utils._is_unordered_list_item(text)

        self.assertTrue(is_item)

    def test__isUnorderedListItem_plus(self):

        text = '+ item'
        is_item = list_utils._is_unordered_list_item(text)

        self.assertTrue(is_item)

    def test__isUnorderedListItem_asterisk(self):

        text = '* item'
        is_item = list_utils._is_unordered_list_item(text)

        self.assertTrue(is_item)

    def test__isUnorderedListItem_subItem_spaces(self):

        text = '    - item'
        is_item = list_utils._is_unordered_list_item(text)

        self.assertTrue(is_item)

    def test__isUnorderedListItem_subItem_tab(self):

        text = '\t- item'
        is_item = list_utils._is_unordered_list_item(text)

        self.assertTrue(is_item)

    def test__isUnorderedListItem_false(self):

        text = 'This is just text.'
        is_item = list_utils._is_unordered_list_item(text)

        self.assertFalse(is_item)

    def test__isUnorderedListItem_orderedItem(self):

        text = '1. This is an ordered item.'
        is_item = list_utils._is_unordered_list_item(text)

        self.assertFalse(is_item)

    def test__isUnorderedListItem_empty(self):

        text = ''
        is_item = list_utils._is_unordered_list_item(text)

        self.assertFalse(is_item)

    def test__isUnorderedListItem_blank(self):

        text = '    '
        is_item = list_utils._is_unordered_list_item(text)

        self.assertFalse(is_item)

    def test__isUnorderedListItem_none(self):

        text = None
        is_item = list_utils._is_unordered_list_item(text)

        self.assertFalse(is_item)

    def test__isUnorderedListItem_multipleItems(self):

        text = '- item one\n- item two'
        is_item = list_utils._is_unordered_list_item(text)

        self.assertFalse(is_item)

    #
    # _is_unordered_list_item
    #

    def test__isOrderedListItem(self):

        text = '1. item'
        is_item = list_utils._is_ordered_list_item(text)

        self.assertTrue(is_item)

    def test__isOrderedListItem_subItem_spaces(self):

        text = '    2. item'
        is_item = list_utils._is_ordered_list_item(text)

        self.assertTrue(is_item)

    def test__isOrderedListItem_subItem_tab(self):

        text = '\t3. item'
        is_item = list_utils._is_ordered_list_item(text)

        self.assertTrue(is_item)

    def test__isOrderedListItem_false(self):

        text = 'This is just text.'
        is_item = list_utils._is_ordered_list_item(text)

        self.assertFalse(is_item)

    def test__isOrderedListItem_false_notPeriodDelimited(self):

        text = '1, Item'
        is_item = list_utils._is_ordered_list_item(text)

        self.assertFalse(is_item)

    def test__isOrderedListItem_unorderedItem(self):

        text = '1 This is an unordered item'
        is_item = list_utils._is_ordered_list_item(text)

        self.assertFalse(is_item)

    def test__isOrderedListItem_empty(self):

        text = ''
        is_item = list_utils._is_ordered_list_item(text)

        self.assertFalse(is_item)

    def test__isOrderedListItem_blank(self):

        text = '    '
        is_item = list_utils._is_ordered_list_item(text)

        self.assertFalse(is_item)

    def test__isOrderedListItem_none(self):

        text = None
        is_item = list_utils._is_ordered_list_item(text)

        self.assertFalse(is_item)

    def test__isOrderedListItem_multipleItems(self):

        text = '1. item one\n2. item two'
        is_item = list_utils._is_ordered_list_item(text)

        self.assertFalse(is_item)

    #
    # _tab_count
    #

    def test__tabCount_none(self):

        text = None
        tab_count = list_utils._tab_count(text)

        self.assertEqual(tab_count, 0)

    def test__tabCount_empty(self):

        text = ''
        tab_count = list_utils._tab_count(text)

        self.assertEqual(tab_count, 0)

    def test__tabCount_blank(self):

        text = '  '
        tab_count = list_utils._tab_count(text)

        self.assertEqual(tab_count, 0)

    def test__tabCount_zero(self):

        text = 'No tabs'
        tab_count = list_utils._tab_count(text)

        self.assertEqual(tab_count, 0)

    def test__tabCount_one(self):

        text = '\tOne tab'
        tab_count = list_utils._tab_count(text)

        self.assertEqual(tab_count, 1)

    def test__tabCount_two(self):

        text = '\t\tTwo tab'
        tab_count = list_utils._tab_count(text)

        self.assertEqual(tab_count, 2)

    def test__tabCount_many(self):

        text = '\t\t\t\t\t\tMany tabs'
        tab_count = list_utils._tab_count(text)

        self.assertEqual(tab_count, 6)

    def test__tabCount_spaces_one(self):

        text = '    One tab'
        tab_count = list_utils._tab_count(text)

        self.assertEqual(tab_count, 1)

    def test__tabCount_spaces_many(self):

        text = '    ' * 6 + 'Many tab'
        tab_count = list_utils._tab_count(text)

        self.assertEqual(tab_count, 6)

    def test__tabCount_mixed(self):

        text = '\t    \t\t        Mixed tab types'
        tab_count = list_utils._tab_count(text)

        self.assertEqual(tab_count, 6)

    #
    # fix_ordered_list_numbering
    #

    def test_fixOrderedListNumbering_doesNothing(self):

        text = '3. item one'

        expected = text
        actual = list_utils.fix_ordered_list_numbering(text)

        self.assertEqual(actual, expected)
