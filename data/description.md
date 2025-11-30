# Mô tả cấu trúc dữ liệu en_ewt-ud-train.txt

## Mức toàn bộ file

| Tên trường | Kiểu dữ liệu | Mô tả ngắn |
|-----------|-------------|------------|
| `raw_text` | `string` | Toàn bộ nội dung file văn bản, gồm nhiều đoạn/bài viết tiếng Anh, xuống dòng, dấu câu, chữ số, ký tự đặc biệt, v.v. |

## Mức từng dòng/đoạn văn

Ở mức chi tiết hơn, có thể coi mỗi dòng (hoặc một nhóm dòng liên tiếp không bị ngăn cách bởi dòng trống) là một bản ghi văn bản:

| Tên trường | Kiểu dữ liệu | Mô tả ngắn |
|-----------|-------------|------------|
| `text` | `string` | Một câu hoặc đoạn văn tiếng Anh thô, chưa tách token, không có nhãn hay cột bổ sung; được dùng làm đầu vào cho các bước tokenization/vectorization. |

