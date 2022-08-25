"""
Author: Satya Jhaveri
Unit: FIT2004
Purpose: Test Cases for FIT2004 Assignment 4, 2022 Semester 1
Disclaimer: This contains the test cases from the Assignment pdf, and some custom ones I added.
    I can't guarantee that the custom test cases are all right, but afaik they're correct, pls
    point out any errors tho

    Also just because your code has 0 errors doesn't mean you'll get 100% on your assignment, check
    your code fits the time and space complexity requirements listed in the instructions, both
    tasks have pretty (relatively) easy-to-code brute force solutions but that ain't what the markers
    are looking for.

To use this tester: Just put this file in the same directory as your assignment code file and run this
    file(your code file must be named "assignment4.py", as per the assignment instructions).
"""

from myversionofp1 import allocate#, EventsTrie
import unittest


class TestAssignment(unittest.TestCase):
    def setUp(self) -> None:
        # Create list of errors to collect over all tests:
        self.errorList = []

    def tearDown(self) -> None:
        # Print all errors found:
        for e in self.errorList:
            print(e)
        print(f"Number of errors: {len(self.errorList)}")

    def test_allocate(self) -> None:
        # my lord this was a pain to do
        # Test 1 with Preference set #1:
        preferences = [[0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                       [1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                       [0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
                       [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
                       [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
                       [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
                       [0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
                       [0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                       [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
                       [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
                       [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
                       [0, 1, 0, 1, 0, 0, 0, 1, 1, 1],
                       [0, 0, 1, 0, 1, 1, 1, 1, 1, 1],
                       [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
                       [0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                       [1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
                       [1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                       [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
                       [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                       [0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
                       [1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
                       [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
                       [0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
                       [0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                       [1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
                       [1, 0, 0, 1, 0, 1, 1, 1, 1, 0],
                       [1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
                       [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 1, 0, 1, 0, 0]]
        min_shifts = 5
        max_unwanted_shifts = 10
        sys_admins_per_night = 6
        expectingNone = False
        try:
            res = allocate(preferences, sys_admins_per_night, max_unwanted_shifts, min_shifts)
            # Validate output:
            if expectingNone:
                self.assertIsNone(res,
                                  msg=f"allocate(preferences=preference set #1, sys_admins_per_night={sys_admins_per_night}, max_unwanted_shifts={max_unwanted_shifts} should have returned None\nYour output was: {res}\n")
            else:
                # Check the min shifts of all workers:
                for i in range(len(res[0])):
                    self.assertLessEqual(min_shifts, sum(d[i] for d in res),
                                         msg=f"allocate(preferences=preference set #1, sys_admins_per_night={sys_admins_per_night}, max_unwanted_shifts={max_unwanted_shifts} did not meet the minimum shift requirement.\nYour output was: {res}\n")

                # Check the max unwanted shifts is not exceeded:
                for i in range(len(res[0])):
                    num_unwanted = 0
                    for d in range(len(res)):
                        if preferences[d][i] == 0 and res[d][i]: num_unwanted += 1
                    self.assertLessEqual(num_unwanted, max_unwanted_shifts,
                                         msg=f"allocate(preferences=preference set #1, sys_admins_per_night={sys_admins_per_night}, max_unwanted_shifts={max_unwanted_shifts} exceeded the maximum unwanted shift requirement.\nYour output was: {res}\n")

                # Check the sys_admins per night:
                for d in range(len(res)):
                    self.assertEqual(sys_admins_per_night, sum(res[d]),
                                     msg=f"allocate(preferences=preference set #1, sys_admins_per_night={sys_admins_per_night}, max_unwanted_shifts={max_unwanted_shifts} did not match the sys_admins_per_night requirement.\nYour output was: {res}\n")

        except AssertionError as e:
            self.errorList.append(str(e))
        except Exception as e:
            self.errorList.append(
                f"allocate(preferences=preference set #1, sys_admins_per_night={sys_admins_per_night}, max_unwanted_shifts={max_unwanted_shifts}, min_shifts={min_shifts}) raised the error: {str(e)}")

        # Test 2 with Preference set 1:
        preferences = [[0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                       [1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                       [0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
                       [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
                       [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
                       [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
                       [0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
                       [0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                       [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
                       [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
                       [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
                       [0, 1, 0, 1, 0, 0, 0, 1, 1, 1],
                       [0, 0, 1, 0, 1, 1, 1, 1, 1, 1],
                       [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
                       [0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                       [1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
                       [1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                       [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
                       [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                       [0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
                       [1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
                       [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
                       [0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
                       [0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                       [1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
                       [1, 0, 0, 1, 0, 1, 1, 1, 1, 0],
                       [1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
                       [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 1, 0, 1, 0, 0]]
        min_shifts = 5
        max_unwanted_shifts = 10
        sys_admins_per_night = 7
        expectingNone = False
        try:
            res = allocate(preferences, sys_admins_per_night, max_unwanted_shifts, min_shifts)
            # Validate output:
            if expectingNone:
                self.assertIsNone(res,
                                  msg=f"allocate(preferences=preference set #1, sys_admins_per_night={sys_admins_per_night}, max_unwanted_shifts={max_unwanted_shifts} should have returned None\nYour output was: {res}\n")
            else:
                # Check the min shifts of all workers:
                for i in range(len(res[0])):
                    self.assertLessEqual(min_shifts, sum(d[i] for d in res),
                                         msg=f"allocate(preferences=preference set #1, sys_admins_per_night={sys_admins_per_night}, max_unwanted_shifts={max_unwanted_shifts} did not meet the minimum shift requirement.\nYour output was: {res}\n")

                # Check the max unwanted shifts is not exceeded:
                for i in range(len(res[0])):
                    num_unwanted = 0
                    for d in range(len(res)):
                        if preferences[d][i] == 0 and res[d][i]: num_unwanted += 1
                    self.assertLessEqual(num_unwanted, max_unwanted_shifts,
                                         msg=f"allocate(preferences=preference set #1, sys_admins_per_night={sys_admins_per_night}, max_unwanted_shifts={max_unwanted_shifts} exceeded the maximum unwanted shift requirement.\nYour output was: {res}\n")

                # Check the sys_admins per night:
                for d in range(len(res)):
                    self.assertEqual(sys_admins_per_night, sum(res[d]),
                                     msg=f"allocate(preferences=preference set #1, sys_admins_per_night={sys_admins_per_night}, max_unwanted_shifts={max_unwanted_shifts} did not match the sys_admins_per_night requirement.\nYour output was: {res}\n")

        except AssertionError as e:
            self.errorList.append(str(e))
        except Exception as e:
            self.errorList.append(
                f"allocate(preferences=preference set #1, sys_admins_per_night={sys_admins_per_night}, max_unwanted_shifts={max_unwanted_shifts}, min_shifts={min_shifts}) raised the error: {str(e)}")

        # Test 3 with preference set 1:
        preferences = [[0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                       [1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                       [0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
                       [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
                       [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
                       [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
                       [0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
                       [0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                       [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
                       [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
                       [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
                       [0, 1, 0, 1, 0, 0, 0, 1, 1, 1],
                       [0, 0, 1, 0, 1, 1, 1, 1, 1, 1],
                       [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
                       [0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                       [1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
                       [1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                       [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
                       [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                       [0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
                       [1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
                       [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
                       [0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
                       [0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                       [1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
                       [1, 0, 0, 1, 0, 1, 1, 1, 1, 0],
                       [1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
                       [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 1, 0, 1, 0, 0]]
        min_shifts = 5
        max_unwanted_shifts = 10
        sys_admins_per_night = 8
        expectingNone = True
        try:
            res = allocate(preferences, sys_admins_per_night, max_unwanted_shifts, min_shifts)
            # Validate output:
            if expectingNone:
                self.assertIsNone(res,
                                  msg=f"allocate(preferences=preference set #1, sys_admins_per_night={sys_admins_per_night}, max_unwanted_shifts={max_unwanted_shifts} should have returned None\nYour output was: {res}\n")
            else:
                # Check the min shifts of all workers:
                for i in range(len(res[0])):
                    self.assertLessEqual(min_shifts, sum(d[i] for d in res),
                                         msg=f"allocate(preferences=preference set #1, sys_admins_per_night={sys_admins_per_night}, max_unwanted_shifts={max_unwanted_shifts} did not meet the minimum shift requirement.\nYour output was: {res}\n")

                # Check the max unwanted shifts is not exceeded:
                for i in range(len(res[0])):
                    num_unwanted = 0
                    for d in range(len(res)):
                        if preferences[d][i] == 0 and res[d][i]: num_unwanted += 1
                    self.assertLessEqual(num_unwanted, max_unwanted_shifts,
                                         msg=f"allocate(preferences=preference set #1, sys_admins_per_night={sys_admins_per_night}, max_unwanted_shifts={max_unwanted_shifts} exceeded the maximum unwanted shift requirement.\nYour output was: {res}\n")

                # Check the sys_admins per night:
                for d in range(len(res)):
                    self.assertEqual(sys_admins_per_night, sum(res[d]),
                                     msg=f"allocate(preferences=preference set #1, sys_admins_per_night={sys_admins_per_night}, max_unwanted_shifts={max_unwanted_shifts} did not match the sys_admins_per_night requirement.\nYour output was: {res}\n")

        except AssertionError as e:
            self.errorList.append(str(e))
        except Exception as e:
            self.errorList.append(
                f"allocate(preferences=preference set #1, sys_admins_per_night={sys_admins_per_night}, max_unwanted_shifts={max_unwanted_shifts}, min_shifts={min_shifts}) raised the error: {str(e)}")

        # Test 4 with preference set 1:
        preferences = [[0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                       [1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                       [0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
                       [1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
                       [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
                       [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
                       [0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
                       [0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                       [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
                       [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
                       [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
                       [0, 1, 0, 1, 0, 0, 0, 1, 1, 1],
                       [0, 0, 1, 0, 1, 1, 1, 1, 1, 1],
                       [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
                       [0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                       [1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
                       [1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                       [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
                       [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                       [0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
                       [1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
                       [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
                       [0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
                       [0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                       [1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
                       [1, 0, 0, 1, 0, 1, 1, 1, 1, 0],
                       [1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
                       [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 1, 0, 1, 0, 0]]
        min_shifts = 5
        max_unwanted_shifts = 10
        sys_admins_per_night = 9
        expectingNone = True
        try:
            res = allocate(preferences, sys_admins_per_night, max_unwanted_shifts, min_shifts)
            # Validate output:
            if expectingNone:
                self.assertIsNone(res,
                                  msg=f"allocate(preferences=preference set #1, sys_admins_per_night={sys_admins_per_night}, max_unwanted_shifts={max_unwanted_shifts} should have returned None\nYour output was: {res}\n")
            else:
                # Check the min shifts of all workers:
                for i in range(len(res[0])):
                    self.assertLessEqual(min_shifts, sum(d[i] for d in res),
                                         msg=f"allocate(preferences=preference set #1, sys_admins_per_night={sys_admins_per_night}, max_unwanted_shifts={max_unwanted_shifts} did not meet the minimum shift requirement.\nYour output was: {res}\n")

                # Check the max unwanted shifts is not exceeded:
                for i in range(len(res[0])):
                    num_unwanted = 0
                    for d in range(len(res)):
                        if preferences[d][i] == 0 and res[d][i]: num_unwanted += 1
                    self.assertLessEqual(num_unwanted, max_unwanted_shifts,
                                         msg=f"allocate(preferences=preference set #1, sys_admins_per_night={sys_admins_per_night}, max_unwanted_shifts={max_unwanted_shifts} exceeded the maximum unwanted shift requirement.\nYour output was: {res}\n")

                # Check the sys_admins per night:
                for d in range(len(res)):
                    self.assertEqual(sys_admins_per_night, sum(res[d]),
                                     msg=f"allocate(preferences=preference set #1, sys_admins_per_night={sys_admins_per_night}, max_unwanted_shifts={max_unwanted_shifts} did not match the sys_admins_per_night requirement.\nYour output was: {res}\n")

        except AssertionError as e:
            self.errorList.append(str(e))
        except Exception as e:
            self.errorList.append(
                f"allocate(preferences=preference set #1, sys_admins_per_night={sys_admins_per_night}, max_unwanted_shifts={max_unwanted_shifts}, min_shifts={min_shifts}) raised the error: {str(e)}")

    def test_get_longest_chain(self) -> None:
        # Implementing test cases from the assignment pdf:
        # Example 1:
        # Example 1.1:
        timelines = ["abc", "dbcef", "gdbc"]
        expected_res = "bc"
        noccurence = 3

        try:
            myTrie = EventsTrie(timelines)
        except Exception as e:
            self.errorList.append(f"EventsTrie(timelines={timelines}) raised the error: {str(e)}")

        try:
            res = myTrie.getLongestChain(noccurence)
            self.assertEqual(res, expected_res,
                             msg=f"Output for getLongestChain(noccurence={noccurence})\n incorrect. \nExpected:{expected_res}.\nYour function returned: {res}\n")
        except AssertionError as e:
            self.errorList.append(str(e))
        except Exception as e:
            self.errorList.append(f"getLongestChain(noccurence={noccurence}) raised the error: {str(e)}")

        # Example 1.2:
        timelines = ["abc", "dbcef", "gdbc"]
        expected_res = "dbc"
        noccurence = 2

        try:
            myTrie = EventsTrie(timelines)
        except Exception as e:
            self.errorList.append(f"EventsTrie(timelines={timelines}) raised the error: {str(e)}")

        try:
            res = myTrie.getLongestChain(noccurence)
            self.assertEqual(res, expected_res,
                             msg=f"Output for getLongestChain(noccurence={noccurence})\n incorrect. \nExpected:{expected_res}.\nYour function returned: {res}\n")
        except AssertionError as e:
            self.errorList.append(str(e))
        except Exception as e:
            self.errorList.append(f"getLongestChain(noccurence={noccurence}) raised the error: {str(e)}")

        # Example 1.3:
        timelines = ["abc", "dbcef", "gdbc"]
        expected_res = "dbcef"
        noccurence = 1

        try:
            myTrie = EventsTrie(timelines)
        except Exception as e:
            self.errorList.append(f"EventsTrie(timelines={timelines}) raised the error: {str(e)}")

        try:
            res = myTrie.getLongestChain(noccurence)
            self.assertEqual(res, expected_res,
                             msg=f"Output for getLongestChain(noccurence={noccurence})\n incorrect. \nExpected:{expected_res}.\nYour function returned: {res}\n")
        except AssertionError as e:
            self.errorList.append(str(e))
        except Exception as e:
            self.errorList.append(f"getLongestChain(noccurence={noccurence}) raised the error: {str(e)}")

        # Example 2:
        # Example 2.1:
        timelines = ["abaaac", "dbce", "aabcba", "dbce", "caaaa"]
        accepted_res = ["abaaac", "aabcba"]
        noccurence = 1

        try:
            myTrie = EventsTrie(timelines)
        except Exception as e:
            self.errorList.append(f"EventsTrie(timelines={timelines}) raised the error: {str(e)}")

        try:
            res = myTrie.getLongestChain(noccurence)
            self.assertTrue(res in accepted_res,
                            msg=f"Output for getLongestChain(noccurence={noccurence})\n incorrect. \Accepted results:{accepted_res}.\nYour function returned: {res}\n")
        except AssertionError as e:
            self.errorList.append(str(e))
        except Exception as e:
            self.errorList.append(f"getLongestChain(noccurence={noccurence}) raised the error: {str(e)}")

        # Example 2.2:
        timelines = ["abaaac", "dbce", "aabcba", "dbce", "caaaa"]
        expected_res = "dbce"
        noccurence = 2

        try:
            myTrie = EventsTrie(timelines)
        except Exception as e:
            self.errorList.append(f"EventsTrie(timelines={timelines}) raised the error: {str(e)}")

        try:
            res = myTrie.getLongestChain(noccurence)
            self.assertEqual(res, expected_res,
                             msg=f"Output for getLongestChain(noccurence={noccurence})\n incorrect. \nExpected:{expected_res}.\nYour function returned: {res}\n")
        except AssertionError as e:
            self.errorList.append(str(e))
        except Exception as e:
            self.errorList.append(f"getLongestChain(noccurence={noccurence}) raised the error: {str(e)}")

        # Example 2.3:
        timelines = ["abaaac", "dbce", "aabcba", "dbce", "caaaa"]
        accepted_res = ["aa", "bc"]
        noccurence = 3

        try:
            myTrie = EventsTrie(timelines)
        except Exception as e:
            self.errorList.append(f"EventsTrie(timelines={timelines}) raised the error: {str(e)}")

        try:
            res = myTrie.getLongestChain(noccurence)
            self.assertTrue(res in accepted_res,
                            msg=f"Output for getLongestChain(noccurence={noccurence})\n incorrect. \nAccepted results:{accepted_res}.\nYour function returned: {res}\n")
        except AssertionError as e:
            self.errorList.append(str(e))
        except Exception as e:
            self.errorList.append(f"getLongestChain(noccurence={noccurence}) raised the error: {str(e)}")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignment)
    unittest.TextTestRunner(verbosity=0).run(suite)