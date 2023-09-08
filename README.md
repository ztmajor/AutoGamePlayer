# AutoGamePlayer
用代码控制安卓模拟器上的重复性游戏操作
**目前仅实现了在windows端的操作**

**目前代码中大量借用了airtest的代码，并且还没有带license，如果之后要release代码，需要带上license， 借用的代码会在文件中添加TODO进行提示，未添加TODO的就是借用的**

# Get Start
```
pip install -e .
```
# AutoGamePlayer V1.0

对于超能世界实现了以下功能：
- 日常任务： daily_routine
- 单刷试炼之地： place_of_trial1 / place_of_trial2 （需要预先进入试炼之地）
- 单推最新章节： break_through_latest_levels （需要进入主界面）
- 联盟自动帮点-
- 神奇树洞一键探索
- 游乐园自动抽奖
- 自动收送爱心
- 使用点金手

# 原子操作
## 图片分析
- 给定对应图片，找到图片中的对应位置
- ORC文字提取