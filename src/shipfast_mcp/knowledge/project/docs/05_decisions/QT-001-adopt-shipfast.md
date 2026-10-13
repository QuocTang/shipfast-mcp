# QT-001 — Áp dụng quy trình shipfast

| Mục | Giá trị |
|---|---|
| Loại | Quy trình |
| Trạng thái | Hiệu lực |
| Ngày | {{NGAY}} |
| Người chốt | PO |
| Đợt | — |
| Thay thế cho | — |

## Bối cảnh

Dự án cần một cách làm việc thống nhất giữa PO và agent: ai quyết, việc đi qua những bước nào, trạng thái ghi ở đâu.

## Quyết định

Dựng khung từ shipfast {{PHIEN_BAN}}: vai trò PO, Điều hành, agent; đợt 7 bước; ba chế độ chốt (PO chốt mặc định, chốt thẳng, uỷ quyền chưa bật); tranh luận tham vấn bằng vai phản biện; bảng đợt; backlog; sổ quyết định; từ vựng; cơ chế bộ phận và team thi công (chưa lập); phát hành; báo cáo.

## Hệ quả

- Mọi việc có code đi qua đợt (`docs/04_waves/README.md`), trừ hotfix và việc PO giao trực tiếp (`PO-nn`).
- Khung nâng cấp bằng tool `upgrade` của MCP shipfast; thư mục `.shipfast/` được commit và không sửa tay.
