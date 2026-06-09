"""
## 2. Safe List Access  *(Easy)*

=================================================
SAFE LIST ACCESS
=================================================

Problem Statement:
Write a Python FUNCTION called `safe_get`
that takes a list and an index, and returns
the value at that index WITHOUT crashing the
program when the index is invalid.

The function must return a TUPLE:
        (status, value_or_message)
   - status -> "ok" or "error"
   - value_or_message -> the value on success,
                         or an error string on
                         failure.

Handle these error cases:
   - IndexError      -> "Index out of range"
   - TypeError       -> "Index must be an int"
   - other Exception -> "Unexpected error: ..."

-------------------------------------------------
Instructions:
1. Define a function:
      def safe_get(items, index):
2. Use a try block that returns items[index].
3. Add a separate `except` block for each
   expected exception in the correct order
   (most specific first).
4. Add a final `except Exception as e:` block
   that includes str(e) in the error message.
5. Do NOT use:
   - the `in` operator to guess validity
     beforehand
   - if-checks like `if 0 <= index < len(items)`
     to AVOID the exception.
   The whole point is to LET the exception be
   raised and HANDLE it.

-------------------------------------------------
Debugging Skills to Practice:
- Use print(repr(index), type(index)) when the
  function misbehaves; `repr` shows quotes
  around strings so you can tell "3" from 3.
- Read the exception MESSAGE — IndexError on a
  list of length 5 tells you the index that
  was rejected.
- Try `import traceback; traceback.print_exc()`
  inside the except block to print the full
  traceback while still handling the error.

-------------------------------------------------
Input Example 1:
safe_get([10, 20, 30, 40], 2)

Output Example 1:
('ok', 30)

-------------------------------------------------
Input Example 2:
safe_get([10, 20, 30], 7)

Output Example 2:
('error', 'Index out of range')

-------------------------------------------------
Input Example 3:
safe_get([10, 20, 30], "1")

Output Example 3:
('error', 'Index must be an int')

=================================================

"""
def safe_get(items, index):
    try:
        result = items[index]
        return ("ok", result)
        
    except IndexError:
        return ("error", "Index out of range")
        
    except TypeError:
        return ("error", "Index must be an int")
        
    except Exception as e:
        return ("error", f"Unexpected error: {str(e)}")

list1= input("Enter list elements separated by commas: ").split(",")
for i in range(len(list1)):
    if list1[i].isdigit():
       list1[i] = int(list1[i])
print(f"Current list parsed as: {list1}")
raw_index = input("Enter an index to look up (or a string like 'one' to trigger TypeError): ")
if raw_index.isdigit():
   final_index = int(raw_index)
else:
  final_index = raw_index  
        
print("\nExecuting safe_get...")
output = safe_get(list1, final_index)
print(f"Output Tuple: {output}")
