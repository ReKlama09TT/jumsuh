<!DOCTYPE html>
<html lang="ky">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Секрет База — VIP Кызмат</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    <style>
        :root {
            --primary: #8A2BE2;
            --secondary: #FF6B6B;
            --dark: #2C2C54;
            --light: #F7F9FC;
            --success: #28a745;
            --error: #dc3545;
            --shadow: 0 15px 35px rgba(0,0,0,0.1);
            --transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 10px;
            overflow-x: hidden;
            touch-action: manipulation;
        }

        .container {
            width: 100%;
            max-width: 600px;
            background: rgba(255, 255, 255, 0.96);
            backdrop-filter: blur(10px);
            border-radius: 24px;
            padding: 30px 20px;
            box-shadow: var(--shadow);
            position: relative;
            overflow: hidden;
            text-align: center;
            animation: float 6s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }

        .container::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(138,43,226,0.08) 0%, transparent 70%);
            z-index: -1;
            pointer-events: none;
        }

        /* Hero Screen — Роль тандоо */
        .hero {
            padding: 30px 15px;
        }

        .hero h1 {
            font-size: 1.8rem;
            color: var(--dark);
            margin-bottom: 15px;
            font-weight: 800;
            letter-spacing: -0.5px;
            line-height: 1.3;
            background: linear-gradient(to right, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .hero p {
            color: #555;
            font-size: 1rem;
            line-height: 1.6;
            margin-bottom: 25px;
            padding: 0 10px;
        }

        .role-btn {
            display: block;
            width: 90%;
            max-width: 300px;
            padding: 22px 15px;
            margin: 12px auto;
            background: white;
            border: 2px solid var(--primary);
            border-radius: 20px;
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--primary);
            cursor: pointer;
            transition: var(--transition);
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
            text-align: center;
            touch-action: manipulation;
        }

        .role-btn:hover, .role-btn:active {
            transform: translateY(-3px) scale(1.02);
            box-shadow: 0 8px 25px rgba(138,43,226,0.2);
            background: var(--primary);
            color: white;
        }

        .role-btn i {
            font-size: 2rem;
            display: block;
            margin-bottom: 10px;
        }

        .role-btn small {
            display: block;
            font-size: 0.85rem;
            margin-top: 5px;
            opacity: 0.9;
        }

        /* Форма стилдери */
        .form-container {
            display: none;
            animation: fadeIn 0.6s ease-out;
            padding: 20px 15px;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: scale(0.95); }
            to { opacity: 1; transform: scale(1); }
        }

        .form-header h2 {
            font-size: 1.6rem;
            color: var(--dark);
            margin-bottom: 10px;
            font-weight: 700;
        }

        .form-header p {
            color: #666;
            font-size: 0.95rem;
            margin-bottom: 25px;
            line-height: 1.5;
        }

        .form-group {
            margin-bottom: 20px;
            text-align: left;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: var(--dark);
            font-size: 0.95rem;
        }

        input, select, textarea {
            width: 100%;
            padding: 14px;
            border: 2px solid #e1e5eb;
            border-radius: 14px;
            font-size: 1rem;
            transition: var(--transition);
            background: white;
            box-shadow: 0 2px 5px rgba(0,0,0,0.03);
        }

        input:focus, select:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 5px 15px rgba(138,43,226,0.15);
            transform: scale(1.01);
        }

        button {
            width: 95%;
            max-width: 320px;
            padding: 16px;
            background: linear-gradient(135deg, var(--primary), #6a5acd);
            color: white;
            border: none;
            border-radius: 18px;
            font-size: 1.1rem;
            font-weight: 700;
            cursor: pointer;
            transition: var(--transition);
            margin: 20px auto 10px;
            display: block;
            box-shadow: 0 5px 20px rgba(138,43,226,0.3);
            touch-action: manipulation;
        }

        button:hover, button:active {
            transform: translateY(-3px) scale(1.03);
            box-shadow: 0 8px 25px rgba(138,43,226,0.4);
        }

        #message {
            margin: 15px auto;
            padding: 12px;
            border-radius: 12px;
            text-align: center;
            font-weight: 600;
            font-size: 0.95rem;
            max-width: 90%;
            display: none;
        }

        .success { background: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
        .error { background: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }

        /* Модалдык терезе */
        .modal {
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.85);
            backdrop-filter: blur(8px);
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .modal-content {
            background: white;
            padding: 30px 20px;
            border-radius: 24px;
            width: 100%;
            max-width: 340px;
            text-align: center;
            position: relative;
            animation: modalIn 0.5s ease-out;
        }

        @keyframes modalIn {
            from { opacity: 0; transform: scale(0.8); }
            to { opacity: 1; transform: scale(1); }
        }

        .close-modal {
            position: absolute;
            top: 15px;
            right: 15px;
            font-size: 1.5rem;
            cursor: pointer;
            color: #888;
            padding: 5px;
        }

        .modal h2 {
            color: var(--dark);
            margin-bottom: 15px;
            font-size: 1.5rem;
        }

        .modal p {
            margin: 12px 0;
            line-height: 1.6;
            color: #555;
            font-size: 0.95rem;
        }

        .badge {
            display: inline-block;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            margin: 8px 4px;
        }

        .badge-seller { background: #FF6B6B; color: white; }
        .badge-buyer { background: #4ECDC4; color: white; }

        /* Confetti */
        .confetti {
            position: absolute;
            width: 8px;
            height: 8px;
            animation: fall 5s linear forwards;
        }

        @keyframes fall {
            to { transform: translateY(100vh) rotate(360deg); opacity: 0; }
        }

        /* Responsive адаптация */
        @media (min-width: 768px) {
            .container {
                padding: 40px;
                border-radius: 28px;
            }

            .hero h1 {
                font-size: 2.5rem;
            }

            .role-btn {
                width: 45%;
                display: inline-block;
                margin: 10px;
            }

            button {
                width: 100%;
                max-width: none;
                margin: 25px auto 15px;
            }
        }

        /* Мобилдикте форманын ичин жеңил скроллоо үчүн */
        .form-container {
            max-height: 70vh;
            overflow-y: auto;
            padding-bottom: 60px;
        }

        /* Safe area for iPhone notch */
        @supports (padding: max(0px)) {
            body {
                padding-top: max(20px, env(safe-area-inset-top));
                padding-bottom: max(20px, env(safe-area-inset-bottom));
            }
        }
    </style>
</head>
<body>
    <!-- Баштапкы экран: Роль тандоо -->
    <div class="container" id="roleSelector">
        <div class="hero">
            <h1>UCHASTOKTOR.KG</h1>
            <p>Сиз кайсы тараптан киресиз? Төмөнкү бир түймөнү тандап, VIP кызматтан пайдаланыңыз.</p>
            
            <div>
                <div class="role-btn" onclick="selectRole('seller')">
                    <i class="fas fa-home"></i>
                    Мен сатуучумун
                    <small>Үй же участок сатам</small>
                </div>
                
                <div class="role-btn" onclick="selectRole('buyer')">
                    <i class="fas fa-search"></i>
                    Мен сатып алуучумун
                    <small>Үй же участок издеп жатам</small>
                </div>
            </div>
        </div>
    </div>

    <!-- Форма (башында жашырын) -->
    <div class="container form-container" id="applicationFormContainer">
        <div class="form-header">
            <h2 id="formTitle">Заявка толтуруу</h2>
            <p id="formDesc">Төмөнкү маалыматтарды толугу менен жазыңыз.</p>
        </div>

        <form id="applicationForm">
            <input type="hidden" id="userRole" value="">

            <div class="form-group">
                <label><i class="fas fa-layer-group"></i> Түрү</label>
                <select id="propertyType" required>
                    <option value="">Тандаңыз...</option>
                    <option value="Участок">Участок</option>
                    <option value="Үй">Үй</option>
                </select>
            </div>

            <div class="form-group">
                <label><i class="fas fa-compass"></i> Багыт / Аймак</label>
                <select id="direction" required>
                    <option value="">Тандаңыз...</option>
                    <option value="Түндүк">Түндүк</option>
                    <option value="Түштүк">Түштүк</option>
                    <option value="Чыгыш">Чыгыш</option>
                    <option value="Батыш">Батыш</option>
                </select>
            </div>

            <div class="form-group">
                <label><i class="fas fa-map-marked-alt"></i> Район</label>
                <input type="text" id="district" placeholder="Мисалы: Чүй, Ысык-Көл, Ош" required>
            </div>

            <div class="form-group">
                <label><i class="fas fa-map-pin"></i> Адрес (село, көчө, үй)</label>
                <input type="text" id="address" placeholder="Толугураак жазыңыз" required>
            </div>

            <div class="form-group">
                <label><i class="fas fa-ruler-combined"></i> Аянты (сотых / м²)</label>
                <input type="text" id="area" placeholder="Мисалы: 10 сотых же 150 м²" required>
            </div>

            <div class="form-group">
                <label><i class="fas fa-dollar-sign"></i> Баасы (мүмкүн болсо)</label>
                <input type="text" id="price" placeholder="Мисалы: 50 000$">
            </div>

            <div class="form-group">
                <label><i class="fas fa-image"></i> Сүрөт (URL)</label>
                <input type="text" id="photoUrl" placeholder="https://example.com/photo.jpg">
            </div>

            <div class="form-group">
                <label><i class="fas fa-user"></i> Атыңыз</label>
                <input type="text" id="name" placeholder="Толук атыңыз" required>
            </div>

            <div class="form-group">
                <label><i class="fas fa-phone"></i> Телефон</label>
                <input type="tel" id="phone" placeholder="+996 XXX XXX XXX" required>
            </div>

            <button type="submit" id="submitBtn">
                <i class="fas fa-paper-plane"></i> VIP Заявка жөнөтүү
            </button>
        </form>

        <div id="message"></div>
    </div>

    <!-- Модалдык терезе -->
    <div class="modal" id="successModal">
        <div class="modal-content">
            <span class="close-modal" onclick="closeModal()">&times;</span>
            <h2>🎉 Куттуктайбыз!</h2>
            <p>Сиздин <span id="modalRoleBadge"></span> заявкаңыз ийгиликтүү жөнөтүлдү!</p>
            <p><strong>Биз 15 мүнөт ичинде сиз менен байланышабыз.</strong></p>
            <button onclick="resetFlow()" style="margin-top:20px; padding:14px 30px; background:var(--primary); color:white; border:none; border-radius:16px; cursor:pointer; font-size:1.05rem; font-weight:700;">
                🔄 Жаңы заявка түзүү
            </button>
        </div>
    </div>

    <script>
        let userRole = '';

        function selectRole(role) {
            userRole = role;
            document.getElementById('roleSelector').style.display = 'none';
            const formContainer = document.getElementById('applicationFormContainer');
            formContainer.style.display = 'block';
            
            // Мобилдикте форманын үстүнө скролл
            setTimeout(() => {
                formContainer.scrollTo({ top: 0, behavior: 'smooth' });
            }, 300);

            const title = document.getElementById('formTitle');
            const desc = document.getElementById('formDesc');
            const badge = document.getElementById('modalRoleBadge');

            if (role === 'seller') {
                title.innerHTML = '🏡 Сатуучу үчүн VIP Форма';
                desc.innerHTML = 'Сиздин үй же участокту сатуу боюнча маалыматтарды толтуруңуз.';
                badge.innerHTML = '<span class="badge badge-seller">VIP Сатуучу</span>';
            } else {
                title.innerHTML = '🔍 Сатып Алуучу үчүн VIP Форма';
                desc.innerHTML = 'Сиз издеп жаткан үй же участоктун сипаттамаларын жазыңыз.';
                badge.innerHTML = '<span class="badge badge-buyer">VIP Сатып Алуучу</span>';
            }

            document.getElementById('userRole').value = role;
        }

        function resetFlow() {
            document.getElementById('successModal').style.display = 'none';
            document.getElementById('applicationFormContainer').style.display = 'none';
            document.getElementById('roleSelector').style.display = 'block';
            document.getElementById('applicationForm').reset();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function closeModal() {
            document.getElementById('successModal').style.display = 'none';
        }

        // Telegram жөнөтүү
        document.getElementById('applicationForm').addEventListener('submit', async function(e) {
            e.preventDefault();

            const formData = {
                role: document.getElementById('userRole').value,
                propertyType: document.getElementById('propertyType').value,
                direction: document.getElementById('direction').value,
                district: document.getElementById('district').value,
                address: document.getElementById('address').value,
                area: document.getElementById('area').value,
                price: document.getElementById('price').value,
                photoUrl: document.getElementById('photoUrl').value,
                name: document.getElementById('name').value,
                phone: document.getElementById('phone').value
            };

            // Валидация
            if (!formData.propertyType || !formData.direction || !formData.district || !formData.address || !formData.area || !formData.name || !formData.phone) {
                showMessage('❌ Бардык талаалар толтурулушу керек!', 'error');
                return;
            }

            const botToken = '8055839738:AAEAgTwOKZp00o8MANoEEBUZwthONUOKHE4';
            const chatId = '@Sekretbazakg';

            let emoji = formData.role === 'seller' ? '🏡' : '🔍';
            let roleLabel = formData.role === 'seller' ? 'VIP Сатуучу' : 'VIP Сатып Алуучу';

            let message = `
${emoji} <b>${roleLabel} — Жаңы Заявка</b>

🏗 <b>Түрү:</b> ${formData.propertyType}
🧭 <b>Багыт:</b> ${formData.direction}
📍 <b>Район:</b> ${formData.district}
🏠 <b>Адрес:</b> ${formData.address}
📏 <b>Аянты:</b> ${formData.area}
💰 <b>Баасы:</b> ${formData.price || 'Көрсөтүлгөн жок'}
🖼 <b>Сүрөт:</b> ${formData.photoUrl ? `<a href="${formData.photoUrl}">Көрүү</a>` : 'Жок'}
👤 <b>Аты:</b> ${formData.name}
📞 <b>Телефон:</b> ${formData.phone}

📱 <i>Мобилдик формадан жөнөтүлдү</i>
            `;

            const submitBtn = document.getElementById('submitBtn');
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Жөнөтүлүүдө...';

            try {
                const response = await fetch(`https://api.telegram.org/bot${botToken}/sendMessage`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        chat_id: chatId,
                        text: message,
                        parse_mode: 'HTML',
                        disable_web_page_preview: false
                    })
                });

                const result = await response.json();
                if (result.ok) {
                    showSuccessModal();
                } else {
                    showMessage(`❌ Ката: ${result.description}`, 'error');
                }
            } catch (error) {
                showMessage('❌ Интернетке туташуу ката чыкты. Кайталап көрүңүз.', 'error');
                console.error('Error:', error);
            } finally {
                submitBtn.disabled = false;
                submitBtn.innerHTML = '<i class="fas fa-paper-plane"></i> VIP Заявка жөнөтүү';
            }
        });

        function showSuccessModal() {
            document.getElementById('successModal').style.display = 'flex';
            createConfetti();
        }

        function showMessage(text, type) {
            const msgDiv = document.getElementById('message');
            msgDiv.textContent = text;
            msgDiv.className = type;
            msgDiv.style.display = 'block';
            setTimeout(() => {
                msgDiv.style.display = 'none';
            }, 5000);
        }

        function createConfetti() {
            for (let i = 0; i < 80; i++) {
                const confetti = document.createElement('div');
                confetti.classList.add('confetti');
                confetti.style.left = Math.random() * 100 + 'vw';
                confetti.style.backgroundColor = `hsl(${Math.random() * 360}, 100%, 50%)`;
                confetti.style.animationDuration = (Math.random() * 3 + 2) + 's';
                confetti.style.animationDelay = Math.random() * 2 + 's';
                document.body.appendChild(confetti);
                setTimeout(() => {
                    confetti.remove();
                }, 5000);
            }
        }

        // Esc басылса модал жабылсын
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                closeModal();
            }
        });
    </script>
</body>
</html>
