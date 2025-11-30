name: Run Tests

on: push

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - name: Check out code
        uses: actions/checkout@v3
      
      - name: Run test 1
        run: |
          python3 find_lowest_number.py test_data/test1_input.txt output1.txt
          diff output1.txt test_data/test1_expected.txt
      
      - name: Run test 2
        run: |
          python3 find_lowest_number.py test_data/test2_input.txt output2.txt
          diff output2.txt test_data/test2_expected.txt
      
      - name: Run test 3
        run: |
          python3 find_lowest_number.py test_data/test3_input.txt output3.txt
          diff output3.txt test_data/test3_expected.txt
