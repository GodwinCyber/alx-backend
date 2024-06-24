#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self, index: int = None, page_size: int = 10
    ) -> Dict[str, Any]:
        """
        Implement a get_hyper_index method with two integer arguments:
        index with a None default value and page_size with default value of 10.
        Args:
            index: the current start index of the return page.
            next_index: the next index to query with
            page_size: the current page size
            data: the actual page of the dataset
        Requirements/Behavior:
            Use assert to verify that index is in a valid range.
            if the user queries index 0, page_size 10, they will
            get rows indexed 0 to 9 included.
            If they request the next index (10) with page_size 10,
            but rows 3, 6 and 7 were deleted, the user should still
            receive rows indexed 10 to 19 included.
        """
        dataset = self.indexed_dataset()
        assert index is not None and 0 <= index <= max(dataset.keys())

        data = []
        data_count = 0
        next_index = None
        start_index = index if index else 0

        for i in range(start_index, len(dataset)):
            if i in dataset:
                if data_count < page_size:
                    data.append(dataset[i])
                    data_count += 1
                else:
                    next_index = i
                    break
        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }
