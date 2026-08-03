## v0.4.3 — 2026-08-03

### 完成内容
- 修复 `renderTab` 无限递归（Tab 点击完全无反应的根因）
- 修复 `tab-flavor` 容器永远 `display:none`（风味 Tab 点开是空白的根因）
- 修复 `classifyDirection` 漏读 `body`/`content` 字段（大量事件徽章显示错误的根因）
- 补丁 IIFE 顶部先保存全部原始函数引用，再执行重写

### 测试结果
- `classifyDirection`：18/18 通过（含 body 字段事件）
- 原始函数保存：6/6 正确
- Tab 显隐：flavor 打开时 content 隐藏，events 打开时 flavor 隐藏
- 语法检查：game.js / ui.js / save_system.js 全部 OK

### 文件变更
- `js/game.js` — classifyDirection 文本拼接补全
- `js/ui.js` — 补丁 IIFE 重写（先保存后覆盖 + 双容器显隐）
- `index.html` — tab-flavor 默认 display:none

### 经验
- 装饰器/猴子补丁模式必须先保存原始引用再覆盖，否则首次调用时缓存的是自己
- DOM 容器显隐应由 JS 路由统一控制，不要写死在 HTML 里
- 事件对象字段名要穷举（title/desc/text/body/content），不能假设统一用某个
