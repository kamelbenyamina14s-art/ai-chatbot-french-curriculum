"""
مدير المراجع والمصادر الحديثة
"""

import requests
from datetime import datetime, timedelta
from typing import List, Dict

class ReferencesManager:
    def __init__(self):
        """تهيئة مدير المراجع"""
        self.references = []
        self._load_references()
    
    def _load_references(self):
        """تحميل المراجع من مصادر متعددة"""
        # هذه قاعدة بيانات مثال - يمكن توسيعها
        self.references = [
            {
                'title': 'التعليم في فرنسا - النظام التعليمي الحديث',
                'summary': 'دراسة شاملة عن نظام التعليم الفرنسي المعاصر',
                'url': 'https://www.education.gouv.fr',
                'date': '2024',
                'type': 'official',
                'keywords': ['تعليم', 'منهج', 'فرنسا']
            },
            {
                'title': 'الذكاء الاصطناعي في التعليم',
                'summary': 'تطبيقات الذكاء الاصطناعي في المناهج الحديثة',
                'url': 'https://www.researchgate.net',
                'date': '2024',
                'type': 'research',
                'keywords': ['ذكاء اصطناعي', 'تعليم', 'تكنولوجيا']
            },
            {
                'title': 'اللغة العربية في المنهج الفرنسي',
                'summary': 'دراسة عن تعليم اللغة العربية في المدارس الفرنسية',
                'url': 'https://www.cairn.info',
                'date': '2023',
                'type': 'academic',
                'keywords': ['لغة عربية', 'منهج', 'فرنسا']
            },
            {
                'title': 'المنهج الفرنسي والعلوم الحديثة',
                'summary': 'تطبيق المنهج الفرنسي في تدريس العلوم والرياضيات',
                'url': 'https://www.sesamath.net',
                'date': '2024',
                'type': 'educational',
                'keywords': ['علوم', 'رياضيات', 'منهج فرنسي']
            },
            {
                'title': 'المهارات القرن الحادي والعشرين',
                'summary': 'تطوير المهارات الأساسية للقرن الحادي والعشرين',
                'url': 'https://www.atd-documentation.be',
                'date': '2023',
                'type': 'research',
                'keywords': ['مهارات', 'تعليم', 'مستقبل']
            }
        ]
    
    def search(self, query: str, limit: int = 5) -> List[Dict]:
        """
        البحث عن مراجع ذات صلة بالسؤال
        
        Args:
            query: نص البحث
            limit: عدد النتائج المطلوبة
            
        Returns:
            قائمة المراجع ذات الصلة
        """
        query_lower = query.lower()
        keywords = self._extract_keywords(query_lower)
        
        scored_references = []
        for ref in self.references:
            score = self._calculate_relevance_score(keywords, ref)
            if score > 0:
                scored_references.append((score, ref))
        
        # ترتيب حسب الدرجة
        scored_references.sort(key=lambda x: x[0], reverse=True)
        
        # إرجاع أعلى النتائج
        return [ref for score, ref in scored_references[:limit]]
    
    def _extract_keywords(self, text: str) -> List[str]:
        """استخراج الكلمات الرئيسية من النص"""
        # كلمات توقف عربية
        stop_words = ['في', 'من', 'إلى', 'عن', 'هو', 'هي', 'و', 'أو', 'لا', 'نعم']
        
        words = text.split()
        keywords = [w for w in words if w not in stop_words and len(w) > 2]
        return keywords
    
    def _calculate_relevance_score(self, keywords: List[str], reference: Dict) -> float:
        """حساب درجة الصلة بين البحث والمرجع"""
        score = 0
        ref_text = (reference['title'] + ' ' + reference['summary']).lower()
        
        for keyword in keywords:
            if keyword in ref_text:
                # النقاط الأعلى للكلمات في العنوان
                if keyword in reference['title'].lower():
                    score += 2
                else:
                    score += 1
        
        return score
    
    def add_reference(self, reference: Dict):
        """إضافة مرجع جديد"""
        reference['date'] = reference.get('date', str(datetime.now().year))
        self.references.append(reference)
    
    def get_all_sources(self) -> List[Dict]:
        """الحصول على جميع المصادر المتاحة"""
        return [
            {
                'title': ref['title'],
                'type': ref['type'],
                'date': ref['date']
            }
            for ref in self.references
        ]
    
    def update_references_from_web(self):
        """تحديث المراجع من مصادر الويب (اختياري)"""
        # هذا يمكن تطويره لسحب مراجع حديثة من الإنترنت
        pass
