#!/usr/bin/env python3
"""Module Three"""

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function named index_range that takes two integer
        arguments page and page_size return a tuple of
        size two containing a start index and an end
        index corresponding to the range of indexes to
        return in a list for those particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skipping the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """method named get_page that takes two integer arguments page
            with default value 1 and page_size with default value 10.
            You have to use this CSV file (same as the one presented at
            the top of the project)
        Args:
            assert:  verify that both arguments are integers greater than 0.
            find the correct indexes to paginate the dataset correctly and
            return the appropriate page of the dataset
            (i.e. the correct list of rows). If the input arguments are out of
            range for the dataset, an empty list should be returned.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.dataset()
        start, end = index_range(page, page_size)

        if start >= len(dataset):
            return []
        return dataset[start:end]

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str, object]:
        """Implement a get_hyper method that takes the same
            arguments (and defaults) as get_page and returns a
            dictionary containing the  following key-value pairs:
        Args:
            page_size: the length of the returned dataset page
            page: the current page number
            data: dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        Note:
            make sure to reuse get_page in your implementation
            you can use the math module if necessary
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
