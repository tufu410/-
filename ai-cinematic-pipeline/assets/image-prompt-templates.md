# 图像提示词可复制模板（Image Prompt Templates）

> 角色三面板模板见 `assets/character-kit-template.md`。本文件汇总场景、道具、编辑、纹理修复、反打的成稿模板。方法与检查清单见 `references/10-image-prompts.md`。所有提示词正文用英文；画幅/分辨率/Soul ID 在平台 UI 设置，不写进正文。

---

## 1. 场景 / 定场静帧（Soul Cinema，21:9 / 16:9，2k）

```text
[机位锚定，最重要，写得明确直白：如 high angle three-quarter wide shot, camera high above the room looking diagonally down at a 45 degree angle]. [场景身份与核心空间].
[关键建筑/自然景物，材质与表面处理：如 board-formed concrete, oxidized copper verdigris]. [光源 + 方向 + 色温：如 soft morning key light from the floor-to-ceiling windows on the right, gentle fill, 2:1 ratio, smooth falloff].
[远景元素向画面深处延伸，前景/中景/后景层次]. [色调：如 palette of 60% warm ochre, 30% deep charcoal, 10% rust-red]. [技术参数块].
[氛围/摄影师参考，点到为止].
[需要空旷则正向描述：empty deserted interior, bare walls, still air]. [rule of thirds].
```

技术块二选一：
- 胶片：`Photorealistic ARRI Alexa LF anamorphic Cooke S4 lens at T2.0, organic 35mm Kodak Vision3 250D film grain, soft cinematic falloff, cinematic film still aesthetic`
- 干净数字：`Shot on ARRI Alexa Mini LF with ARRI Signature Prime lens, clean modern digital cinematic capture, crisp natural detail, minimal fine grain, soft cinematic falloff, hyperrealistic photographic detail`

提醒：机位用直白物理描述（慎用鱼眼/监控等抽象术语）；景深/光学参数留给人物镜头、不写进场景；Soul Cinema 自带颗粒，技术块一行即可；不堆否定词。

## 2. 道具 / 产品设定表（NBP / GPT Image 2，1:1，高道具 3:4，2k–4k）

```text
Photorealistic [top-down / three-quarter overhead] product shot of [道具] on a [neutral grey concrete / matte stone] surface, [soft directional lighting, gentle 2:1 ratio, smooth falloff], isolated subject.
[道具具体描述：材质、表面处理、磨损/新旧状态]. plain unbranded surfaces, blank matte finish, no logos, no readable text.
[技术参数块]. rule of thirds.
```

- 不同状态（完好 / 破损 / 沾染血迹）拆成独立资产分别生成。
- 危险类道具规避敏感词，只描述材质与功能。
- 物体上需要文字时：引号写完整原文 + 字体/字重/颜色（`Write 'GENUINE' in bold red serif on the sign`）。

## 3. 图片编辑（NBP 首选；最小 CHANGE，详尽 PRESERVE，一次只改一处）

```text
Edit the image: [一行写编辑目标].
CHANGE: [仅写需要修改的一项，描述精准].
PRESERVE EXACTLY:
- [列出所有必须原样保留：人脸、发型、服装、配饰、道具、物体位置、墙面地面、机位角度、原有全部阴影与反光]
- Color grade, palette, contrast, grain, falloff, lens character
ONLY CHANGE: [再次重申唯一改动项]. 100% identical otherwise.
```

- 移除某物体时必须写明空缺填充：`Remove the lamppost, fill the gap with the continuous brick wall behind it.`
- 用户反馈改动过大 = CHANGE 写多了，应少改、多锁。
- 禁止用编辑功能整张重绘；需要重绘交 Soul 系列。

## 4. AI 纹理糊块修复（Seedream，仅纹理，禁定点编辑）

```text
Restore the collapsed AI-generated texture only: refine realistic [skin pores / fabric weave / surface patina and wear] across [指定表面], bringing back natural micro-detail and correct material response.
PRESERVE EXACTLY: composition, framing, facial identity, facial features, pose, wardrobe, props, lighting direction, color grade, contrast, grain.
Texture restoration only; do not relocate, reshape, add or remove any object, and do not perform localized spot edits.
```

## 5. 极小范围精细局部修改（GPT Image 2，终极备选）

- 沿用第 3 节精准编辑模板，CHANGE 范围尽可能窄（该模型会轻微污染整张画面，PRESERVE 要写得比 NBP 更完整）。

## 6. 换机位 / 反打视角（默认 GPT Image 2）

- 必须逐个写明物体镜像后的新位置，否则空间错乱：
```text
Re-render the same room from the reverse angle, shot from behind where the sofa was.
New positions: the sofa, previously on the right, now sits on the left; the doorway that was behind the camera now appears in the foreground; the floor lamp moves from frame-left to frame-right. Keep identical furniture, materials, lighting direction, color grade and time of day.
```
- 若坚持用 NBP 做反打，同样必须写全所有物体新摆放位置。

---

## 通用固定规则速记

- 除角色设定表外，图像/视频提示词加 `rule of thirds`。
- 无负面提示词参数：正向描述想要的效果（干净皮肤 `clean dry skin`、空旷 `empty deserted street, bare walls, still air`、无 logo `plain unbranded wrapper, blank matte surface`）。
- 色调 60/30/10，配比取自用户/参考图，不擅自改。
- 防插画跑偏：加胶片型号、镜头、真实材质、`cinematic film still` / `studio photographs` / `film character sheet`，不写 `painterly`、`character reference sheet`。
- 控制长度：约 80–150 词、字符 ≤1500–2000，删无效修饰。
- 视频提示词同样“写动作状态之中、不写完整过渡”，完整视频规则见 `references/40-director-build.md` 至 `references/43-director-qc.md`。
