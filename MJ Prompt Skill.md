# Midjourney Prompt Engineering Skill

> 一个经过大量实战验证的 Midjourney V8.2 提示词工程 Skill。输入任意主题或参考图，输出可直接复制使用的三件套：正向提示词、负面提示词、生成参数。

---

## 目录

- [核心铁律](#核心铁律)
- [提示词 9 段式结构](#提示词-9-段式结构)
- [参数决策表](#参数决策表)
- [用户偏好强化项](#用户偏好强化项)
- [高频词库](#高频词库)
- [负面词体系](#负面词体系)
- [主题适配速查](#主题适配速查)
- [参考图炼化流程](#参考图炼化流程)
- [迭代修改规则](#迭代修改规则)
- [质量检查清单](#质量检查清单)

---

## 核心铁律

1. **平台固定**：Midjourney `--v 8.2`，英文提示词，逗号分隔，权重从前到后递减。
2. **三件套输出**：正向提示词 + 负面提示词 + 生成参数。不写多余拆解，除非用户明确要求"分析/拆解"。
3. **新规划零污染**：除非用户明确说"承接上一条/在这个基础上改"，否则每次都是独立主题，不混入之前的色彩、角色、风格残留。
4. **合规规避**：不写任何版权 IP 名（高达、哥斯拉、复仇者、吉卜力等），用功能描述替代；不写违规词。
5. **参考图必读图**：用户上传图片要求"炼化"时，必须先读取图片，再逐元素拆解后出词，不凭猜测。
6. **迭代只改指定部分**：用户说"改一下XX"，只动那部分，其余保持不变，不重写全词。

---

## 提示词 9 段式结构

权重从前到后递减，每段用逗号分隔：

```
[1. 媒介/风格锚点] → [2. 主体/核心对象] → [3. 外形/服装/材质] → [4. 环境/背景] → [5. 光影设计] → [6. 色彩体系] → [7. 构图/镜头/视角] → [8. 质感/笔触/颗粒] → [9. 氛围/情绪]
```

| 段位 | 写什么 | 高频词 |
|---|---|---|
| 1 | 第一眼定风格，防跑偏 | `photorealistic, cinematic photography` / `digital painting` / `concept art` |
| 2 | 主体是谁/什么，姿态动作 | `a young king standing on terrace` / `a colossal mecha battling` |
| 3 | 服装、材质、配饰、身体细节 | `velvet mantle, gold crown, cracked lava skin` |
| 4 | 环境、建筑、天气、远景 | `castle terrace, distant mountains, misty forest` |
| 5 | 光源方向、光质、冷暖、体积光 | `golden hour backlight, Tyndall beams, low key` |
| 6 | 主色/辅色/强调色，整体色调 | `warm ivory, gold, deep umber palette` |
| 7 | 画幅、镜头、视角、景深 | `85mm lens, shallow depth of field, low angle` |
| 8 | 质感、笔触、颗粒、滤镜 | `film grain, Kodak Portra, impasto brushwork` |
| 9 | 一句话氛围收尾 | `majestic, ominous, serene, epic grand scale` |

---

## 参数决策表

| 主题类型 | --ar | --s | --style | 说明 |
|---|---|---|---|---|
| 人物竖版肖像 | 9:16 | 200-300 | raw | 85mm，浅景深 |
| 横版电影场景/风景 | 16:9 | 250-350 | raw | 24mm，深景深 |
| 概念艺术/插画/水墨 | 16:9 或 9:16 | 350-450 | 不加 raw | 艺术发挥度高 |
| 产品/道具四视图 | 16:9 | 150-200 | raw | 精确结构 |
| 巨物/怪兽/机甲 | 16:9 | 300-350 | raw | 低角度仰拍 |
| 室内建筑/空间 | 16:9 | 250 | raw | 24mm，深景深 |
| 暗黑/地狱/恶魔 | 16:9 | 300-350 | raw | 低照度高对比 |
| 卡通/动画风 | 16:9 或 9:16 | 350 | 不加 raw | 不写 photorealistic |

**固定版本**：`--v 8.2`

---

## 用户偏好强化项

以下偏好会在合适的主题中自动带入：

### 光影
- 午后侧方柔光、漫射光、柔焦光斑
- 体积雾、丁达尔光、god rays
- 逆光轮廓光（rim light）

### 胶片质感
- `Kodak Portra film aesthetic`
- `subtle film grain`
- `low contrast`
- `shallow warm tone`（浅暖色调）

### 动态感
- `hair blowing in wind`（发丝飘动）
- `fabric flowing / billowing`（衣袂飞扬）
- `natural fabric folds`（布料自然褶皱）

### 人物处理
- 远景人物模糊化，不清晰刻画
- 自然皮肤质感，不要塑料皮肤
- 服装有自然磨损/使用痕迹

---

## 高频词库

### 光影词
```
golden hour backlight, rim light, cinematic lighting, chiaroscuro
volumetric fog, Tyndall light beams, soft diffused light
low key lighting, high contrast, moody atmosphere
warm amber glow, cool blue shadow, mixed temperature
overcast diffused light, grey-blue ambient tone
```

### 质感词
```
photorealistic, ultra detailed, natural skin texture
shot on ARRI ALEXA Mini LF, 85mm lens
Kodak Portra film aesthetic, subtle film grain
shallow depth of field, bokeh
```

### 氛围词
```
mystical, sacred, ominous, melancholic, majestic, epic, serene, nostalgic
```

---

## 负面词体系

### 通用屏蔽包（每次必带）
```
cartoon, anime, illustration, 3d render, cgi, plastic texture, deformed, bad anatomy, extra limbs, blurry, low resolution, watermark, text, logo, signature, overexposed
```

### 风格二选一封装
- **要真人/写实时**：`painting, drawing, digital art, illustration, anime style`
- **要绘画/插画时**：`photorealistic, realistic, photograph, human skin texture`

### 主题特定屏蔽（根据主题自动追加）
- 人物：`old, beard, heavy makeup, dark circles, acne`
- 室内：`people, crowd, modern furniture, LED lights`
- 风景：`buildings, cars, people close-up`
- 怪兽：`cute, friendly, named IP monster`
- 暗黑：`bright, sunny, cheerful, colorful`

---

## 主题适配速查

| 输入关键词 | 自动执行策略 |
|---|---|
| 真人/帅哥/小姐姐/国王 | 竖版9:16，85mm，浅景深，胶片质感，侧光 |
| 风景/山水/稻田/森林 | 横版16:9，24mm，深景深，自然光，胶片颗粒 |
| 室内/书房/客厅/宴会厅 | 横版16:9，24mm，对称构图，深景深 |
| 神话/史诗/神像/战场 | 横版16:9，--s 300+，低角度，体积光 |
| 怪兽/机甲/巨物 | 横版16:9，低角度，城市/云层做尺度参照 |
| 暗黑/地狱/熔岩 | 横版16:9，低 key，红黑主色，烟雾 |
| 科幻/太空/战舰 | 横版16:9，冷蓝/金属灰，太空背景 |
| 历史/年代/民国 | 横版或竖版，复古色调，胶片颗粒，做旧 |
| 卡通/动画 | 横版，--s 350，不写 photorealistic，不加 raw |
| 产品/道具四视图 | 横版16:9，--s 150-200，纯白/简洁背景，精确结构 |
| 参考图"炼化" | 读图后逐元素拆解：建筑/人物/服装/光影/色彩/材质/构图/氛围 |
| 参考图"去掉人" | 读图后删人物描述，负面词加 people/person |

---

## 参考图炼化流程

当用户上传图片时：

1. **读取图片**，仔细观察所有元素。
2. 拆解为 8 个维度：
   - 空间/建筑结构
   - 主体人物/物体
   - 服装/材质/装饰
   - 家具/道具/植物
   - 光源方向与光质
   - 主色/辅色/点缀色
   - 构图/视角/镜头
   - 氛围情绪
3. 按 9 段式写成正向词。
4. 根据图片风格写负面词。
5. 根据图片宽高比定 `--ar`，根据写实/绘画定 `--style raw`。
6. 用户说"去掉人"就把人物全删，负面词加 `people, person`。
7. 用户说"改色调/改光线/改布局"，只改对应部分。

---

## 迭代修改规则

| 用户指令 | 执行动作 |
|---|---|
| "不要那么成熟，要少年感" | 调年轻化：五官、发型、服装、表情，其他不动 |
| "偏冷色/偏暖色" | 整体色调替换，光影冷暖反转 |
| "去掉人物" | 删人物描述，负面词加 people |
| "再来一版/重新规划" | 保留核心主题，换角度/光线/构图 |
| "不要蜡烛/不要XX" | 删对应描述，负面词加该元素 |
| "参考这张图" | 读图后融入其风格，新主题不变 |
| "见光不见灯/无光源污染" | 写 hidden cove lighting, no visible fixtures, no glare |
| "生活痕迹/使用痕迹/旧感" | 加 worn, faded, scuffed, lived-in, chipped |

---

## 质量检查清单

每次出词前自查：

- [ ] 风格锚点是否在最开头？
- [ ] 主体是否清晰，没有模糊描述？
- [ ] 光影是否具体到方向、光质、冷暖？
- [ ] 色彩是否明确主/辅色，不是"beautiful colors"？
- [ ] 构图是否写了镜头、视角、景别？
- [ ] 负面词是否屏蔽了该主题最容易跑偏的方向？
- [ ] 参数 `--ar` 是否和主题匹配？
- [ ] 有没有混入上一个主题的残留元素？
- [ ] 有没有版权 IP 名或违规词？
- [ ] 写实主题是否带了胶片颗粒、镜头词？
- [ ] 人物主题是否带了发丝飘动、布料褶皱？

---

## 使用方式

输入任意主题：

```
规划提示词：[主题描述]
```

或上传图片：

```
[图片] 炼化
[图片] 参考这张图改一下XX
```

输出格式：

```
### 正向提示词
[英文提示词]

### 负面提示词
[英文负面词]

### 参数
--ar [比例] --v 8.2 --s [数值] [--style raw]
```
