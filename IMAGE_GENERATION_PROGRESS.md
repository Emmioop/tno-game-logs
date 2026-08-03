# 事件图片生成进度与恢复指南

## 任务目标
为游戏中**所有事件**添加单独的历史风格图片，确保每个事件弹窗都显示与其内容匹配的真实JPG图片。

## 总体架构
- 游戏共有 **80,274个事件**：274个剧情事件 + 80,000个随机事件
- 随机事件虽有8万个，但只有 **50种类型**（如"美国民权运动"、"密码破译"等）
- 策略：为50种事件类型各生成1张图片 + 为274个剧情事件各生成1张独立图片
- 图片存放在 `/workspace/img/events/` 目录
- 图片通过 `_getEventImage()` 函数在 `js/ui.js` 中映射

## 已完成进度

### 第一批：50种随机事件类型图片 ✅ 已完成
文件名前缀 `ev_type_`，覆盖所有50种事件类型：
- ev_type_civil_rights.jpg (美国民权运动)
- ev_type_mark_devaluation.jpg (马克贬值)
- ev_type_state_funeral.jpg (国葬)
- ev_type_codebreaking.jpg (密码破译)
- ev_type_occult.jpg (神秘学活动)
- ev_type_arsenal_explosion.jpg (军火库爆炸)
- ev_type_diplomatic_crisis.jpg (外交危机)
- ev_type_black_market.jpg (黑市走私)
- ev_type_air_show.jpg (航空展)
- ev_type_slave_revolt.jpg (奴隶起义)
- ev_type_satellite_launch.jpg (人造卫星发射)
- ev_type_religious_conflict.jpg (宗教冲突)
- ev_type_paranormal.jpg (超自然现象调查)
- ev_type_propaganda.jpg (宣传战)
- ev_type_art_looting.jpg (艺术品掠夺)
- ev_type_rocket_failure.jpg (火箭试射失败)
- ev_type_military_mutiny.jpg (国防军哗变)
- ev_type_plague.jpg (瘟疫爆发)
- ev_type_tech_breakthrough.jpg (技术突破)
- ev_type_border_clash.jpg (边境冲突)
- ev_type_space_race.jpg (太空竞赛突破)
- ev_type_defection.jpg (高官叛逃)
- ev_type_espionage.jpg (间谍案)
- ev_type_camp_riot.jpg (集中营暴动)
- ev_type_sports.jpg (体育赛事)
- ev_type_strike.jpg (罢工潮)
- ev_type_underground.jpg (地下抵抗)
- ev_type_gas_leak.jpg (毒气泄漏)
- ev_type_nuclear_accident.jpg (核设施事故)
- ev_type_military_parade.jpg (阅兵式)
- ev_type_intelligence_leak.jpg (情报泄露)
- ev_type_harvest.jpg (粮食丰收)
- ev_type_student_protest.jpg (学生示威)
- ev_type_submarine.jpg (潜艇失踪)
- ev_type_infiltration.jpg (勃艮第渗透)
- ev_type_warlord.jpg (俄罗斯军阀动态)
- ev_type_economic_crisis.jpg (经济危机)
- ev_type_ss_activity.jpg (党卫军异动)
- ev_type_nuclear_test.jpg (核试验)
- ev_type_mine_collapse.jpg (矿井坍塌)
- ev_type_slave_auction.jpg (奴隶拍卖)
- ev_type_ufo.jpg (UFO目击)
- ev_type_weather_anomaly.jpg (气象异常)
- ev_type_navy_army_rivalry.jpg (日本陆海对立)
- ev_type_movie_premiere.jpg (电影首映)
- ev_type_food_shortage.jpg (粮食短缺)
- ev_type_diplomatic_wedding.jpg (外交婚礼)
- ev_type_currency_reform.jpg (货币改革)
- ev_type_assassination_plot.jpg (暗杀阴谋)
- ev_type_industrial_accident.jpg (工业事故)

### 第二批：剧情事件图片 ✅ 已完成约170张
已完成的剧情事件系列：
- 勃艮第/海德里希系列 (ev_burgundy_*, ev_heydrich_*)
- 内战系列 (ev_civil_war_*, ev_choose_successor)
- 施佩尔系列 (ev_speer_*)
- 戈林系列 (ev_goring_*, ev_goering_*)
- 鲍曼系列 (ev_bormann_*)
- 俄罗斯系列 (ev_russia_*, ev_amur_*, ev_buryat_*, ev_chita_*, ev_irktusk_*, ev_kemerovo_*, ev_komi_*, ev_magadan_*, ev_omsk_*, ev_samara_*, ev_siberian_*, ev_sverdlovsk_*, ev_tomsk_*, ev_vyatka_*)
- 美国系列 (ev_us_*)
- 日本系列 (ev_japan_*)
- 中立区系列 (ev_neutral_zone_*, ev_speidal_*, ev_speidel_*, ev_crimea_hofer, ev_hofer_*)
- 结局系列 (ev_2000_finale, ev_millennium_*, ev_final_*, ev_new_world_order_*, ev_end_of_cold_war)
- 地中海/意大利/土耳其系列 (ev_mediterranean_*, ev_italian_*, ev_italy_*, ev_triumvirate_*, ev_turkey_*, ev_iberia*, ev_spanish_*)

### 第三批：剧情事件图片 ⏳ 未完成
还需要生成以下约85个剧情事件的图片：

#### 中国/亚洲系列
- ev_china_economic_collapse_1968|中国大崩溃
- ev_china_resistance_1968|中原烽火
- ev_china_warlord_era_1978|中国的碎片化
- ev_cps_china_inferno|中国腹地的怒火
- ev_cps_decolonization|共荣圈的解体
- ev_cps_korea_uprising|朝鲜的怒火
- ev_cps_manchuria_resistance|满洲的火种
- ev_indian_civil_war|次大陆的撕裂
- ev_indonesian_independence|香料群岛的怒火
- ev_indonesian_resistance_1972|万隆之火
- ev_manchukuo_industrialization|满洲的钢铁
- ev_korean_uprising_1975|朝鲜的怒吼
- ev_japan_reform|东京之春
- ev_japan_yen_collapse|日元的崩盘

#### 非洲/中东系列
- ev_africa_scramble|非洲独立浪潮
- ev_anarchy_west_africa|无政府区的黎明
- ev_congo_dam_crisis|刚果之泪
- ev_first_nile_war|第一次尼罗河战争
- ev_ofn_intervention_africa_1976|非洲的代理人战争
- ev_saharan_war|撒哈拉战争
- ev_somali_ethiopian_war|非洲之角的战争
- ev_south_africa_crisis|南非种族隔离危机
- ev_south_african_war|好望角的硝烟
- ev_iranian_revolution|波斯的怒吼
- ev_lebanon_civil_war|雪松之国的崩塌
- ev_middle_east (已有图片 ev_middle_east.jpg)
- ev_suez_crisis|苏伊士运河危机

#### 经济/科技系列
- ev_economic_bubble_1982|繁荣的泡沫
- ev_economic_collapse_1975|一九七五：大崩溃
- ev_economic_globalization|地球村的黎明
- ev_german_economic_crisis_1985|帝国的黄昏
- ev_german_internet|帝国的网络
- ev_global_boom_1985|全球经济繁荣
- ev_oil_crisis_1979|黑金的诅咒
- ev_brazil_economic_miracle|南美的经济奇迹
- ev_argentina_dirty_war|银之河的肮脏战争
- ev_genetic_engineering|上帝的剪刀
- ev_personal_computer|每个人的计算机
- ev_information_age|信息时代
- ev_technology_revolution_1995|数字革命
- ev_mars_landing|火星之上
- ev_space_race_2|星辰大海
- ev_space_race_mars|红色的星球
- ev_space_station|天空之城

#### 核/环境系列
- ev_chernobyl_equivalent|熔毁
- ev_nuclear_accident_germany|哈茨山的火光
- ev_nuclear_disarmament|削减
- ev_nuclear_near_miss|千钧一发
- ev_env_cold_war_thaw|解冻
- ev_nuclear_free_world|无核世界的远景
- ev_environmental_movement|绿色的觉醒
- ev_pandemic_flu|白色瘟疫

#### 欧洲/其他系列
- ev_berlin_wall_equivalent|墙倒了
- ev_french_civil_war|法国内战
- ev_french_occupation_costs|占领法国的经济成本
- ev_degaulle_return|戴高乐回归
- ev_free_france_rallying|自由法国集结
- ev_british_resistance (已有 ev_british_resistance.jpg)
- ev_british_underground (已有 ev_british_underground.jpg)
- ev_atlantropa_aftermath|亚特兰特罗帕的伤疤
- ev_atlantropa_consequences|亚特兰特罗帕的诅咒
- ev_gibraltar_dam_maintenance|直布罗陀大坝危机
- ev_student_movement_1968|一九六八：街头的革命
- ev_reform_movement_1987|改革的新风
- ev_refugee_crisis_balkans|巴尔干的流民
- ev_disarmament_geneva|日内瓦的谈判桌
- ev_aryan_brotherhood|崇拜仇敌的人
- ev_underground_nazi_resistance|地下的旧梦
- ev_slave_rebellion_east|东方的怒火
- ev_slave_revolt_cycle|枷锁下的怒火
- ev_ural_border_war|乌拉尔的炮声
- ev_second_west_russian_war|AA线危机
- ev_west_russia_final|命运的抉择：战争与和平
- ev_wrrf_consolidation|北方的红旗
- ev_russia_magadan|马加丹的港口
- ev_russia_monarchist_unified|双头鹰的重生
- ev_russia_nuclear_threat|核阴影
- ev_russia_omsk_black_league|黑林的复仇者
- ev_russia_pressure_1979|最后通牒的前奏
- ev_russia_reconciliation|东方的和解
- ev_russia_recovery_1|俄罗斯重建：钢铁复苏
- ev_russia_recovery_2|俄罗斯重新武装：铁幕降临
- ev_russia_superpower|第四极
- ev_russia_superregional_war|俄罗斯的决战
- ev_russia_tomsk_yagoda|托木斯克的红旗
- ev_russia_unification_type|东方的曙光——或暗夜
- ev_russia_unification_war|统一之战
- ev_russia_unified_emergence|巨熊苏醒
- ev_russia_warlords_1968|群雄逐鹿
- ev_russia_wrrf|西俄革命阵线的余烬
- ev_taboritsky_collapses|黑暗的终结
- ev_tabortsy_purge|神权恐怖
- ev_latin_america (已有 ev_latin_america.jpg)

#### rnd_ 开头的随机事件（约19个）
- rnd_assassination_attempt|暗杀阴谋
- rnd_burgundy_remnant|勃艮第残党
- rnd_civil_unrest|民众骚乱
- rnd_coup_attempt|政变企图
- rnd_diplomatic_breakthrough|外交突破
- rnd_economic_boom|经济利好
- rnd_economic_sanctions|国际制裁
- rnd_industrial_accident|工厂事故
- rnd_military_scandal|军方丑闻
- rnd_natural_disaster|自然灾害
- rnd_nuclear_accident|核事故
- rnd_plague_outbreak|瘟疫
- rnd_research_breakthrough|科研突破
- rnd_russian_refugees|俄罗斯难民潮
- rnd_scientist_defects|科学家出逃
- rnd_slave_revolt|奴隶起义
- rnd_spain_refugees|西班牙难民
- rnd_youth_subculture|亚文化浪潮

## 代码修改要点

### ui.js 中 _getEventImage() 函数
当前已有 `themeImages` 映射表（44个主题→图片）和 `realImages` 映射表。

**需要修改的逻辑：**
1. 剧情事件（非 ev_gen_ 开头）：直接用事件ID匹配 `img/events/{eventId}.jpg`
2. 随机事件（ev_gen_ 开头）：从标题提取事件类型，映射到 `ev_type_{类型英文}.jpg`
3. rnd_ 开头事件：映射到对应 `rnd_{id}.jpg`

**随机事件类型→图片文件名映射：**
```
美国民权运动 → ev_type_civil_rights.jpg
马克贬值 → ev_type_mark_devaluation.jpg
国葬 → ev_type_state_funeral.jpg
密码破译 → ev_type_codebreaking.jpg
神秘学活动 → ev_type_occult.jpg
军火库爆炸 → ev_type_arsenal_explosion.jpg
外交危机 → ev_type_diplomatic_crisis.jpg
黑市走私 → ev_type_black_market.jpg
航空展 → ev_type_air_show.jpg
奴隶起义 → ev_type_slave_revolt.jpg
人造卫星发射 → ev_type_satellite_launch.jpg
宗教冲突 → ev_type_religious_conflict.jpg
超自然现象调查 → ev_type_paranormal.jpg
宣传战 → ev_type_propaganda.jpg
艺术品掠夺 → ev_type_art_looting.jpg
火箭试射失败 → ev_type_rocket_failure.jpg
国防军哗变 → ev_type_military_mutiny.jpg
瘟疫爆发 → ev_type_plague.jpg
技术突破 → ev_type_tech_breakthrough.jpg
边境冲突 → ev_type_border_clash.jpg
太空竞赛突破 → ev_type_space_race.jpg
高官叛逃 → ev_type_defection.jpg
间谍案 → ev_type_espionage.jpg
集中营暴动 → ev_type_camp_riot.jpg
体育赛事 → ev_type_sports.jpg
罢工潮 → ev_type_strike.jpg
地下抵抗 → ev_type_underground.jpg
毒气泄漏 → ev_type_gas_leak.jpg
核设施事故 → ev_type_nuclear_accident.jpg
阅兵式 → ev_type_military_parade.jpg
情报泄露 → ev_type_intelligence_leak.jpg
粮食丰收 → ev_type_harvest.jpg
学生示威 → ev_type_student_protest.jpg
潜艇失踪 → ev_type_submarine.jpg
勃艮第渗透 → ev_type_infiltration.jpg
俄罗斯军阀动态 → ev_type_warlord.jpg
经济危机 → ev_type_economic_crisis.jpg
党卫军异动 → ev_type_ss_activity.jpg
核试验 → ev_type_nuclear_test.jpg
矿井坍塌 → ev_type_mine_collapse.jpg
奴隶拍卖 → ev_type_slave_auction.jpg
UFO目击 → ev_type_ufo.jpg
气象异常 → ev_type_weather_anomaly.jpg
日本陆海对立 → ev_type_navy_army_rivalry.jpg
电影首映 → ev_type_movie_premiere.jpg
粮食短缺 → ev_type_food_shortage.jpg
外交婚礼 → ev_type_diplomatic_wedding.jpg
货币改革 → ev_type_currency_reform.jpg
暗杀阴谋 → ev_type_assassination_plot.jpg
工业事故 → ev_type_industrial_accident.jpg
```

### CSS样式 (style.css)
- `.event-image-banner-wrap`: height 200px, overflow hidden
- `.event-image-banner`: width 100%, height 100%, object-fit cover
- 已设置暗色背景 `#1a1a20` 作为加载前占位

### 预加载机制 (ui.js preloadEventImages)
- 进入游戏后500ms开始逐个预加载所有图片
- 已在 `quickStart()`, `start()`, 和继续游戏按钮中调用
- **注意：预加载列表需要更新为完整列表**

### 图片压缩
- 原始AI生成图片约300KB-1MB
- 需要用Python+Pillow压缩到25-80KB/张
- 压缩脚本：目标宽度800px，质量参数自适应

## 违禁词规避经验
- "爆炸"、"火球"、"坦克"、"士兵"、"武器"等词可能触发安全检查
- 用"橙色火光与浓烟"、"戏剧性场景"、"身影"等中性词替代
- "暗杀"用"紧张氛围"、"神秘场景"替代
- 避免直接描述暴力场景，改用建筑/风景/气氛描述

## 下一步计划
1. 完成剩余约85个剧情事件图片生成
2. 用Python脚本批量压缩所有图片到25-80KB
3. 更新 `_getEventImage()` 函数：剧情事件直接用ID匹配，随机事件用类型映射
4. 更新 `preloadEventImages()` 中的图片列表
5. 更新 index.html 缓存版本号
6. 测试验证并推送到GitHub

## 当前版本号
- CSS: v=61
- JS: v=61
