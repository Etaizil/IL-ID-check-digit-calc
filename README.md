# IL ID Check Digit

This repository calculates the check digit for Israeli ID numbers. I added a small minimalist web UI served by a lightweight Flask app.

Quick start (Windows PowerShell):

```powershell
# create and activate virtualenv (optional but recommended)
python -m venv .venv; .\.venv\Scripts\Activate.ps1

# install dependencies
pip install -r requirements.txt

# run the server
python .\src\app.py
```

Open http://127.0.0.1:5000 in your browser.

Notes:
- The UI lives in the `ui/` folder (static files).
- The Flask server is `src/app.py` and exposes POST `/api/checkdigit` which accepts JSON `{ "id_number": "..." }` and returns `{ "ok": true, "check_digit": <n> }`.
- The server also serves `index.html`, CSS and JS from the `ui/` folder.

The calculation for a correct check digit is as follows
----------------------------------------------------

1. Start with the ID number as digits only. The code accepts either 8 or 9 digits. If a 9-digit value is provided, the last digit is treated as an existing check digit and is ignored for the calculation.
2. Process the remaining 8 digits from left to right. Multiply the digits alternately by 1 and 2, starting with 1 for the left-most digit. That produces a sequence of products: 1×d1, 2×d2, 1×d3, 2×d4, …
3. For any product greater than 9, subtract 9 from it. (This is equivalent to summing the digits of the product for two-digit results.)
4. Sum all the adjusted products to a single total.
5. The check digit is the amount that must be added to the total to reach the next multiple of 10. In formula form:

	check_digit = (10 - (total % 10)) % 10

Worked example (ID: 12345678)

- Digits: 1 2 3 4 5 6 7 8
- Multiply (1,2 alternation): 1, 4, 3, 8, 5, 12, 7, 16
- Subtract 9 where >9: 1, 4, 3, 8, 5, 3, 7, 7
- Sum: 1+4+3+8+5+3+7+7 = 38
- Check digit: (10 - (38 % 10)) % 10 = (10 - 8) % 10 = 2

So the computed check digit for `12345678` is `2`.