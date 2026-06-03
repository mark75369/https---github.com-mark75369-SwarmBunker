狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：客製化 entity 類型 / QA 模組 / 作品專屬骨架 / 議題清單（D-047 後）  
優先級：中

# 07 客製化

工具支援 3 種既有客製化機制 + 1 種未來計畫客製化：

| 機制 | 客製什麼 | 狀態 |
|---|---|---|
| 1. entity_type_registry | 加新 entity 類型（如 I-* 物品 / 自訂 X-*）| ✅ 已 lock |
| 2. qa_type_registry | 加新 QA 模組（如自訂「驚悚密度」檢查）| ✅ 已 lock |
| 3. 00_b 作品專屬骨架 | 類型語氣 / 越界禁區 / 高風險場景處理 | ✅ 已 lock |
| 4. issue_type_registry | 自訂 /create-* 5 skill 議題清單 | ⏳ 計畫 D-047（Phase A.0 完成後）|

---

# 1. 自訂 entity 類型

對應 SPEC §5.1b + DATA_FORMAT_SPEC §7。

## 1.1 三層架構

```
core/（鎖定，不能動）— 11 種（鏡像；權威見 entity_type_registry）
  W-rules / W-language / W-style / V / C / R / P / CH / S / A / ORG
  ↑
reserved_prefixes/（預留前綴，user 不能用）
  I / UI / SKILL
  ↑
user_extensions/（你可以加）
  自訂 X-* 等
```

## 1.2 怎麼加新 entity 類型

編輯 Instance root 的 `entity_type_registry.yaml`：

```yaml
version: 1
schema_version: data_format_spec_v0.2

core:
  # 11 種 core entity（不能改；權威見 entity_type_registry）
  # ...

reserved_prefixes:
  - I       # 物品（v1.0 不採）
  - UI      # UI 文案（v1.0 不採）
  - SKILL   # 技能（v1.0 不採）

user_extensions:
  - type: ITEM
    description: 自訂物品實體
    id_pattern: ^ITEM-.+$
    target_dir: 11_items/   # 對應目錄要存在
    cross_ref_allowed: true
    locked: false
    
  - type: LOCATION
    description: 自訂地點實體
    id_pattern: ^LOC-.+$
    target_dir: 14_locations/
    cross_ref_allowed: true
    locked: false
```

## 1.3 限制

- ❌ 不能跟 core 11 種衝突（權威見 entity_type_registry）
- ❌ 不能用 `I` / `UI` / `SKILL` 三個 reserved prefix
- ❌ id_pattern 必須是 valid regex
- ❌ target_dir 必須存在

---

# 2. 自訂 QA 模組

對應 SPEC §5.2.4 + DATA_FORMAT_SPEC §8。

## 2.1 機制

```
core/（8 種必跑）
  AI_FLAVOR / VOICE_CONSISTENCY / FORBIDDEN_WORD / INFO_CONTROL /
  GENRE_DRIFT / RHYTHM / DRAMATIC_TENSION / CROSS_SCENE_CONTINUITY
  ↑
user_extensions/（你可以加）
  自訂 09_x_* 模板
```

## 2.2 怎麼加新 QA 模組

**Step 1：寫新 QA 模板** 

放在 `09_quality_assurance/09_x_<名稱>檢查模板.md`，依 00_p QA 擴充協議骨架。

**Step 2：註冊到 registry**

編輯 Instance root 的 `qa_type_registry.yaml`：

```yaml
core:
  - qa_type: AI_FLAVOR
    template_path: 09_quality_assurance/09_a_ai_flavor.md
    locked: true
  # ... 8 core qa_type

user_extensions:
  - qa_type: HORROR_DENSITY     # 自訂：恐怖密度檢查
    template_path: 09_quality_assurance/09_x_horror_density.md
    locked: false
    description: 恐怖類遊戲專用的驚悚密度曲線檢查
```

**Step 3：跑 /qa 時會自動含**

跑 `/qa` 預設**只跑 8 份 core**。要含 user_extensions 用：

```
/qa S-01-03 --include-user-qa
```

## 2.3 限制

- ✅ 可以加任意數量 user qa_type
- ✅ user qa_type 不影響 8 份 core 必跑邏輯
- ✅ FINAL gate 仍只看 9 種 status（8 core QA + 09_e）

---

# 3. 作品專屬 00_b 擴充

對應 SPEC §17。

`00_protocol/00_b_反AI味檢查表.md` 是**工具骨架**（Template 提供）。Instance bootstrap 時複製過來，**作品專屬部分**由 5 個 /create-* skill 自動補：

## 3.1 7 個固定 section anchors（鎖定順序）

```markdown
## 1. 作品類型語氣定位          ← /create-world 補
## 2. 髒話尺度與死亡處理偏好    ← /create-world 補
## 3. 規模定位                  ← /create-outline 補
## 4. 類型偏移風險清單          ← /create-outline 補
## 5. 角色偏移檢查清單          ← /create-character 補（每角色一個 ### 子節）
## 6. 高風險場景的處理方式      ← /create-detailed-outline 補（每場景類型一個 ### 子節）
## 7. 經驗累積的偏移案例        ← 你日常手動寫入
```

## 3.2 規則

- ❌ Section 順序不可改
- ❌ Section 名稱不可改
- ✅ Section 內容由 5 skill 自動補（user 可手動編輯）
- ✅ §7 經驗累積由 user 隨時加

## 3.3 衝突處理

如果你已手寫 §1 類型語氣，跑 /create-world 想補 §1，agent 會：
- 偵測現有 §1 內容
- 印 diff 給你
- 你選 merge / overwrite / skip

---

# 4. 議題清單客製化（D-047，未來）

⏳ **狀態：規劃中** — 對應 [`POST_LOCK_PENDING.md`](../_design/POST_LOCK_PENDING.md) §NEW_REQ_1

## 4.1 為什麼需要

目前 5 個 /create-* skill 的議題清單（11/9/6/7/7）**hardcode 在 UD §1.1-§1.5**。但不同類型遊戲需要不同議題：

- 純愛戀愛 → 不需要「越界禁區」議題
- 恐怖懸疑 → 需要加「驚悚密度曲線」議題
- 科幻 → 需要加「科技邏輯一致性」議題

## 4.2 預計機制（D-047）

```yaml
# issue_type_registry.yaml
core:
  00_e_world:
    - id: 1
      name: 世界類型快速分類
      required_level: REQUIRED
      locked: true
    # ... 11 個議題
  # ... 5 個 skill 對應的議題清單

user_extensions:
  00_e_extra:
    - id: 12
      name: 美術風格定位
      required_level: STRONGLY_PREFERRED
      question: "你想要寫實派 / 動漫派 / 像素派 / 其他風格？"
  00_f_extra:
    - id: 10
      name: 角色音調語速偏好
      required_level: OPTIONAL
      question: "這角色配音時偏好高 / 低音？快 / 慢？"

core_overrides:
  00_e_skip:
    - 6   # 純愛遊戲跳過議題 6 宗教
  00_f_skip:
    []
```

## 4.3 預計時間

| 時點 | 動作 |
|---|---|
| 現在 | 在 `POST_LOCK_PENDING.md` 紀錄為 NEW_REQ_1 |
| Phase A.0 9 個 parser sub-task 全完成 | 開新 master 第五輪整合 → 拍板 D-047 |
| Phase B 中 | 實作 /create-* skill 讀 registry |
| Phase A.0F 後 | 前端工具加 issue registry 編輯 UI |

---

# 5. 客製化建議流程

如果你想客製化任何東西，建議流程：

```
1. 先看本說明書 §1-§4 有沒有現成機制
   ↓ 有 → 直接用
   ↓ 沒有
2. 在 POST_LOCK_PENDING.md 加 NEW_REQ_N 紀錄
3. 等 Phase A.0+ 階段或開 master 第五輪整合對話拍板
4. 走 D-NNN 加入 spec 後再實作
```

**禁止：** 不要直接動 `_design/` 內 LOCKED 文件（會破壞工具升級相容性）。

---

# 6. 參考

- `_design/SPEC.md` §5.1 / §5.2.4 / §17 — 設計層權威
- `_design/DATA_FORMAT_SPEC.md` §7 / §8 — registry schema 完整定義
- `_design/POST_LOCK_PENDING.md` — 後續客製化需求紀錄
