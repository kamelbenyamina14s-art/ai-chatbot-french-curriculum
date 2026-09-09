العربية | [English](README_EN.md)

# تطبيق ذكاء اصطناعي للدردشة مع مراجع حديثة 🤖

تطبيق ذكي للدردشة مع الإجابة على الأسئلة بناءً على **المنهج الفرنسي** والمراجع الحديثة والموثوقة.

## المميزات ✨

- 💬 **دردشة ذكية** - محادثات طبيعية وذكية باستخدام GPT-4
- 📚 **مراجع حديثة** - استخدام مراجع موثوقة وحديثة في الإجابات
- 🇫🇷 **المنهج الفرنسي** - تتبع معايير وطريقة التعليم الفرنسي
- 🔍 **بحث ذكي** - البحث عن المراجع ذات الصلة تلقائياً
- 📖 **سياق تعليمي** - توفير السياق المنهجي للإجابات
- 🌐 **واجهة ويب** - واجهة سهلة الاستخدام

## المتطلبات 📋

- Python 3.8+
- مفتاح API من OpenAI
- pip (مدير الحزم)

## التثبيت 🛠️

### 1. استنساخ المستودع

```bash
git clone https://github.com/kamelbenyamina14s-art/ai-chatbot-french-curriculum.git
cd ai-chatbot-french-curriculum
```

### 2. إنشاء بيئة افتراضية

```bash
python -m venv venv

# في Windows
venv\Scripts\activate

# في Linux/Mac
source venv/bin/activate
```

### 3. تثبيت المكتبات

```bash
pip install -r requirements.txt
```

### 4. إعداد متغيرات البيئة

```bash
# نسخ ملف المثال
cp .env.example .env

# تعديل .env وإضافة مفتاح API الخاص بك
# OPENAI_API_KEY=sk-...
```

## الاستخدام 🚀

### تشغيل التطبيق

```bash
python main.py
```

يسيتم تشغيل التطبيق على `http://localhost:5000`

### استخدام API

#### إرسال رسالة

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "ما هو المنهج الفرنسي في تدريس الرياضيات؟"
  }'
```

**الاستجابة:**

```json
{
  "success": true,
  "message": "ما هو المنهج الفرنسي في تدريس الرياضيات؟",
  "response": "المنهج الفرنسي...",
  "references": [
    {
      "title": "المنهج الفرنسي والعلوم الحديثة",
      "summary": "تطبيق المنهج الفرنسي في تدريس العلوم والرياضيات",
      "url": "https://www.sesamath.net",
      "date": "2024",
      "type": "educational"
    }
  ],
  "sources": [...]
}
```

#### الحصول على المصادر المتاحة

```bash
curl http://localhost:5000/api/sources
```

#### فحص صحة التطبيق

```bash
curl http://localhost:5000/health
```

## هيكل المشروع 📁

```
ai-chatbot-french-curriculum/
├── main.py                      # التطبيق الرئيسي
├── chatbot.py                   # فئة روبوت المحادثة
├── references_manager.py        # مدير المراجع
├── french_curriculum.py         # المنهج الفرنسي
├── requirements.txt             # المكتبات المطلوبة
├── .env.example                 # متغيرات البيئة (نموذج)
└── README.md                    # هذا الملف
```

## المنهج الفرنسي 🎓

يغطي التطبيق الموضوعات التعليمية التالية:

1. **اللغة العربية** - القراءة، الكتابة، القواعس
2. **الرياضيات** - الجبر، الهندسة، الإحصاء
3. **العلوم** - الفيزياء، الكيمياء، الأحياء
4. **التاريخ والجغرافيا** - التطورات التاريخية والجغرافيا
5. **التربية المدنية** - المواطنة والديمقراطية
6. **الفنون** - الرسم، النحت، الموسيقى

## المراجع 📚

المصادر المستخدمة تشمل:

- مصادر حكومية فرنسية رسمية
- أبحاث أكاديمية معاصرة
- مواقع تعليمية موثوقة
- منصات تعليمية متخصصة

## المساهمة 🤝

نرحب بمساهماتكم! يرجى:

1. عمل fork للمشروع
2. إنشاء فرع للميزة الجديدة (`git checkout -b feature/AmazingFeature`)
3. التزام التغييرات (`git commit -m 'Add some AmazingFeature'`)
4. دفع إلى الفرع (`git push origin feature/AmazingFeature`)
5. فتح Pull Request

## الترخيص 📄

هذا المشروع مرخص تحت رخصة MIT - انظر ملف [LICENSE](LICENSE) للتفاصيل.

## التواصل 📞

- **البريد الإلكتروني**: kamelbenyamina14s-art@example.com
- **GitHub**: [@kamelbenyamina14s-art](https://github.com/kamelbenyamina14s-art)

## شكر خاص 👏

شكراً لـ:
- فريق OpenAI على GPT-4
- المنهج الفرنسي التعليمي
- المكتبات مفتوحة المصدر المستخدمة

---

صُنع بـ ❤️ من قبل Kamel Ben Yamina
