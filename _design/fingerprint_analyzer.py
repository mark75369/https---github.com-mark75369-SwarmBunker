"""
TSV 文風指紋量化分析
輸入：Script_Level_07/08/09 TSV
輸出：句長分佈 / 標點密度 / 角色高頻詞 / 旁白(括號)模式 / 三層敘事比例
"""
import re
import csv
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("/sessions/upbeat-modest-pasteur/mnt/game-script-A/台詞")
TSV_FILES = sorted(ROOT.glob("Script_Level_*_adjusted.tsv"))

CHAR_LABELS = {
    "MainCharacter": "清道夫",
    "MainGirlA": "瑟琳",
    "MainGirlB": "莉娜",
    "MainGirlC": "諾拉",
}

# 分類正則
RE_DIALOGUE = re.compile(r"[「『]([^」』]+)[」』]")
RE_NARR_BRACKET = re.compile(r"[（(]([^）)]+)[）)]")
# 中文標點
RE_PUNCT_SOFT = re.compile(r"[，、]")  # 軟停頓
RE_PUNCT_HARD = re.compile(r"[。！？]")  # 硬停頓
RE_PUNCT_ELLIPSIS = re.compile(r"…")
RE_PUNCT_DASH = re.compile(r"——|──|—")

def split_sentences(text):
    """以中文硬標點切句"""
    text = text.strip()
    if not text:
        return []
    sents = re.split(r"[。！？]+", text)
    return [s for s in sents if s.strip()]

def analyze_file(tsv_path):
    rows = []
    with open(tsv_path, "r", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f, delimiter="\t")
        try:
            for r in reader:
                rows.append(r)
        except UnicodeDecodeError as e:
            print(f"[warn] {tsv_path.name}: truncated at row ~{len(rows)} ({e})")
    return rows

def per_character_stats():
    stats = defaultdict(lambda: {
        "n_rows": 0,
        "dialogue_chars": 0,        # 「」內字數
        "narr_chars": 0,            # （）內字數
        "raw_chars": 0,
        "n_dialogue_sents": [],     # 對話句長
        "n_narr_sents": [],         # 旁白句長
        "punct_soft": 0,
        "punct_hard": 0,
        "punct_ellipsis": 0,
        "punct_dash": 0,
        "vocab": Counter(),
        "phrases": Counter(),       # 2-3 字片語
        "dialogue_full": [],        # 完整對話樣本
        "narr_full": [],            # 完整旁白樣本
    })

    for tsv in TSV_FILES:
        for r in analyze_file(tsv):
            label = r.get("角色", "").strip()
            text = r.get("台詞", "").strip()
            if not text or not label:
                continue
            name = CHAR_LABELS.get(label, label)
            s = stats[name]
            s["n_rows"] += 1
            s["raw_chars"] += len(text)

            dialogues = RE_DIALOGUE.findall(text)
            narrs = RE_NARR_BRACKET.findall(text)

            for d in dialogues:
                s["dialogue_chars"] += len(d)
                s["dialogue_full"].append(d)
                for sent in split_sentences(d):
                    s["n_dialogue_sents"].append(len(sent))
            for n in narrs:
                s["narr_chars"] += len(n)
                s["narr_full"].append(n)
                for sent in split_sentences(n):
                    s["n_narr_sents"].append(len(sent))

            s["punct_soft"] += len(RE_PUNCT_SOFT.findall(text))
            s["punct_hard"] += len(RE_PUNCT_HARD.findall(text))
            s["punct_ellipsis"] += len(RE_PUNCT_ELLIPSIS.findall(text))
            s["punct_dash"] += len(RE_PUNCT_DASH.findall(text))

            # 高頻詞：先剝掉「」（）符號，2-3 連字 n-gram
            clean = re.sub(r"[「」『』（）()，、。！？…—\s]", "", text)
            for ch in clean:
                s["vocab"][ch] += 1
            # 2-字 / 3-字 n-gram
            for i in range(len(clean) - 1):
                s["phrases"][clean[i:i+2]] += 1
            for i in range(len(clean) - 2):
                s["phrases"][clean[i:i+3]] += 1

    return stats

def summarize(stats):
    out = []
    out.append("=" * 70)
    out.append("文風指紋量化分析報告")
    out.append("=" * 70)
    out.append(f"資料來源：{', '.join(t.name for t in TSV_FILES)}")
    out.append(f"分析角色：{', '.join(CHAR_LABELS.values())}")
    out.append("")

    for name in ["清道夫", "瑟琳", "莉娜", "諾拉"]:
        s = stats.get(name)
        if not s or s["n_rows"] == 0:
            out.append(f"\n--- {name}：無資料 ---")
            continue
        out.append(f"\n--- {name} (label: {[k for k,v in CHAR_LABELS.items() if v==name][0]}) ---")
        out.append(f"行數：{s['n_rows']}")
        out.append(f"總字數：{s['raw_chars']}")
        out.append(f"對話「」字數：{s['dialogue_chars']}  ({s['dialogue_chars']*100//max(s['raw_chars'],1)}%)")
        out.append(f"旁白（）字數：{s['narr_chars']}  ({s['narr_chars']*100//max(s['raw_chars'],1)}%)")
        out.append(f"剩餘（無標記）：{s['raw_chars']-s['dialogue_chars']-s['narr_chars']}")

        if s["n_dialogue_sents"]:
            dlens = s["n_dialogue_sents"]
            out.append(f"對話句長：n={len(dlens)} mean={sum(dlens)/len(dlens):.1f} "
                      f"min={min(dlens)} max={max(dlens)} median={sorted(dlens)[len(dlens)//2]}")
            # 句長分佈 bucket
            buckets = Counter()
            for l in dlens:
                if l <= 5: buckets["<=5"] += 1
                elif l <= 10: buckets["6-10"] += 1
                elif l <= 20: buckets["11-20"] += 1
                elif l <= 35: buckets["21-35"] += 1
                else: buckets["36+"] += 1
            total = len(dlens)
            out.append("  分佈：" + "  ".join(f"{k}:{v}({v*100//total}%)" for k,v in sorted(buckets.items())))

        if s["n_narr_sents"]:
            nlens = s["n_narr_sents"]
            out.append(f"旁白句長：n={len(nlens)} mean={sum(nlens)/len(nlens):.1f} "
                      f"min={min(nlens)} max={max(nlens)}")

        out.append(f"標點：軟停={s['punct_soft']} 硬停={s['punct_hard']} 省略={s['punct_ellipsis']} 破折={s['punct_dash']}")

        # 高頻 2-3 字片語（去掉太普通的）
        common_skip = {"的", "了", "是", "我", "你", "他", "她", "在", "有", "不", "我們",
                       "你們", "他們", "她們", "這", "那", "個", "一個", "什麼", "可以"}
        meaningful = [(p, c) for p, c in s["phrases"].most_common(80)
                      if c >= 3 and not all(ch in common_skip for ch in [p[0]])]
        out.append(f"特徵詞（出現≥3 次）：")
        for p, c in meaningful[:25]:
            out.append(f"  {p}: {c}")

        # 樣本
        out.append("\n對話樣本（前 5）：")
        for d in s["dialogue_full"][:5]:
            out.append(f"  ｢{d[:60]}｣")
        out.append("旁白樣本（前 5）：")
        for n in s["narr_full"][:5]:
            out.append(f"  （{n[:60]}）")

    # 三層敘事比例（全局）
    out.append("\n" + "=" * 70)
    out.append("三層敘事結構（全角色合計）")
    out.append("=" * 70)
    total_dial = sum(s["dialogue_chars"] for s in stats.values())
    total_narr = sum(s["narr_chars"] for s in stats.values())
    total_raw = sum(s["raw_chars"] for s in stats.values())
    out.append(f"對話「」  ：{total_dial} ({total_dial*100//max(total_raw,1)}%)")
    out.append(f"旁白（）  ：{total_narr} ({total_narr*100//max(total_raw,1)}%)")
    out.append(f"其他      ：{total_raw - total_dial - total_narr}")

    # 男主角 「對話 vs 旁白」比例（這是 MC 的特殊性 — 同時負責兩層）
    mc = stats.get("清道夫", {})
    if mc.get("n_rows"):
        mc_total = mc["dialogue_chars"] + mc["narr_chars"]
        out.append(f"\n男主角 清道夫（同時負責對話+旁白）：")
        out.append(f"  對話佔：{mc['dialogue_chars']*100//max(mc_total,1)}%  旁白佔：{mc['narr_chars']*100//max(mc_total,1)}%")
        out.append(f"  → 旁白即「主角第一人稱視角描述」，第一人稱 OS 暗藏在這層")

    return "\n".join(out)

if __name__ == "__main__":
    stats = per_character_stats()
    report = summarize(stats)
    print(report)
    out_path = "/sessions/upbeat-modest-pasteur/mnt/outputs/fingerprint_report.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\n--> report written to {out_path}")
