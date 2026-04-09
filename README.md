# BookBot 📚

BookBot is a Python CLI tool that analyzes text files (books) and provides useful statistics like word count, character frequency, and most common words.

---

## 🚀 Features

* 📊 Total word count
* 🔤 Character frequency (a-z)
* 🔝 Top N most frequent words
* 📁 Export results to JSON

---

## 📂 Project Structure

```
bookbot/
│── books/
│── main.py
│── stats.py
│── README.md
```

---

## ⚙️ How to Run

```bash
python main.py <path_to_book>
```

### Example:

```bash
python main.py books/frankenstein.txt
```

---

## 🔧 Optional Arguments

### Show top N words

```bash
python main.py books/frankenstein.txt --top 20
```

### Export report to JSON

```bash
python main.py books/frankenstein.txt --export
```

### Combine both

```bash
python main.py books/frankenstein.txt --top 15 --export
```

---

## 📤 Output Example

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...

----------- Word Count ----------
Found 78321 total words

--------- Character Count -------
a: 4567
b: 1234
...

--------- Top Words -------
the: 5000
and: 4000
...

============= END ===============
```

---

## 📁 JSON Output (report.json)

```json
{
  "word_count": 78321,
  "top_words": [
    ["the", 5000],
    ["and", 4000]
  ]
}
```

---

## 🛠️ Tech Used

* Python 3
* Standard Library (sys, json, string)

---

## 💡 Future Improvements

* Add stop-word filtering (ignore "the", "and", etc.)
* Add GUI or web interface
* Add unit tests
* Support multiple file formats

---

## 👨‍💻 Author

Raaghav
