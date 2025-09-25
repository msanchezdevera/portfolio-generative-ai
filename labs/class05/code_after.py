from typing import List, Any, Optional


def find_index(lst: List[Any], value: Any) -> int:
    """
    Return the index of the first occurrence of value in the list, or -1 if not found.
    
    This function searches for the specified value in the given list and returns
    the index of its first occurrence. If the value is not found, it returns -1.
    
    Args:
        lst: The list to search in
        value: The value to search for
        
    Returns:
        The index of the first occurrence of value, or -1 if not found
        
    Examples:
        >>> find_index([1, 2, 3, 4], 3)
        2
        >>> find_index(['apple', 'banana', 'cherry'], 'banana')
        1
        >>> find_index([1, 2, 3, 2], 2)
        1
        >>> find_index([1, 2, 3], 5)
        -1
        >>> find_index([], 1)
        -1
    """
    try:
        return lst.index(value)
    except ValueError:
        return -1


def find_index_manual(lst: List[Any], value: Any) -> int:
    """
    Manual implementation of find_index without using built-in index() method.
    
    Return the index of the first occurrence of value in the list, or -1 if not found.
    This version demonstrates the corrected manual approach with early return.
    
    Args:
        lst: The list to search in
        value: The value to search for
        
    Returns:
        The index of the first occurrence of value, or -1 if not found
        
    Examples:
        >>> find_index_manual([1, 2, 3, 4], 3)
        2
        >>> find_index_manual(['apple', 'banana', 'cherry'], 'banana')
        1
        >>> find_index_manual([1, 2, 3], 5)
        -1
    """
    for i, item in enumerate(lst):
        if item == value:
            return i  # Early return - stops iteration immediately
    return -1


def find_all_indices(lst: List[Any], value: Any) -> List[int]:
    """
    Return all indices where value appears in the list.
    
    This function finds all occurrences of the specified value and returns
    a list of their indices. If the value is not found, returns an empty list.
    
    Args:
        lst: The list to search in
        value: The value to search for
        
    Returns:
        A list of all indices where value appears
        
    Examples:
        >>> find_all_indices([1, 2, 3, 2, 2], 2)
        [1, 3, 4]
        >>> find_all_indices(['a', 'b', 'a', 'c'], 'a')
        [0, 2]
        >>> find_all_indices([1, 2, 3], 5)
        []
    """
    return [i for i, item in enumerate(lst) if item == value]


# Demonstration and testing
if __name__ == "__main__":
    # Test cases to demonstrate the improvements
    test_list = [1, 2, 3, 2, 4, 2]
    search_value = 2
    
    print("Testing find_index function:")
    print(f"List: {test_list}")
    print(f"Searching for: {search_value}")
    print(f"First index: {find_index(test_list, search_value)}")
    print(f"Manual implementation: {find_index_manual(test_list, search_value)}")
    print(f"All indices: {find_all_indices(test_list, search_value)}")
    
    # Test edge cases
    print("\nTesting edge cases:")
    print(f"Empty list: {find_index([], 1)}")
    print(f"Value not found: {find_index([1, 2, 3], 5)}")
    print(f"String search: {find_index(['apple', 'banana'], 'banana')}")