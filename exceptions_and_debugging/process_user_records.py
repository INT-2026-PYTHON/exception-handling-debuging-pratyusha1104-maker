"""
## 3. Process User Records with Mixed Exceptions  *(Medium)*

=================================================
PROCESS USER RECORDS WITH MIXED EXCEPTIONS
=================================================

Problem Statement:
You are given a LIST of DICTIONARIES, where
each dictionary is supposed to represent a
user record:
        {"name": str, "age": str, "score": str}

The data is messy — some records are missing
keys, some have non-numeric strings, and some
are not even dictionaries.

Write a Python program that processes the
list and returns a TUPLE:
        (clean_records, error_log)

   - clean_records -> list of dicts with
                       "name": str
                       "age":  int
                       "score": float
   - error_log     -> list of tuples:
                       (index, error_class_name,
                        message)

You must demonstrate FOUR exception-handling
techniques:
   1. Catching MULTIPLE exception types in
      ONE except block.
   2. Using `except ... as e` to inspect the
      exception object.
   3. Using `raise` to re-raise an exception
      after logging.
   4. Using `else` to run code only when the
      try block succeeded.

-------------------------------------------------
Instructions:
1. Define a function:
      def process_records(records):
2. Iterate over the list with an index counter.
3. For each record, use a try / except / else
   chain:
      try:
          - access record["name"], record["age"],
            record["score"]   -> may raise
            KeyError or TypeError
          - convert age to int and score to float
            -> may raise ValueError
      except (KeyError, TypeError) as e:
          - record the error with the class name
            from type(e).__name__
      except ValueError as e:
          - record the error with the message
            str(e)
      else:
          - this branch runs ONLY when no
            exception was raised; append the
            cleaned record to clean_records.
4. Write a SECOND function:
      def process_strict(records):
   that calls process_records, and if ANY
   error occurred, RE-RAISES a RuntimeError
   that contains the number of failures.
   Use the bare `raise` keyword inside an
   except block, OR
       raise RuntimeError(...) from None
   to suppress the original traceback chain.
5. Do NOT use:
   - bare `except:`
   - custom exception classes
   - any external library
6. Call both functions and print:
   - the clean_records list
   - the error_log list
   - the message from the RuntimeError
     (catch it with try/except in the driver)

-------------------------------------------------
Debugging Skills to Practice:
- `type(e).__name__` gives the exact exception
  class as a string — useful for log messages.
- Catching multiple exception types in ONE
  except block: `except (KeyError, TypeError):`
  avoids duplicate handler code.
- The `else` block makes the success path
  visually obvious and prevents accidentally
  catching exceptions raised AFTER the risky
  operation.
- When an exception is re-raised, the original
  traceback is preserved. Read it from the
  BOTTOM up: the last line names the exception,
  the lines above show where it came from.

-------------------------------------------------
Input Example:
records = [
   {"name": "Alice", "age": "25",   "score": "88.5"},
   {"name": "Bob",   "age": "abc",  "score": "70"},
   {"name": "Carol", "age": "30"},                       # missing "score"
   "not a dict",                                          # wrong type
   {"name": "Dan",   "age": "40",   "score": "55.5"},
]

Output Example:
Clean Records:
[
  {'name': 'Alice', 'age': 25, 'score': 88.5},
  {'name': 'Dan',   'age': 40, 'score': 55.5}
]
Error Log:
[
  (1, 'ValueError', "invalid literal for int() with base 10: 'abc'"),
  (2, 'KeyError',   'score'),
  (3, 'TypeError',  'string indices must be integers')
]
Strict mode raised: RuntimeError: 3 record(s) failed to process

-------------------------------------------------
Explanation:
- Record at index 1 ("Bob") has a non-numeric
  age, so int("abc") raises ValueError.
- Record at index 2 ("Carol") is missing the
  "score" key, so record["score"] raises
  KeyError.
- Record at index 3 ("not a dict") is a plain
  string, so record["name"] raises TypeError.
- Records at indices 0 and 4 succeed, so the
  `else` block runs and they are appended to
  clean_records.
- The strict version re-raises a RuntimeError
  summarising the total number of failures.
=================================================

"""
def process_records(records):
    clean_records = []
    error_log = []
    index=0  
    for  record in records:
        try:
            name = record["name"]
            age_str = record["age"]
            score_str = record["score"]
        
            age = int(age_str)
            score = float(score_str)
            
        except (KeyError, TypeError) as e:
            class_name = type(e).__name__
            message = str(e)
            error_log.append((index, class_name, message))
            
        except ValueError as e:
            class_name = type(e).__name__
            message = str(e)
            error_log.append((index, class_name, message))
            
        else:
            cleaned_record = {
                "name": name,
                "age": age,
                "score": score
            }
            clean_records.append(cleaned_record)
            
    return clean_records, error_log


def process_strict(records):
    clean_records, error_log = process_records(records)
    
    if error_log:
        num_failures = len(error_log)
        raise RuntimeError(f"{num_failures} record(s) failed to process") from None
        
    return clean_records, error_log

records = []
print("--- User Record Processing Setup ---")
try:
    num_records = int(input("How many records do you want to input? "))
except ValueError:
    print("Invalid number. Defaulting to 3 records.")
    num_records = 3

for i in range(num_records):
    print(f"\n--- Constructing Record #{i} ---")
    record_type = input("Enter 'd' for a normal dictionary record, or 's' to pass a raw string (to test TypeError): ").strip().lower()
        
    if record_type == 's':
      raw_string = input("Enter the raw string text: ")
      records.append(raw_string)
    else:
      print("Leave a field blank to test missing key (KeyError)")
      name = input("Enter Name: ").strip()
      age = input("Enter Age (e.g., 25 or 'abc' to test ValueError): ").strip()
      score = input("Enter Score (e.g., 88.5): ").strip()      
      record_dict = {}
      if name: 
        record_dict["name"] = name
      if age: 
         record_dict["age"] = age
      if score: 
         record_dict["score"] = score
                
      records.append(record_dict)
            
clean, errors = process_records(records)
print("\n[Output] Clean Records:")
print(clean)
print("\n[Output] Error Log:")
print(errors)
print("-" * 40)
try:
    process_strict(records)
except RuntimeError as e:
    print(f"[Output] Strict mode raised: RuntimeError: {e}")