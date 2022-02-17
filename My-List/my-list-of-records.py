#!/bin/python3

import json
from typing import List, Dict
import pprint
import random

Record = Dict[str, str]
Result = Dict[str, str]
pp = pprint.PrettyPrinter(width=41, compact=True)


def process_records(records: List[Record]) -> List[Result]:
    results: List[Result] = []

    # pp.pprint(records)

    for rec in records:
        print("-" * 80)
        pp.pprint(rec)
        if write_to_database(rec) is None:
            dict1 = {"id": rec["id"], "status": "Success"}
            results.append(dict1)
        else:
            dict1 = {"id": rec["id"], "status": "Failed", "error": "Description of the failure"}
            results.append(dict1)

    return results


def write_to_database(record: Record) -> None:
    codes = [None, 1]
    return random.choice(codes)


def main():
    list1 = []

    for i in range(123, 127):
        req1 = """
        {
            "id": "%s",
            "ipAddress": "234.44.55.356",
            "message": "string"
        }
        """ % str(i)

        '''
        Call API call using API 234.44.55.356
        '''

        resp1 = """
        {
            "country": "United States",
            "city":"Los Angeles",
            "zip": "90071"
        }
        """

        record1 = json.loads(req1)
        enhanced = json.loads(resp1)

        for key, val in enhanced.items():
            record1[key] = val

        list1.append(record1)

    processed = process_records(list1)
    print("-" * 80)
    pp.pprint(processed)
    print("-" * 80)


if __name__ == "__main__":
    main()
