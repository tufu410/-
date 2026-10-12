#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
next_timecodes.py — 由每镜时长（秒）生成连续、无缝的分镜时间码区间。

仅使用 Python 标准库。

三种喂数方式：
  1) 命令行参数：
       python next_timecodes.py 2.3 2.5 2.2
  2) 管道（每行一个时长，# 开头为注释）：
       python next_timecodes.py < durations.txt
  3) 指定文本文件：
       python next_timecodes.py --file durations.txt

可选：
  --hours        强制使用 HH:MM:SS.s 格式（默认总时长 >=1 小时才用）
  --sep -        指定起止分隔符（默认 -）

输出每行：镜N｜START-END，可直接拼到分镜表头。
"""

import sys
import argparse


def parse_durations(args):
    values = []
    if args.file:
        with open(args.file, "r", encoding="utf-8") as fh:
            lines = fh.readlines()
    elif args.durations:
        lines = args.durations
    else:
        lines = sys.stdin.readlines()

    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        try:
            d = float(line)
        except ValueError:
            raise SystemExit(f"无法解析的时长: {raw!r}（应为秒数，如 2.5）")
        if d <= 0:
            raise SystemExit(f"时长必须为正数: {raw!r}")
        values.append(d)

    if not values:
        raise SystemExit("没有读到任何镜头时长。")
    return values


def format_time(seconds, force_hours):
    if seconds < 0:
        seconds = 0.0
    use_hours = force_hours or seconds >= 3600
    # 四舍五入到 0.1 秒，避免浮点尾巴
    total_tenths = int(round(seconds * 10))
    hours, rem = divmod(total_tenths, 36000)
    minutes, rem = divmod(rem, 600)
    secs_tenths = rem
    secs = secs_tenths // 10
    tenths = secs_tenths % 10
    if use_hours:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}.{tenths}"
    return f"{minutes:02d}:{secs:02d}.{tenths}"


def main():
    ap = argparse.ArgumentParser(description="生成连续分镜时间码")
    ap.add_argument("durations", nargs="*", help="每镜时长（秒）")
    ap.add_argument("--file", help="从文本文件读取时长（每行一个）")
    ap.add_argument("--hours", action="store_true", help="强制 HH:MM:SS.s")
    ap.add_argument("--sep", default="-", help="起止分隔符，默认 -")
    args = ap.parse_args()

    durations = parse_durations(args)

    cursor = 0.0
    for i, d in enumerate(durations, start=1):
        start = cursor
        end = cursor + d
        print(f"镜{i}｜{format_time(start, args.hours)}{args.sep}{format_time(end, args.hours)}")
        cursor = end

    print(f"# 共 {len(durations)} 镜，总时长 {format_time(cursor, args.hours)}", file=sys.stderr)


if __name__ == "__main__":
    main()
