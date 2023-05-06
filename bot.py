import nonebot
from nonebot.adapters.onebot import V11Adapter as OnebotAdapters

# 初始化 NoneBot
nonebot.init()

# 注册适配器
driver = nonebot.get_driver()
driver.register_adapter(OnebotAdapters)

# 在这里加载插件
nonebot.load_builtin_plugins("echo")  # 内置插件
nonebot.load_plugin("nonebot_plugin_petpet")
nonebot.load_plugin("nonebot_plugin_status")
nonebot.load_plugin("nonebot_plugin_starrail_calendar")
nonebot.load_plugin("nonebot_plugin_gspanel")

if __name__ == "__main__":
    nonebot.run()