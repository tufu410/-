#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_storyboard.py — 校验分镜文本的镜号连续性与时间码咬合。

仅使用 Python 标准库。

用法：
  python validate_storyboard.py storyboard.md
  type storyboard.md | python validate_storyboard.py

它会从文本中抓取形如下面的表头：
  镜1｜00:00.0-00:02.3｜景别｜运镜
  镜2｜00:02.3-00:04.8｜...
支持的起止分隔符：- – — ~ 至；时间码支持 MM:SS.s 与 HH:MM:SS.s。

检查项：
  1) 镜号是否从 1 连续、无重复无跳号；
  2) 每镜结束时间是否晚于开始时间；
  3) 相邻镜是否无缝（前一镜结束 == 后一镜开始，容差 0.05 秒）；
  4) 报告镜头总数与总时长。
退出码：全部通过为 0，发现问题为 1。
"""

import re
import sys

SHOT_RE = re.compile(
    r"镜\s*(\d+)\s*[｜|]\s*"
    r"(\d{1,2}:\d{2}(?::\d{2})?(?:\.\d+)?)"
    r"\s*[-–—~至]+\s*"
    r"(\d{1,2}:\d{2}(?::\d{2})?(?:\.\d+)?)"
)

TOLERANCE = 0.05


def parse_timecode(text):
    parts = text.split(":")
    nums = [float(p) for p in parts]
    if len(nums) == 2:
        m, s = nums
        return m * 60 + s
    if len(nums) == 3:
        h, m, s = nums
        return h * 3600 + m * 60 + s
    raise ValueError(f"无法解析时间码: {text}")


def collect_shots(text):
    shots = []
    for match in SHOT_RE.finditer(text):
        num = int(match.group(1))
        start = parse_timecode(match.group(2))
        end = parse_timecode(match.group(3))
        shots.append((num, start, end))
    return shots


def fmt(seconds):
    total_tenths = int(round(seconds * 10))
    hours, rem = divmod(total_tenths, 36000)
    minutes, rem = divmod(rem, 600)
    secs = rem // 10
    tenths = rem % 10
    if hours:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}.{tenths}"
    return f"{minutes:02d}:{secs:02d}.{tenths}"


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as fh:
            text = fh.read()
    else:
        text = sys.stdin.read()

    shots = collect_shots(text)
    if not shots:
        print("未在文本中找到任何 '镜N｜START-END' 表头。")
        return 1

    problems = []

    # 1) 镜号连续
    nums = [n for n, _, _ in shots]
    expected = list(range(1, len(shots) + 1))
    if nums != expected:
        seen = set()
        dup = sorted({n for n in nums if n in seen or seen.add(n)})
        if dup:
            problems.append(f"镜号重复: {dup}")
        missing = [n for n in expected if n not in nums]
        if missing:
            problems.append(f"镜号跳号/缺失: {missing}")
        extra = [n for n in nums if n not in expected]
        if extra:
            problems.append(f"存在超出 1..{len(shots)} 的镜号: {extra}")

    # 2) 每镜 end > start
    for n, s, e in shots:
        if e <= s:
            problems.append(f"镜{n} 结束时间({fmt(e)})不晚于开始时间({fmt(s)})")

    # 3) 相邻无缝
    for (n1, _, e1), (n2, s2, _) in zip(shots, shots[1:]):
        if abs(e1 - s2) > TOLERANCE:
            if s2 > e1:
                problems.append(f"时间码断档：镜{n1} 结束 {fmt(e1)}，镜{n2} 才开始 {fmt(s2)}（缺口 {fmt(s2 - e1)}）")
            else:
                problems.append(f"时间码重叠：镜{n1} 结束 {fmt(e1)}，镜{n2} 从 {fmt(s2)} 开始")

    print(f"识别到 {len(shots)} 个镜头，总时长 {fmt(shots[-1][2])}。")
    if problems:
        print(f"发现 {len(problems)} 个问题：")
        for p in problems:
            print(f"  - {p}")
        return 1

    print("校验通过：镜号连续，时间码无缝咬合。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
