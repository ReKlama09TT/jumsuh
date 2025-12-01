# bot.py — Бот: Кыргызча гана, чек → @bazalarkg, админ тастыктоо

import asyncio
import logging
import sqlite3
from datetime import datetime
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart
from aiogram.types import (
    Message, ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
)
from aiogram.fsm.storage.memory import MemoryStorage

# ─── Токендер ───────────────────────────────────────────────────────
TOKEN = "8331810499:AAERYrcLn64m5Zxg0_8JkrPBpx7ke72S_4o"
ADMIN_ID = 8302818436

# ─── Бот объекттери ─────────────────────────────────────────────────
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()

# ─── База (жаңыланган: рефералдар үчүн) ─────────────────────────────
conn = sqlite3.connect("users.db", check_same_thread=False)
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS users")
c.execute("DROP TABLE IF EXISTS pending_payments")

c.execute('''
    CREATE TABLE users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        phone TEXT,
        registered_at TEXT,
        is_blocked INTEGER DEFAULT 0,
        ref_by INTEGER DEFAULT 0,
        referrals INTEGER DEFAULT 0
    )
''')
c.execute('''
    CREATE TABLE pending_payments (
        user_id INTEGER PRIMARY KEY,
        payment_photo_id TEXT,
        sent_to_channel BOOLEAN DEFAULT 0,
        approved BOOLEAN DEFAULT 0,
        created_at TEXT
    )
''')
conn.commit()

# ─── QR сүрөтү ──────────────────────────────────────────────────────
QR_IMAGE_URL = "https://i.ibb.co/XZXk1sf9/IMG-20251124-WA0536-fotor-enhance-2025113012193.jpg"

# ─── Клавиатура ─────────────────────────────────────────────────────
def main_kb(is_admin=False):
    rows = [
        [KeyboardButton(text="👷 Жумуш группалары"), KeyboardButton(text="🚌 Автобустар")],
        [KeyboardButton(text="📢 Жарнама жайгаштыруу"), KeyboardButton(text="👤 Мой профиль")],
        [KeyboardButton(text="🤝 Досунду чакыр")]
    ]
    if is_admin:
        rows.append([KeyboardButton(text="🛠️ Админ панель")])
    return ReplyKeyboardMarkup(keyboard=rows, resize_keyboard=True)

# ─── Хендлерлер ─────────────────────────────────────────────────────

@router.message(CommandStart())
async def start(message: Message):
    uid = message.from_user.id
    c.execute("SELECT is_blocked FROM users WHERE user_id=?", (uid,))
    row = c.fetchone()
    if row and row[0] == 1:
        return await message.answer("🔒 Сиз блоктолгонсуз! Ботту колдонуу мүмкүн эмес.")

    # Реферал ID алуу
    ref_by = None
    if message.text and " " in message.text:
        ref_param = message.text.split(" ", 1)[1]
        if ref_param.isdigit():
            ref_by = int(ref_param)

    is_admin = (uid == ADMIN_ID)
    if row:
        await message.answer(f"👋 Кайра кош келиңиз, {message.from_user.first_name}!", reply_markup=main_kb(is_admin))
    else:
        # Жаңы колдонуучуну каттоо
        username = message.from_user.username or ""
        c.execute("""
            INSERT INTO users (user_id, username, first_name, phone, registered_at, is_blocked, ref_by)
            VALUES (?, ?, ?, ?, ?, 0, ?)
        """, (uid, username, message.from_user.first_name, None, datetime.now().strftime("%d.%m.%Y %H:%M"), ref_by))
        if ref_by:
            c.execute("UPDATE users SET referrals = referrals + 1 WHERE user_id = ?", (ref_by,))
        conn.commit()
        await message.answer("👋 Саламатсызбы! Телефон номериңизди жиберип, кабыл алыңыз.", reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="📲 Номерди жиберүү", request_contact=True)]],
            resize_keyboard=True, one_time_keyboard=True
        ))

@router.message(F.contact)
async def contact(message: Message):
    uid = message.from_user.id
    c.execute("SELECT is_blocked FROM users WHERE user_id=?", (uid,))
    row = c.fetchone()
    if row and row[0] == 1:
        return await message.answer("🔒 Сиз блоктолгонсуз!")
    if message.contact.user_id != message.from_user.id:
        return await message.answer("📱 Сураныч, өзүңүздүн номериңизди гана жибериңиз!")
    c.execute("UPDATE users SET phone = ? WHERE user_id = ?", (message.contact.phone_number, uid))
    conn.commit()
    await message.answer("✅ Катталдыңыз!", reply_markup=main_kb(uid == ADMIN_ID))
# ─── ДОСУНДУ ЧАКЫР ──────────────────────────────────────────────────
@router.message(F.text.in_({"Досунду чакыр", "🤝 Досунду чакыр"}))
async def invite_friends(message: Message):
    uid = message.from_user.id
    c.execute("SELECT is_blocked FROM users WHERE user_id=?", (uid,))
    row = c.fetchone()
    if row and row[0] == 1:
        return await message.answer("🔒 Сиз блоктолгонсуз!")
    ref_link = f"https://t.me/bishkek_jobs_pro_bot?start={uid}"
    await message.answer(
        f"🎉 **20 досуңузду чакырып, 10 жумуш группасына *акысыз* кошулуп алгыла!**\n\n"
        f"🔗 Сиздин шилтемеңиз:\n`{ref_link}`\n\n"
        f"✅ Ар бир досуңуз катталган сайын, сиздин балансыңыз көбөйүп турат. "
        f"Эгерде 20 досуңуз катталса — автоматтык түрдө акысыз кошулат!",
        parse_mode="Markdown"
    )
# ─── ПРОФИЛЬ: ЧАКЫРУУ СТАТИСТИКАСЫ ──────────────────────────────────
@router.message(F.text.in_({"Мой профиль", "👤 Мой профиль"}))
async def profile(message: Message):
    c.execute("SELECT * FROM users WHERE user_id=?", (message.from_user.id,))
    u = c.fetchone()
    if not u:
        return await message.answer("❌ Эмне экен? Сиз катталган эмессиз!")
    username_display = f"@{u[1]}" if u[1] else "—"
    ref_link = f"https://t.me/bishkek_jobs_pro_bot?start={u[0]}"
    await message.answer(f"""
👤 **СИЗДИН ПРОФИЛИҢИЗ**

🆔 **ID**: `{u[0]}`
📛 **Аты**: {u[2]}
📞 **Номер**: `{u[3]}`
🔖 **Username**: {username_display}
📅 **Катталган**: {u[4]}
🤝 **Чакырдыңыз**: {u[7]} дос
🔗 **Сиздин шилтеме**: `{ref_link}`
    """, parse_mode="Markdown", reply_markup=main_kb(message.from_user.id == ADMIN_ID))
# ─── ЖУМУШ ГРУППАЛАРЫ (акысыз чек-кошуп) ───────────────────────────
@router.message(F.text.in_({"Жумуш группалары", "👷 Жумуш группалары"}))
async def jobs(message: Message):
    uid = message.from_user.id
    c.execute("SELECT is_blocked, referrals FROM users WHERE user_id=?", (uid,))
    row = c.fetchone()
    if row and row[0] == 1:
        return await message.answer("🔒 Сиз блоктолгонсуз!")
    if row and row[1] >= 20:
        await message.answer("🎉 Сиз 20+ дос чакырдыңыз! Сиз акысыз кошулдуңуз.\nАдмин сизге жумуш группаларына кошоп жатышат.")
        return
    await message.answer_photo(
        photo=QR_IMAGE_URL,
        caption="📲 Сканерлеңиз жана **150 сом** төлөңүз мен сизди ватсаптан 10 группага кошом.\n\n📌 Төлөмдөн кийин **чекти WhatsApp'ка жөнөтүңүз**:",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📲 WhatsApp'ка жөнөтүү", url="https://wa.me/996504589189?text=Мага%2010%20жумуш%20группасы%20керек.%20Төлөм%20жасалды.%20Чектин%20скриншотун%20жөнөттүм.")]
        ])
    )
    await message.answer("📸 Эми **чекти ботко жиберип, тастыктоону сураныз**.")

# ─── ФОТО ЖАНА БАШКА БӨЛҮМДӨР ───────────────────────────────────────
# (Булардын коду өзгөртүлбөй калды — төмөндө жалгашат)

@router.message(F.photo)
async def receive_payment_proof(message: Message):
    uid = message.from_user.id
    c.execute("SELECT approved FROM pending_payments WHERE user_id=?", (uid,))
    row = c.fetchone()
    if row and row[0] == 1:
        await message.answer("✅ Сиз буга чейин тастыкталгансиз!")
        return
    wait_msg = await message.answer("⏳ Күтө турунуз, текшерип жатам…")
    photo_id = message.photo[-1].file_id
    phone = "—"
    c.execute("SELECT phone FROM users WHERE user_id=?", (uid,))
    phone_row = c.fetchone()
    if phone_row:
        phone = phone_row[0]
    c.execute("INSERT OR REPLACE INTO pending_payments (user_id, payment_photo_id, sent_to_channel, approved, created_at) VALUES (?,?,?,?,?)",
              (uid, photo_id, 0, 0, datetime.now().strftime("%Y-%m-%d %H:%M")))
    conn.commit()
    try:
        await bot.send_photo(
            chat_id="@bazalarkg",
            photo=photo_id,
            caption=f"🆔 **User ID**: `{uid}`\n📞 **Номер**: `{phone}`\n⏰ **Жөнөтүлдү**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n✅ *Төлөмдү тастыктоо керек*",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="✅", callback_data=f"approve_{uid}")],
                [InlineKeyboardButton(text="❌", callback_data=f"reject_{uid}")]
            ])
        )
        await wait_msg.edit_text("✅ Чек базага жөнөтүлдү! Админ текшергендиктен кийин кабар келет.")
    except Exception as e:
        logging.error(f"Каналга жөнөтүү катасы: {e}")
        await wait_msg.edit_text("❌ Чекти жөнөтүү мүмкүн эмес. Админ менен байланышыңыз.")

@router.callback_query(F.data.startswith(("approve_", "reject_")))
async def handle_approval(cb: CallbackQuery):
    if cb.from_user.id != ADMIN_ID:
        return await cb.answer("🚫 Укугуңуз жок!")
    action, uid_str = cb.data.split("_", 1)
    try:
        uid = int(uid_str)
    except ValueError:
        return await cb.answer("❌ Туура эмес ID!")
    c.execute("SELECT user_id FROM pending_payments WHERE user_id=?", (uid,))
    if not c.fetchone():
        return await cb.answer("❌ Төлөм табылган жок!")
    if action == "approve":
        c.execute("UPDATE pending_payments SET approved=1 WHERE user_id=?", (uid,))
        conn.commit()
        await bot.send_message(uid, "🎉 Ийгиликтүү төлөм! Сиз 10 жумуш группасына тез арада админстартор байланышып кошуп койот!", reply_markup=main_kb(uid == ADMIN_ID))
        await cb.message.edit_text(cb.message.caption + "\n\n🟢 **Тастыкталды!**")
    else:
        c.execute("DELETE FROM pending_payments WHERE user_id=?", (uid,))
        conn.commit()
        await bot.send_message(uid, "❌ Төлөмүңүз ийгиликсиз болду. Суроо болсо, админге жүгүнүңүз.")
        await cb.message.edit_text(cb.message.caption + "\n\n🔴 **Ийгиликсиз!**")
    await cb.answer()

@router.message(F.text.in_({"Автобустар", "🚌 Автобустар"}))
async def bus(message: Message):
    await message.answer(
        "🚌 **БИШКЕК АВТОБУСТАРЫ**\n📍 Реалдуу убакытта карта",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text="🗺️ Картаны ачуу", url="https://e-meria.kg/transport-map")
        ]])
    )

@router.message(F.text.in_({"Жарнама жайгаштыруу", "📢 Жарнама жайгаштыруу"}))
async def reklama(message: Message):
    await message.answer(
        "📢 **ЖАРНАМА ЖАЙГАШТЫРУУ**\n\n🌍 7 область — 80 группа → 💰 **400 сом**\n🏘️ Чүй облусу — 50 группа → 💰 **300 сом**\n📊 Күнүнө 2 жолу отчет",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🌍 7 область — 400 сом", url="https://wa.me/996504589189?text=7%20область%20боюнча%20жарнама")],
            [InlineKeyboardButton(text="🏘️ Чүй облусу — 300 сом", url="https://wa.me/996504589189?text=Чүй%20облусу%20боюнча%20жарнама")],
        ])
    )

# ─── АДМИН ПАНЕЛ: БАЗАНЫ HTML МЕНЕН ЭКСПОРТТОО ─────────────────────
@router.message(F.text.in_({"Админ панель", "🛠️ Админ панель", "/admin"}))
async def admin_panel(message: Message):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("🚫 Укугуңуз жок!")
    c.execute("SELECT COUNT(*), COUNT(CASE WHEN is_blocked=1 THEN 1 END) FROM users")
    total, blocked = c.fetchone()
    await message.answer(
        f"🛠️ **Админ панель**\n\n👥 Жалпы колдонуучу: **{total}**\n🔒 Блоктолгон: **{blocked}**",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="👥 Колдонуучулар", callback_data="users_list")],
            [InlineKeyboardButton(text="📊 Базаны алуу (HTML)", callback_data="export_html")]
        ])
    )

@router.callback_query(F.data == "users_list")
async def users_list(cb: CallbackQuery):
    if cb.from_user.id != ADMIN_ID:
        return
    c.execute("SELECT user_id, username, first_name, phone, is_blocked, referrals FROM users ORDER BY registered_at DESC LIMIT 20")
    rows = c.fetchall()
    text = "👥 **Акыркы 20 колдонуучу:**\n\n"
    for u in rows:
        uid, username, fname, phone, blocked, refs = u
        status = "🔒 Блок" if blocked else "✅ Ачык"
        username_tg = f"@{username}" if username else "—"
        text += f"[{fname}](tg://user?id={uid}) | {username_tg} | `{phone}` | {status} | 🤝{refs}\n"
    await cb.message.edit_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📊 Базаны алуу", callback_data="export_html")]
    ]))

@router.callback_query(F.data == "export_html")
async def export_html(cb: CallbackQuery):
    if cb.from_user.id != ADMIN_ID:
        return await cb.answer("🚫 Укугуңуз жок!")
    c.execute("SELECT user_id, username, first_name, phone, registered_at, is_blocked, ref_by, referrals FROM users ORDER BY registered_at DESC")
    rows = c.fetchall()
    html = """<!DOCTYPE html>
<html lang="ky">
<head>
    <meta charset="UTF-8">
    <title>Колдонуучулар</title>
    <style>table{width:100%;border-collapse:collapse;}th,td{border:1px solid #ccc;padding:8px;text-align:left;}th{background:#f4f4f4;}</style>
</head>
<body>
    <h2>Колдонуучулар базасы ({} колдонуучу)</h2>
    <table>
        <tr><th>ID</th><th>Аты</th><th>Username</th><th>Номер</th><th>Катт.</th><th>Блок</th><th>Ким чакырды</th><th>Чакырды</th></tr>
""".format(len(rows))
    for u in rows:
        uid, username, fname, phone, reg, blocked, ref_by, refs = u
        username = f"@{username}" if username else "—"
        blocked = "Блок" if blocked else "Ачык"
        html += f"<tr><td>{uid}</td><td>{fname}</td><td>{username}</td><td>{phone}</td><td>{reg}</td><td>{blocked}</td><td>{ref_by or '—'}</td><td>{refs}</td></tr>\n"
    html += """</table></body></html>"""
    with open("users_export.html", "w", encoding="utf-8") as f:
        f.write(html)
    await cb.message.answer_document(document=open("users_export.html", "rb"), caption="✅ Колдонуучулар базасы HTML форматында экспорттолду.")
    await cb.answer()

@router.message()
async def unknown(message: Message):
    c.execute("SELECT is_blocked FROM users WHERE user_id=?", (message.from_user.id,))
    row = c.fetchone()
    if row and row[0] == 1:
        return await message.answer("🔒 Сиз блоктолгонсуз!")
    await message.answer("башка Менюдан тандаңыз.", reply_markup=main_kb(message.from_user.id == ADMIN_ID))

# ─── Негизги иштетүү ───────────────────────────────────────────────
async def main():
    dp.include_router(router)
    print("✅ Бот иштейт... Кыргызча гана, чек → @bazalarkg, админ тастыктоо!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
