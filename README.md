# Lab 1 + Lab 2: Tokenization and Count Vectorization

## Tổng Quan

Dự án này triển khai các thành phần tiền xử lý văn bản cơ bản cho Xử Lý Ngôn Ngữ Tự Nhiên (NLP) bằng Python, tập trung vào tokenization (phân đoạn từ) và vector hóa đếm (count vectorization). Dự án tái sử dụng giao diện Tokenizer từ Lab 1 và mở rộng với giao diện Vectorizer trong Lab 2. Các triển khai bao gồm hai tokenizer tùy chỉnh (SimpleTokenizer và RegexTokenizer) và một CountVectorizer để chuyển đổi tài liệu văn bản thành vector đếm theo mô hình Bag-of-Words.

## Cấu trúc code

- src/core/interfaces.py: Lớp cơ sở trừu tượng cho Tokenizer và Vectorizer.
- src/preprocessing/simple_tokenizer.py: Tokenizer dựa trên quy tắc đơn giản.
- src/preprocessing/regex_tokenizer.py: Tokenizer dựa trên biểu thức chính quy (regex).
- src/representations/count_vectorizer.py: Triển khai CountVectorizer.
- src/core/dataset_loaders.py: Tiện ích để tải dữ liệu văn bản thô.
- main.py: Script chính để kiểm tra tokenizer và vectorizer.
- test/lab2_test.py: Kiểm tra đơn vị cho CountVectorizer với corpus mẫu.
- test/lab2_countvectorizer_test.py: Kiểm tra vectorization trên tập dữ liệu UD English-EWT.
