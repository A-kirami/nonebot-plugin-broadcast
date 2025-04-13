from nonebot import logger, on_command
from nonebot.adapters.onebot.v11 import Bot, Message, PrivateMessageEvent
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER

broadcast = on_command("广播", aliases={"bc"}, permission=SUPERUSER)


@broadcast.handle()
async def _(bot: Bot, event: PrivateMessageEvent, arg: Message = CommandArg()) -> None:
    msg = arg.extract_plain_text().strip()
    if not msg:
        await bot.send_private_msg(
            user_id=event.user_id, message="请在指令后接需要广播的消息"
        )
    group_list = await bot.get_group_list()
    for group in group_list:
        try:
            await bot.send_group_msg(group_id=group["group_id"], message=msg)
        except Exception as e:
            logger.warning(f"群 {group} 广播消息时出错: {e}")
