**File**: DESIGN.md
***Developer**: Nalin Yetukuri
**Date**: 9/24/2024

## MY SPLIT

- Define a method `my_split` with one parameter.
- The parameter of the method is `self` of datatype class object `Sentence`.
- Define an accumulator variable `word`.
- Assign an empty list to the accumulator variable `word`.
- Initialize the instance of the attribute `self.words` to an empty list.
- Use the `for loop` to iterate through the string `self.sentence`
- Check every item in `self.sentence` to see if is a blank space or not.
-If the item is not a blank space add the item to the list(accumulator variable) `word`.
- Else check if the list `word` is not empty, use `.join()` to join the characters in the list to form a word (string) and append that word into the list 'self.words' using `.append`.
- Now assign an empty string to the list `word`.
- Come out of the `for loop`.
Check if there are items in the list `word`(in case the sentence is ending without a blank space).
- If there are items join the items in the list `word` and append that list to `self.words`.
- Return `self.words`.