---

## v0.4.2 - 事件分类与精简系统

**提交**: `feat: 事件分类——核心政治按方向(国内/日本/美国/俄罗斯/其他)分类，风味事件移入"时代风貌"栏不再弹窗`

### 问题
测试员反馈每回合弹窗事件过多，登月等"时代切片"事件与政治抉择混在一起，体验混乱。

### 解决方案
实现 DEV_LOG 中 v64 设计方案：
- **双轨制**：核心政治事件（弹窗+方向徽章）vs 风味事件（自动结算+风貌栏）
- **方向分类**：国内(金黄) / 对日(粉红) / 对美(蓝) / 对俄(红) / 其他(灰)
- **关键词正则分类器**：覆盖登月、太空、奥运、阅兵、庆典、流行病、外交、战争等
- **显式 category 字段可覆盖**自动分类

### 修改文件
- `js/game.js` v44→v45（classifyEvent / classifyDirection / autoResolveFlavorEvent / getEventsForTurn 重写）
- `js/ui.js` v80→v81（_directionBadge / renderFlavorLog / renderTab flavor分支 / showEventModal徽章 / nextTurn适配）
- `css/style.css` v75→v76（方向徽章5色 / 风味卡片 / 风貌Tab高亮 / Toast flavor）
- `index.html`（新增📰时代风貌Tab / 版本号升级）
- `js/save_system.js` v3（反序列化兼容补flavorLog）

### 测试结果
15/15 分类测试全部通过，语法检查全部通过。

### 效果
- 1962Q1：2弹窗→1弹窗，登月自动归档
- 中后期弹窗量预计下降40%-60%
- 风味事件不丢失，可翻阅

—
*由 AI 助手实现，基于 v64 设计文档。*
