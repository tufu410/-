# 10 · 图像资产提示词体系（Image Prompts / Lira）

> 产角色、场景、道具静态资产，以及对已有画面做精修/反打时读本文件。回复用用户语言，**提示词正文与行业术语保留英文**。可直接复制的成稿模板见 `assets/image-prompt-templates.md` 与 `assets/character-kit-template.md`。

## 目录

1. 四维工作法与两种工作模式
2. 模型分配对照表（固定路由）
3. 防生成失败十律（全部模型）
4. 各模型完整规则
5. 可复用组件：技术参数块 / 色调 / 摄影师 / 正向替代表
6. 各类提示词写法（角色 / 场景 / 道具 / 编辑 / 纹理 / 反打）
7. 输出前检查清单

---

## 1. 四维工作法与两种模式

内部对每个请求走完四步，再输出：

1. **DECONSTRUCT 拆解**：识别核心意图、主体、上下文；确定目标模型与输出约束（画幅、单张/设定表、生成/编辑）；梳理已有与缺失信息。
2. **DIAGNOSE 诊断**：找出模糊点（机位、光照、色调、主体数量、构图）；预判风险（跑偏成插画、纹身/文字崩坏、多人崩坏、提示词臃肿）。
3. **DEVELOP 构建**：按任务类型选技术方案与模板，分层组织上下文。
4. **DELIVER 交付**：优先放提示词，附简短使用说明（留意什么、哪些参数可调）。

工作模式：

- **DETAIL 详细**：需求模糊或高重要度时，先提 2–3 个针对性澄清问题（总数 ≤3），再优化。
- **BASIC 基础**：用户要求直接输出、或粘贴提示词写明“改写适配 XX”时，修复核心问题、套模板直接出。

回复格式：简单请求给「代码块提示词 + 1–3 行改动说明」；复杂请求先给提示词，再用简短列表/前后对比说明设计与理由。

## 2. 模型分配对照表（固定路由，不要混用）

| 任务 | 模型 | 说明 |
|---|---|---|
| 角色设定表、人像、时尚大片，保证人物一致 | **Higgsfield Soul 2.0**（备选 **Cinema Studio AI Cast**） | 写实人物；Soul ID 锁定跨次生成面部。AI Cast 可全自动出角色设定表，独立工具、UI 设参、无需手写提示词 |
| 环境场景、定场镜头、电影剧照、概念图 | **Higgsfield Soul Cinema** | 电影级纹理、自然胶片颗粒、光影、时代美学；支持 21:9；可放入带 Soul ID 的角色 |
| 道具设定表、产品类物体 | **NBP / GPT Image 2** | 写实产品质感、物体文字渲染精准 |
| 已有画面编辑（**永远首选**） | **Nano Banana Pro（NBP）** | 基于原图改，改动最小、其余像素全保留；最高 4K；画面内文字渲染最好 |
| 修复成品图崩坏的 AI 纹理（皮肤/织物/表面） | **Seedream（4.5 及以上）** | 仅修复糊纹理；**禁止做点状局部编辑** |
| 终极备选：极小范围精细局部修改、换场景视角 | **GPT Image 2** | 会轻微污染整张画面，但局部修改与反打优秀 |

编辑任务固定优先级：**NBP 优先 → Seedream 仅纹理修复 → GPT Image 2 终极备选**。

默认分配：人物/角色表→Soul 2.0（或推荐 AI Cast）；场景/电影镜头→Soul Cinema；道具/产品→NBP 或 GPT Image 2；已有图编辑→NBP；纹理糊块→Seedream，NBP 搞不定的精细局部→GPT Image 2；换机位反打→GPT Image 2（用 NBP 必须写明全部物体新位置）；需要整张重绘≠编辑，交回 Soul 系列。

三条硬约束：

1. Soul 2.0 **不支持 21:9**；带人物的宽银幕镜头用 Soul Cinema + Soul ID。
2. 画幅、分辨率是平台 UI 参数，**不写进提示词**：不写 `--ar`、不写 `16:9`、`4K` 等标记，改用构图描述（`wide panoramic frame`、`vertical full-body framing`）。
3. 所有这些图像模型都**没有负面提示词参数**：不写“不要 XX”，改用正向描述（见第 3 节）。

## 3. 防生成失败十律（每条提示词都遵守）

1. **通顺自然描述，拒绝关键词堆砌**：`4k, masterpiece, trending` 之类标签无效。不要全大写标题；`CHANGE / PRESERVE EXACTLY` 大写区块**只允许出现在编辑类提示词**。
2. **拒绝臃肿**：80–150 词精炼 > 400 词散乱；过长稀释权重、丢细节。删掉无效修饰，保留核心锚点。
3. **正向描述优先**：干净皮肤写 `clean dry skin`（不写 `no acne`）；空旷街道写 `empty deserted street`（不写 `no people`）。否定列表反而引入想规避的概念。编辑类允许写移除指令（`Remove the lamppost`），但**必须同时写明空缺填充什么**（`continuous brick wall behind`）。
4. **画幅/分辨率在 UI 设置**：正文只写构图描述，禁参数语法。
5. **写具体光照与材质，拒绝空泛氛围词**：`single overhead key light, soft 2:1 ratio, smooth falloff` 优于空泛的 `dramatic cinematic lighting`。写真实材质与表面处理：`board-formed concrete`、`oxidized copper verdigris`。景深/光学参数用于**人物**，不要给到场景环境描述。
6. **色调控制**：百分比写法全模型适配，`palette of 60% warm ochre, 30% deep charcoal, 10% rust-red`，遵循 60/30/10 主色-辅色-点缀。配比取自用户需求/参考图，**不擅自改用户指定色调**。
7. **人物一致性靠 Soul ID，不靠文字**：文字锚点只做辅助（`the same real person in all three panels`），不能单靠文字保证跨镜头人脸不变。
8. **防插画跑偏（写实向）**：`character reference sheet`、`painterly` 会触发插画画风，写实任务避免，改用 `studio photographs / film character sheet / cinematic film still`。修复漂移靠加强写实锚点（胶片型号、镜头、真实材质），不堆否定词。
9. **文字/纹身/真人/品牌规则**：画面内文字给完整引号原文 + 字体/字重/颜色（`Write 'GENUINE' in bold red serif on the sign`）；纹身写具体图案 + `clean line-work`（`classic swallow`、`old-school dagger`）；禁止现实名人姓名（转成外貌/体型/气质描述）；禁止 IP、品牌名称。
10. **编辑最小改动**：NBP 优先，最小 CHANGE、详尽 PRESERVE EXACTLY，**一次只改一件事物**；用户反馈改动过大，说明锁定不足，应少改、多保留。

## 4. 各模型完整规则

### Soul 2.0 — 人物生成

- 擅长写实人物、角色设定表、人像、时尚大片。画质 1.5k/2k（UI）。
- 画幅：1:1、16:9、9:16、4:3、3:4、3:2、2:3；**无 21:9**。参考图上限 1 张。
- Soul ID 是平台一致性参数；文字仅辅助。
- 写法：通顺简短自然描述 + 身份锚点 + 摄影锚点（`studio photographs`、`film character sheet`、定向光照）。
- 禁写：`painterly`、`character reference sheet`（触发插画）、全大写面板标题；面板用自然语言。

### Soul Cinema — 场景与电影镜头

- 擅长电影级静帧、概念图、定场镜头、剧照。画幅含 **21:9**；参考图 1 张，可放入带 Soul ID 的角色。
- 优势：胶片质感、自然颗粒、光影、时代美学、皮肤与织物材质；成品可直接作视频关键帧。
- 模型原生自带胶片颗粒，**技术块写一行即可，不堆颗粒词**。
- 机位锚定（最常见痛点）：直白物理描述优于抽象黑话。
  - 推荐：`high angle three-quarter wide shot, camera high above the room looking diagonally down at 45 degrees`。
  - 慎用：监控摄像头、鱼眼等抽象术语（易畸变崩坏）。

### Cinema Studio AI Cast — 自动角色设定表

- 全自动输出统一风格电影角色设定表，**无需手写提示词**；Higgsfield 独立工具，全部参数在 UI 面板设置。
- 用户目标是“产出角色设定表”时，**优先推荐这个快速方案**；Soul 2.0 三面板模板仅用于需要完全手动控制细节时。

### Nano Banana Pro（NBP）— 编辑首选与道具

- 编辑：所有图片编辑第一步；编辑=原图后期，**禁止用编辑功能整张重绘**（重绘交 Soul）。
- 道具：与 GPT Image 2 一起产道具表/产品，写实产品质感。
- 分辨率 1k/2k/4k，含 21:9、4:5/5:4；参考图上限 14 张；自然语言编辑，自动适配光照反射；强项是画面内文字渲染（引号写全文 + 字体字重颜色）。
- **换场景视角必须写明物体全新摆放位置**（主视角沙发在右侧，反打视角沙发移至左侧），否则空间错乱。

### Seedream（4.5 及以上）— 仅纹理修复

- 唯一功能：修复成品图糊掉的 AI 纹理（皮肤毛孔、织物编织、表面污渍质感）。**不能定点局部编辑。**
- 基础最高 4K、高规格约 6K，支持多参考图。
- 写法：目标“修复崩坏 AI 纹理”；CHANGE 写待修复表面；PRESERVE 锁构图、人脸、光照、调色。

### GPT Image 2 — 终极局部修改 + 反打

- 全局会被轻微改动，但局部修改强。用途：NBP 完不成的极小局部修改；与 NBP 配合做道具；切换场景机位/反打很合适。
- 分辨率 1k/2k/4k，低/中/高画质档。
- 用同样的精准编辑模板；PRESERVE 要写得尽可能完整（该模型易擅自重绘）。

## 5. 可复用组件（同一项目统一复用，保证视觉统一）

### 平台参数（UI 设置，禁止写进正文）

- 画幅：Soul Cinema 21:9 宽银幕；人物设定 16:9；竖版 UGC 9:16；道具 1:1；人像 3:4/2:3。Soul 2.0 无 21:9。
- 画质：Soul 系列 1.5k/2k；NBP/Seedream/GPT Image 2 最高 4K。
- Soul ID 在 UI 设置；AI Cast 全自动、UI 设置。

### 胶片颗粒电影质感块

```text
Photorealistic ARRI Alexa LF anamorphic Cooke S4 lens at T2.0, organic 35mm Kodak Vision3 250D film grain, soft cinematic falloff, cinematic film still aesthetic
```

> 搭配低饱和调色与电影氛围；写实人物设定表不写 `painterly`。

### 现代干净数字电影块

```text
Shot on ARRI Alexa Mini LF with ARRI Signature Prime lens, clean modern digital cinematic capture, crisp natural detail, minimal fine grain, soft cinematic falloff, modern cinematic film still quality, hyperrealistic photographic detail
```

配套：`natural living skin tones, medium contrast, subtle cool tone in the shadows, true-to-life modern colour, no heavy desaturation`。与胶片版区分：无厚重颗粒、不强降饱和。Soul Cinema 原生自带颗粒，技术块宜短。

### 色调模板

```text
Refined desaturated palette: cool dominant tones dominating, warm element as the only warm contrast, deep crushed blacks, restrained naturalistic grading, soft low contrast, strong cinematic chiaroscuro
```

支持百分比写法；写实人物删 `painterly`；色调配比来自用户输入/参考，不擅自编造。

### 摄影师 / 氛围参考（点到为止，不堆砌名单）

- Roger Deakins：写实自然光、受控剪影（银翼杀手 2049、1917）。
- Emmanuel Lubezki：自然光、广角、手持（荒野猎人、生命之树）。
- Hoyte van Hoytema：宏大写实（星际穿越）。
- Christopher Blauvelt：静谧（第一头牛）。
- Paweł Pawlikowski：复古忧郁、极简室内（冷战、伊达）。
- Andrei Tarkovsky：画中画构图、室内望向室外（镜子、潜行者）。
- Akira Kurosawa：安静风景氛围；Naomi Kawase：日本乡村氛围。

### 正向替代否定词

- 防插画跑偏：加胶片型号、镜头、真实材质、`cinematic film still`，不写“不要绘画风”。
- 空旷：`empty deserted street, bare walls, still air`（不写 `no people`）。
- 干净皮肤：`clean dry skin`（不写 `no acne`）。
- 道具无 logo：`plain unbranded wrapper, blank matte surface`，完全不写品牌。
- 编辑移除指令后必须补“空缺填充内容”。

### 精准编辑模板（NBP 优先，全编辑流程通用）

```text
Edit the image: 【一行写编辑目标】.
CHANGE: 【仅写需要修改的一项，描述精准】.
PRESERVE EXACTLY:
- 【列出所有必须原样保留：人脸、服装、道具、物体位置、墙面地面、机位角度、原有全部阴影】
- Color grade, palette, contrast, grain, falloff
ONLY CHANGE: 【再次重申唯一改动项】. 100% identical otherwise.
```

经验：改动过大/跑偏，说明 CHANGE 写多了；应尽可能锁定，只改极少部分。Seedream 纹理修复：CHANGE 写修复表面，PRESERVE 锁构图/身份/光照/调色，禁定点编辑。GPT Image 2：同样模板，CHANGE 范围尽可能窄。

## 6. 各类提示词写法

### 角色设定表（写实三面板，Soul 2.0）

> 快速方案优先推荐 **Cinema Studio AI Cast 全自动**；需手动精细控制才用此模板。UI：画幅 16:9、2k，已有角色填 Soul ID。

```text
Three studio photographs of the same [人物] arranged side by side on a flat neutral mid-grey studio backdrop, a film character sheet: full-body front photo on the left, full-body back photo in the middle, close-up portrait photo on the right, the same real person in all three, consistent across panels. Soft directional cinematic studio lighting from one side, gentle natural shadow falloff, clean neutral cinematic look.
The [人物]: [年龄，体型，人种特征，面部特征，发型，胡须，独特标记；参考现实人物只写特征，禁止写人名].
[Wardrobe, consistent in all panels: 全部面板统一服装]. [Distinctive props / signature items. 标志性道具].
On the left panel the [人物] stands straight facing the camera in a neutral pose, arms relaxed at the sides, full figure head to feet. In the middle panel the same standing pose is seen from behind. On the right panel a close-up head-and-shoulders portrait, [表情 + 关键面部细节].
[色调行]. [技术参数块].
```

规则：禁 `character reference sheet`、`painterly`，改用 `film character sheet` / `studio photographs`；设定表**不用三分构图**；一致性锚点 `same real person in all three, consistent across panels`、服装 `consistent in all panels`；面板用连贯文字、不写 LEFT/MIDDLE/RIGHT 大写块；纹身具体图案 + `clean line-work`；单向定向光、不平光；跨镜头一致性靠 Soul ID。

### 场景环境（Soul Cinema）

UI：宽银幕 21:9、普通视频 16:9、2k。

```text
【机位锚定，最重要，写得明确直白】. 【场景身份】.
【关键建筑/自然景物】. 【光源 + 方向 + 色温】.
【远景元素向画面深处延伸】. 【色调模板】. 【技术参数块】.
【氛围/摄影师参考】.
【需要空旷则正向描述：empty deserted interior, bare walls, still air】.
```

技巧：直白物理机位优于抽象黑话；用现实设备与摄影词汇；地板木纹等顽固几何正向描述；画中画构图（前景残破墙体暗色框住门窗洞口，塔可夫斯基式）；**景深/光学参数不写进场景提示词，留给人物镜头**；技术块简短、不重复堆颗粒。

### 道具设定表（NBP / GPT Image 2）

UI：画幅 1:1（高道具 3:4）、2k–4k。

```text
Photorealistic [top-down / three-quarter overhead] product shot of [道具] on a [neutral grey concrete] surface, [soft directional lighting], isolated subject.
【道具具体描述：材质、磨损状态】. 【不需要 logo 就正向写 plain unbranded surfaces】. 【技术参数块】.
```

不同状态（完好/破损/沾染血迹）拆成独立资产；危险类道具规避敏感词、描述材质与功能；不写品牌、正向写无标识。

### 图片编辑（永远优先 NBP）

用精准编辑模板，最小 CHANGE、详尽 PRESERVE EXACTLY、一次改一件；锁定人脸、服装、道具、机位、阴影、调色，除非明确要改它们。流程：

1. 优先 NBP；
2. AI 纹理糊块→Seedream 仅纹理修复，禁定点编辑；
3. NBP 搞不定的微小局部→GPT Image 2，范围尽可能小；
4. 需要整张重绘→不属编辑，交 Soul 重新生成。

**换场景机位/反打**：默认交 GPT Image 2；若用 NBP，逐个写明物体镜像后新位置（“主视角沙发在右侧；本反打沙发移至左侧，原本在摄像机后方的门洞现在出现在前景”）。

### 视频提示词衔接（Seedance / 可灵等）

核心同样是“写人物处于动作状态之中，不写完整过渡过程”（挥拳进行中、投掷进行中，不写伸手-掏出-挥臂蓄力）；加 `rule of thirds`（角色设定表除外）。可灵用自定义多镜头、不用时间码；Seedance 用时间码结构；需要时出中英双语。视频侧完整规则见 `40`–`43`。

## 7. 输出前检查清单

- [ ] 模型分配正确：生成用 Soul；设定表优先 AI Cast；道具 NBP/GPT Image 2；编辑优先 NBP；纹理才用 Seedream。
- [ ] 画幅、分辨率在 UI 设置，正文无参数标记（`--ar`/`16:9`/`4K`）。
- [ ] 语言通顺；`CHANGE / PRESERVE EXACTLY` 大写区块仅出现在编辑提示词。
- [ ] 正向描述优先；每处移除操作都写明空缺填充内容。
- [ ] 写明技术光照（主光、光比、衰减）与具体材质（材质 + 表面处理）。
- [ ] 色调遵循 60/30/10，取自用户输入/参考图，不擅自编造。
- [ ] 人物任务：Soul ID + 文字身份锚点。
- [ ] 除角色设定表外用三分构图。
- [ ] 无品牌、IP、现实人物姓名；无 `painterly` / `character reference sheet` 误触发。
- [ ] 提示词不臃肿（约 80–150 词，字符 ≤1500–2000），删掉无效填充。
