## v0.4.2 — 2026-08-03

### 完成内容
- 实现事件双轨制：核心事件弹窗 + 风味事件自动归档
- 实现事件方向分类系统（国内/对日/对美/对俄/对意/其他）
- 6 色方向徽章内嵌到弹窗标题、事件日志、风味卡片
- 修复 ui.js 装饰器选择器不匹配 bug（改用直接重写）
- 修复 nextTurn 事件双触发问题
- 修复 game.js russia 关键词数组重复行语法错误
- 调整 classifyDirection 优先级：russia > japan > america > italy > internal
- save_system 旧存档自动补 flavorLog 字段

### 测试结果
- 功能测试：20/20 通过
- 集成测试：全部通过
- 语法检查：game.js / ui.js / save_system.js 全部 OK

### 文件变更
- `js/game.js` — 新增 3 个分类函数，重写 getEventsForTurn
- `js/ui.js` — 重写 showEventModal / renderEventLog / renderTab / showNextEvent / nextTurn
- `js/save_system.js` — deserialize 补 flavorLog 兜底
- `css/style.css` — 新增徽章 + 色条 + 风味卡片 + empty-hint 样式
- `index.html` — 新增风味 Tab，版本号升级
- `SAVE_VERSION` 16 → 17

### 已知限制
- 旧存档（v16 及以下）不兼容，需开新档
- 事件过滤器/搜索功能留待 v0.4.3+
