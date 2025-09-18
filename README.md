# Lab 1 + Lab 2: Tokenization and Count Vectorization

## Tổng Quan

Dự án này triển khai các thành phần tiền xử lý văn bản cơ bản cho Xử Lý Ngôn Ngữ Tự Nhiên (NLP) bằng Python, tập trung vào tokenization (phân đoạn từ) và vector hóa đếm (count vectorization). Dự án tái sử dụng giao diện Tokenizer từ Lab 1 và mở rộng với giao diện Vectorizer trong Lab 2. Các triển khai bao gồm hai tokenizer tùy chỉnh (SimpleTokenizer và RegexTokenizer) và một CountVectorizer để chuyển đổi tài liệu văn bản thành vector đếm theo mô hình Bag-of-Words.

## Mục lục

- Cấu trúc dự án
- Các bước triển khai
- Cách chạy code và ghi log kết quả
- Giải thích các kết quả thu được
- Các khó khăn gặp phải và cách giải quyết

### Cấu trúc dự án

lab1_22001661_VuongSyViet/
├── data/
│ └── en_ewt-ud-train.txt # Dataset huấn luyện UD English-EWT
├── src/
│ ├── core/
│ │ ├── dataset_loaders.py # Tiện ích tải dataset
│ │ └── interfaces.py # Các lớp cơ sở trừu tượng
│ ├── preprocessing/
│ │ ├── simple_tokenizer.py # Tokenization cơ bản
│ │ └── regex_tokenizer.py # Tokenization dựa trên Regex
│ └── representations/
│ └── count_vectorizer.py # Count vectorization
├── test/
│ ├── **init**.py
│ ├── lab1_test.py # Test SimpleTokenizer
│ └── lab2_test.py # Test CountVectorizer
├── main.py # Script demo chính
└── README.md # Tài liệu hướng dẫn

### Các bước triển khai

**Bước 1: Thiết kế kiến trúc**

1. Phân tích yêu cầu: Xác định cần tokenization và vectorization
2. Thiết kế interface: Tạo abstract base classes cho Tokenizer và Vectorizer
3. Lập kế hoạch module: Tổ chức code theo cấu trúc rõ ràng

**Bước 2: Triển khai Core Interfaces**

# src/core/interfaces.py

- Định nghĩa abstract class Tokenizer với method tokenize()
- Định nghĩa abstract class Vectorizer với methods fit(), transform(), fit_transform()

**Bước 3: Triển khai Tokenizers**

# src/preprocessing/simple_tokenizer.py

- Kế thừa từ Tokenizer interface
- Triển khai logic tokenization cơ bản

# src/preprocessing/regex_tokenizer.py

- Kế thừa từ Tokenizer interface
- Sử dụng regex pattern để tokenize

**Bước 4: Triển khai Vectorizer**

# src/representations/count_vectorizer.py

- Kế thừa từ Vectorizer interface
- Triển khai bag-of-words representation
- Tích hợp với tokenizer

**Bước 5: Tạo Dataset Loader**

# src/core/dataset_loaders.py

- Triển khai function load_raw_text_data()
- Xử lý exception và error handling

**Bước 6: Testing và Validation**

# test/lab1_test.py, test/lab2_test.py, main.py

- Tạo test cases cho từng component
- Validation với dataset thực tế

### Cách chạy code và ghi log kết quả

**Chạy toàn bộ demo:** python main.py
**Chạy test riêng lẻ:**

- Test SimpleTokenizer: python -m test.lab1_test
- Test CountVectorizer: python -m test.lab2_test

### Ghi log kết quả chi tiết:

**File main.py sẽ xuất ra các log sau:**

=== Testing with Sample Sentences ===

--- SimpleTokenizer ---
Input: Hello, world! This is a test.
Tokens: ['hello', ',', 'world', '!', 'this', 'is', 'a', 'test', '.']

Input: NLP is fascinating... isn't it?
Tokens: ['nlp', 'is', 'fascinating', '.', '.', '.', 'isn', "'", 't', 'it', '?']

Input: Let's see how it handles 123 numbers and punctuation!
Tokens: ['let', "'", 's', 'see', 'how', 'it', 'handles', '123', 'numbers', 'and', 'punctuation', '!']

--- RegexTokenizer ---
Input: Hello, world! This is a test.
Tokens: ['hello', ',', 'world', '!', 'this', 'is', 'a', 'test', '.']

Input: NLP is fascinating... isn't it?
Tokens: ['nlp', 'is', 'fascinating', '.', '.', '.', 'isn', "'", 't', 'it', '?']

Input: Let's see how it handles 123 numbers and punctuation!
Tokens: ['let', "'", 's', 'see', 'how', 'it', 'handles', '123', 'numbers', 'and', 'punctuation', '!']

=== Testing Tokenization with UD_English-EWT Dataset ===
Original sample (first 100 chars): Al-Zaman : American forces killed Shaikh Abdullah al-Ani, the preacher at the
mosque in the town of ...

--- SimpleTokenizer Output (first 20 tokens): ['al', '-', 'zaman', ':', 'american', 'forces', 'killed', 'shaikh', 'abdullah', 'al', '-', 'ani', ',', 'the', 'preacher', 'at', 'the', 'mosque', 'in', 'the']

--- RegexTokenizer Output (first 20 tokens): ['al', '-', 'zaman', ':', 'american', 'forces', 'killed', 'shaikh', 'abdullah', 'al', '-', 'ani', ',', 'the', 'preacher', 'at', 'the', 'mosque', 'in', 'the']

=== Testing CountVectorizer with UD_English-EWT Dataset ===
Original sample (first 100 chars): Al-Zaman : American forces killed Shaikh Abdullah al-Ani, the preacher at the
mosque in the town of ...

--- SimpleTokenizer ---
Learned Vocabulary: {'!': 0, ',': 1, '-': 2, '.': 3, '2': 4, '3': 5, ':': 6, '[': 7, ']': 8, 'a': 9, 'abdullah': 10, 'al': 11, 'american': 12, 'ani': 13, 'announced': 14, 'at': 15, 'authorities': 16, 'baghdad': 17, 'be': 18, 'being': 19, 'border': 20, 'busted': 21, 'by': 22, 'causing': 23, 'cells': 24, 'cleric': 25, 'come': 26, 'dpa': 27, 'edgar': 28, 'employ': 29, 'equivalent': 30, 'fbi': 31, 'for': 32, 'forces': 33, 'h': 34, 'had': 35, 'having': 36, 'hoover': 37, 'in': 38, 'interior': 39, 'iraq': 40, 'iraqi': 41, 'is': 42, 'j': 43, 'killed': 44, 'killing': 45, 'like': 46, 'ministry': 47, 'moi': 48, 'mosque': 49, 'near': 50, 'of': 51, 'officials': 52, 'operating': 53, 'preacher': 54, 'qaim': 55, 'respected': 56, 'run': 57, 'shaikh': 58, 'so': 59, 'syrian': 60, 'terrorist': 61, 'that': 62, 'the': 63, 'them': 64, 'they': 65, 'this': 66, 'to': 67, 'town': 68, 'trouble': 69, 'two': 70, 'unwittingly': 71, 'up': 72, 'us': 73, 'were': 74, 'will': 75, 'would': 76, 'years': 77, 'zaman': 78}
Document-Term Vector (first 20 tokens): [1, 3, 2, 4, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1]

--- RegexTokenizer ---
Learned Vocabulary: {'!': 0, ',': 1, '-': 2, '.': 3, '2': 4, '3': 5, ':': 6, '[': 7, ']': 8, 'a': 9, 'abdullah': 10, 'al': 11, 'american': 12, 'ani': 13, 'announced': 14, 'at': 15, 'authorities': 16, 'baghdad': 17, 'be': 18, 'being': 19, 'border': 20, 'busted': 21, 'by': 22, 'causing': 23, 'cells': 24, 'cleric': 25, 'come': 26, 'dpa': 27, 'edgar': 28, 'employ': 29, 'equivalent': 30, 'fbi': 31, 'for': 32, 'forces': 33, 'h': 34, 'had': 35, 'having': 36, 'hoover': 37, 'in': 38, 'interior': 39, 'iraq': 40, 'iraqi': 41, 'is': 42, 'j': 43, 'killed': 44, 'killing': 45, 'like': 46, 'ministry': 47, 'moi': 48, 'mosque': 49, 'near': 50, 'of': 51, 'officials': 52, 'operating': 53, 'preacher': 54, 'qaim': 55, 'respected': 56, 'run': 57, 'shaikh': 58, 'so': 59, 'syrian': 60, 'terrorist': 61, 'that': 62, 'the': 63, 'them': 64, 'they': 65, 'this': 66, 'to': 67, 'town': 68, 'trouble': 69, 'two': 70, 'unwittingly': 71, 'up': 72, 'us': 73, 'were': 74, 'will': 75, 'would': 76, 'years': 77, 'zaman': 78}
Document-Term Vector (first 20 tokens): [1, 3, 2, 4, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1]

**File lab1_test.py sẽ xuất ra các log sau:**
['hello', ',', 'world', '!']

**File lab2_test.py sẽ xuất ra các log sau:**
Learned Vocabulary: {'.': 0, 'a': 1, 'ai': 2, 'i': 3, 'is': 4, 'love': 5, 'nlp': 6, 'of': 7, 'programming': 8, 'subfield': 9}
Document-Term Matrix (Count Vectors):
Document 1: [1, 0, 0, 1, 0, 1, 1, 0, 0, 0]
Document 2: [1, 0, 0, 1, 0, 1, 0, 0, 1, 0]
Document 3: [1, 1, 1, 0, 1, 0, 1, 1, 0, 1]

## Giải thích các kết quả thu được

1. **Tokenization Câu Mẫu**

- SimpleTokenizer: Tách theo khoảng trắng, phân tách dấu câu (ví dụ: "Hello, world! This is a test." → ['hello', ',', 'world', '!', 'this', 'is', 'a', 'test', '.']).
- RegexTokenizer: Trích xuất từ và dấu câu riêng (ví dụ: "Hello, world! This is a test." → ['hello', ',', 'world', '!', 'this', 'is', 'a', 'test', '.']).

2. **Tokenization UD English-EWT**

- Mẫu (100 ký tự đầu): Văn bản thô "American forces killed Shaikh Abdullah al-Ani, the preacher at the
  mosque in the town of ..."
- SimpleTokenizer: 20 token đầu:['al', '-', 'zaman', ':', 'american', 'forces', 'killed', 'shaikh', 'abdullah', 'al', '-', 'ani', ',', 'the', 'preacher', 'at', 'the', 'mosque', 'in', 'the']
- RegexTokenizer: Tương tự

3. **CountVectorizer UD English-EWT**
