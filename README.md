# jumsuh
<!DOCTYPE html>
<html lang="ky">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Жумушка Кабыл Алуу - Талас</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
    <style>
        body {
            background-image: url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80');
            background-size: cover;
            background-attachment: fixed;
            font-family: 'Roboto', sans-serif;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
        }
        .card {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
            padding: 2rem;
            margin-top: 2rem;
        }
        .emoji {
            font-size: 1.5rem;
            margin: 0 0.5rem;
        }
        .btn {
            transition: transform 0.3s ease, background-color 0.3s ease;
        }
        .btn:hover {
            transform: scale(1.05);
            background-color: #2563eb;
        }
        .lang-btn {
            transition: background-color 0.3s ease;
        }
        .lang-btn:hover {
            background-color: #e5e7eb;
        }
        .lang-btn.active {
            background-color: #3b82f6;
            color: white;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
</head>
<body class="min-h-screen flex items-center justify-center">
    <div class="container">
        <div class="flex justify-end mb-4">
            <button onclick="changeLanguage('ky')" class="lang-btn px-4 py-2 mx-1 bg-gray-200 rounded-lg active">Кыргызча</button>
            <button onclick="changeLanguage('ru')" class="lang-btn px-4 py-2 mx-1 bg-gray-200 rounded-lg">Русский</button>
            <button onclick="changeLanguage('uz')" class="lang-btn px-4 py-2 mx-1 bg-gray-200 rounded-lg">O‘zbekcha</button>
        </div>
        <div class="card animate-fadeIn">
            <h1 id="title" class="text-4xl font-bold text-center text-blue-800 mb-6">Ассаламу Алейкум! 👷‍♂️</h1>
            <p id="subtitle" class="text-lg text-gray-700 mb-4">Жумушка кабыл алуу жарыясы 📢</p>
            <ul id="job-details" class="list-disc list-inside text-gray-800 mb-6 space-y-2">
                <li><span class="font-semibold">Жумуш:</span> Клатка кирпич коюу 🧱</li>
                <li><span class="font-semibold">Адрес:</span> Талас шаары 🏙️</li>
                <li><span class="font-semibold">Акысы:</span> 10 сомдон 💸</li>
                <li><span class="font-semibold">Төлөм:</span> Акча өз убагында берилет ✅</li>
                <li><span class="font-semibold">Жатакана:</span> Жатакана берилет 🏠</li>
                <li><span class="font-semibold">Тамак-аш:</span> Тамак-аш өзүңөрдөн, аванс берилет 🍽️</li>
                <li><span class="font-semibold">Бригада:</span> Максимум 3 кишиден жогору 🔢</li>
                <li><span class="font-semibold">Объект:</span> Мектептин 2-этажи 🏫</li>
                <li><span class="font-semibold">Материалдар:</span> Кирпич жана кум 2-этажга чыгарылып берилет 🚛</li>
            </ul>
            <div class="mb-6">
                <p id="contact-title" class="text-lg font-semibold text-gray-800">Байланыш үчүн маалымат:</p>
                <div class="mb-4">
                    <label id="name-label" for="name" class="block text-lg font-semibold text-gray-800 mb-2">Аты-жөнүңүз:</label>
                    <input type="text" id="name" class="w-full p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500" placeholder="Мисалы: Айбек Сыдыков">
                </div>
                <div class="mb-4">
                    <label id="phone-label" for="phone" class="block text-lg font-semibold text-gray-800 mb-2">Телефон номериңиз:</label>
                    <input type="tel" id="phone" class="w-full p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500" placeholder="Мисалы: +996 555 123 456">
                </div>
                <div class="mb-4">
                    <label id="workers-label" for="workers" class="block text-lg font-semibold text-gray-800 mb-2">Бригададагы кишилердин саны:</label>
                    <input type="number" id="workers" min="1" max="10" class="w-full p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500" placeholder="Мисалы: 3">
                </div>
                <div class="mb-4">
                    <label id="location-label" for="location" class="block text-lg font-semibold text-gray-800 mb-2">Толук дарегиңиз:</label>
                    <textarea id="location" class="w-full p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500" rows="4" placeholder="Дарегиңизди жазыңыз..."></textarea>
                </div>
            </div>
            <button id="submit-btn" onclick="submitForm()" class="btn w-full bg-blue-600 text-white py-3 rounded-lg font-semibold text-lg">Жиберүү 🚀</button>
        </div>
    </div>

    <script>
        // Current language
        let currentLang = 'ky';

        // Language translations
        const translations = {
            ky: {
                title: "Ассаламу Алейкум! 👷‍♂️",
                subtitle: "Жумушка кабыл алуу жарыясы 📢",
                jobDetails: [
                    "<span class='font-semibold'>Жумуш:</span> Клатка кирпич коюу 🧱",
                    "<span class='font-semibold'>Адрес:</span> Талас шаары 🏙️",
                    "<span class='font-semibold'>Акысы:</span> 10 сомдон 💸",
                    "<span class='font-semibold'>Төлөм:</span> Акча өз убагында берилет ✅",
                    "<span class='font-semibold'>Жатакана:</span> Жатакана берилет 🏠",
                    "<span class='font-semibold'>Тамак-аш:</span> Тамак-аш өзүңөрдөн, аванс берилет 🍽️",
                    "<span class='font-semibold'>Бригада:</span> Максимум 3 кишиден жогору 🔢",
                    "<span class='font-semibold'>Объект:</span> Мектептин 2-этажи 🏫",
                    "<span class='font-semibold'>Материалдар:</span> Кирпич жана кум 2-этажга чыгарылып берилет 🚛"
                ],
                contactTitle: "Байланыш үчүн маалымат:",
                nameLabel: "Аты-жөнүңүз:",
                namePlaceholder: "Мисалы: Айбек Сыдыков",
                phoneLabel: "Телефон номериңиз:",
                phonePlaceholder: "Мисалы: +996 555 123 456",
                workersLabel: "Бригададагы кишилердин саны:",
                workersPlaceholder: "Мисалы: 3",
                locationLabel: "Толук дарегиңиз:",
                locationPlaceholder: "Дарегиңизди жазыңыз...",
                submitBtn: "Жиберүү 🚀",
                successMsg: "Маалымат жиберилди! 👌\nАты-жөн: {name}\nТелефон: {phone}\nКишилердин саны: {workers}\nДарек: {location}",
                errorMsg: "Бардык талааларды толтуруңуз! ⚠️"
            },
            ru: {
                title: "Ассаламу Алейкум! 👷‍♂️",
                subtitle: "Объявление о найме на работу 📢",
                jobDetails: [
                    "<span class='font-semibold'>Работа:</span> Кладка кирпича 🧱",
                    "<span class='font-semibold'>Адрес:</span> Город Талас 🏙️",
                    "<span class='font-semibold'>Оплата:</span> От 10 сом 💸",
                    "<span class='font-semibold'>Выплаты:</span> Деньги выплачиваются вовремя ✅",
                    "<span class='font-semibold'>Жилье:</span> Предоставляется общежитие 🏠",
                    "<span class='font-semibold'>Питание:</span> Питание за ваш счет, предоставляется аванс 🍽️",
                    "<span class='font-semibold'>Бригада:</span> Максимум более 3 человек 🔢",
                    "<span class='font-semibold'>Объект:</span> Второй этаж школы 🏫",
                    "<span class='font-semibold'>Материалы:</span> Кирпич и песок доставляются на второй этаж 🚛"
                ],
                contactTitle: "Контактная информация:",
                nameLabel: "Ваше имя:",
                namePlaceholder: "Например: Айбек Сыдыков",
                phoneLabel: "Ваш номер телефона:",
                phonePlaceholder: "Например: +996 555 123 456",
                workersLabel: "Количество человек в бригаде:",
                workersPlaceholder: "Например: 3",
                locationLabel: "Ваш полный адрес:",
                locationPlaceholder: "Введите ваш адрес...",
                submitBtn: "Отправить 🚀",
                successMsg: "Данные отправлены! 👌\nИмя: {name}\nТелефон: {phone}\nКоличество человек: {workers}\nАдрес: {location}",
                errorMsg: "Заполните все поля! ⚠️"
            },
            uz: {
                title: "Assalomu Alaykum! 👷‍♂️",
                subtitle: "Ishga yollash e’loni 📢",
                jobDetails: [
                    "<span class='font-semibold'>Ish:</span> G‘isht terish 🧱",
                    "<span class='font-semibold'>Manzil:</span> Talas shahri 🏙️",
                    "<span class='font-semibold'>Maosh:</span> 10 somdan 💸",
                    "<span class='font-semibold'>To‘lov:</span> Pul o‘z vaqtida beriladi ✅",
                    "<span class='font-semibold'>Yashash joyi:</span> Yotoqxona beriladi 🏠",
                    "<span class='font-semibold'>Ovqat:</span> Ovqat o‘zingizdan, avans beriladi 🍽️",
                    "<span class='font-semibold'>Brigada:</span> Maksimum 3 kishidan ko‘proq 🔢",
                    "<span class='font-semibold'>Obyekt:</span> Maktabning 2-qavati 🏫",
                    "<span class='font-semibold'>Materiallar:</span> G‘isht va qum 2-qavatga olib chiqiladi 🚛"
                ],
                contactTitle: "Aloqa uchun ma’lumot:",
                nameLabel: "Ismingiz:",
                namePlaceholder: "Masalan: Aybek Sidiqov",
                phoneLabel: "Telefon raqamingiz:",
                phonePlaceholder: "Masalan: +996 555 123 456",
                workersLabel: "Brigadadagi odamlar soni:",
                workersPlaceholder: "Masalan: 3",
                locationLabel: "To‘liq manzilingiz:",
                locationPlaceholder: "Manzilingizni yozing...",
                submitBtn: "Yuborish 🚀",
                successMsg: "Ma’lumotlar yuborildi! 👌\nIsm: {name}\nTelefon: {phone}\nOdamlar soni: {workers}\nManzil: {location}",
                errorMsg: "Barcha maydonlarni to‘ldiring! ⚠️"
            }
        };

        // Language change function
        function changeLanguage(lang) {
            currentLang = lang;
            const t = translations[lang];

            // Update text content
            document.getElementById('title').innerHTML = t.title;
            document.getElementById('subtitle').innerHTML = t.subtitle;
            const jobDetails = document.getElementById('job-details');
            jobDetails.innerHTML = t.jobDetails.map(item => `<li>${item}</li>`).join('');
            document.getElementById('contact-title').innerHTML = t.contactTitle;
            document.getElementById('name-label').innerHTML = t.nameLabel;
            document.getElementById('name').placeholder = t.namePlaceholder;
            document.getElementById('phone-label').innerHTML = t.phoneLabel;
            document.getElementById('phone').placeholder = t.phonePlaceholder;
            document.getElementById('workers-label').innerHTML = t.workersLabel;
            document.getElementById('workers').placeholder = t.workersPlaceholder;
            document.getElementById('location-label').innerHTML = t.locationLabel;
            document.getElementById('location').placeholder = t.locationPlaceholder;
            document.getElementById('submit-btn').innerHTML = t.submitBtn;

            // Update active button style
            document.querySelectorAll('.lang-btn').forEach(btn => {
                btn.classList.remove('active');
                if (btn.innerText === (lang === 'ky' ? 'Кыргызча' : lang === 'ru' ? 'Русский' : 'O‘zbekcha')) {
                    btn.classList.add('active');
                }
            });
        }

        // Form submission
        function submitForm() {
            const name = document.getElementById('name').value;
            const phone = document.getElementById('phone').value;
            const workers = document.getElementById('workers').value;
            const location = document.getElementById('location').value;
            const t = translations[currentLang];

            if (name && phone && workers && location) {
                // Simulate saving to database
                console.log('Saving to database:', { name, phone, workers, location });

                // Send to WhatsApp
                const message = encodeURIComponent(
                    `${t.successMsg.replace('{name}', name).replace('{phone}', phone).replace('{workers}', workers).replace('{location}', location)}`
                );
                const whatsappUrl = `https://wa.me/+996221085348?text=${message}`;
                window.open(whatsappUrl, '_blank');

                alert(t.successMsg.replace('{name}', name).replace('{phone}', phone).replace('{workers}', workers).replace('{location}', location));
            } else {
                alert(t.errorMsg);
            }
        }

        // GSAP Animation
        gsap.from(".card", { duration: 1, y: 50, opacity: 0, ease: "power2.out" });
        gsap.from(".card > *", { duration: 0.8, y: 20, opacity: 0, stagger: 0.2, ease: "power2.out", delay: 0.3 });

        // Set default language
        changeLanguage('ky');
    </script>
</body>
</html>
