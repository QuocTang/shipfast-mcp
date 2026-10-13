# QT-001 — Áp dụng quy trình shipfast

| Mục | Giá trị |
|---|---|
| Loại | Quy trình |
| Trạng thái | Hiệu lực |
| Ngày | {{NGAY}} |
| Người chốt | PO |
| Wave | — |
| Thay thế cho | — |

## Bối cảnh

Dự án cần một cách làm việc thống nhất giữa PO và agent: ai quyết, việc đi qua những bước nào, trạng thái ghi ở đâu.

## Quyết định

Scaffold từ shipfast {{PHIEN_BAN}}: vai trò PO, Orchestrator, agent; wave 7 bước; ba chế độ chốt (PO chốt mặc định, chốt thẳng, delegation chưa bật); debate tham vấn bằng vai phản biện; bảng wave; backlog; decision log; từ vựng; cơ chế bộ phận và build team (chưa lập); release; báo cáo.

## Hệ quả

- Mọi việc có code đi qua wave (`docs/04_waves/README.md`), trừ hotfix và việc PO giao trực tiếp (`PO-nn`).
- Khung nâng cấp bằng tool `upgrade` của MCP shipfast; thư mục `.shipfast/` được commit và không sửa tay.
