狀態：DRAFT
版本：v0.1
最後更新：2026-05-20
適用範圍：Phase A.0F alpha 前端 scaffold 啟動說明
優先級：高

# 前端啟動說明

## 啟動 3 步

```bash
cd D:/劇本開發工具/_tools/frontend
pip install -r requirements.txt
python server.py --port 8765
```

預期 output：

```text
> Serving from D:/劇本開發工具
> Open browser: http://127.0.0.1:8765
> Press Ctrl-C to stop
```

瀏覽器開啟：

```text
http://127.0.0.1:8765
```

結束方式：在啟動 server 的 terminal 按 `Ctrl-C`。

## 故障排除

- Port 衝突：改用 `python server.py --port 8766`。
- Python 版本錯誤：確認目前 terminal 的 `python --version` 可使用 FastAPI / uvicorn。
- pip install 失敗：先確認網路與 Python 環境，再重跑 `pip install -r requirements.txt`。
- 瀏覽器無法開啟：確認 server output 仍在執行，且網址使用 `127.0.0.1` 或啟動時指定的 `--host`。

## 雙視窗工作流

前端只作為本地 viewer / editor scaffold。Codex、Claude Code、Cowork 或其他 agent 操作維持在另一個視窗執行；前端不啟動 export、skill subprocess 或 QA run。

## Git workflow

前端 Save / adapter 後續實作仍需手動檢查 diff，並由使用者手動 commit。Phase A.0F.0 只建立可啟動的 scaffold，不寫入 export 結果，也不修改 LOCKED spec。

## 對齊文件

- `_design/SPEC.md`
- `_design/UX_SPEC.md` §11
- `_design/ARCHITECTURE.md` §13
