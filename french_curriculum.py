"""
فئة المنهج الفرنسي
توفر السياق التعليمي وفقاً للمنهج الفرنسي
"""

from typing import Dict, List

class FrenchCurriculum:
    def __init__(self):
        """تهيئة المنهج الفرنسي"""
        self.curriculum_topics = self._initialize_topics()
    
    def _initialize_topics(self) -> Dict:
        """تهيئة موضوعات المنهج الفرنسي"""
        return {
            'لغة_عربية': {
                'objectives': [
                    'تطوير مهارات القراءة والكتابة',
                    'فهم القواعد النحوية والصرفية',
                    'تحسين المحادثة والاستماع'
                ],
                'themes': ['الأدب', 'القواعس', 'الكتابة الإبداعية']
            },
            'رياضيات': {
                'objectives': [
                    'تطوير التفكير المنطقي',
                    'حل المسائل الرياضية',
                    'فهم المفاهيم الأساسية'
                ],
                'themes': ['الجبر', 'الهندسة', 'الإحصاء']
            },
            'علوم': {
                'objectives': [
                    'فهم الظواهر الطبيعية',
                    'اكتساب مهارات التجريب',
                    'التفكير العلمي'
                ],
                'themes': ['الفيزياء', 'الكيمياء', 'الأحياء']
            },
            'تاريخ_جغرافيا': {
                'objectives': [
                    'فهم التطورات التاريخية',
                    'معرفة الجغرافيا والمناخ',
                    'الوعي الجيوسياسي'
                ],
                'themes': ['التاريخ', 'الجغرافيا', 'العلاقات الدولية']
            },
            'تربية_مدنية': {
                'objectives': [
                    'تطوير المواطنة الصالحة',
                    'فهم القيم الديمقراطية',
                    'احترام حقوق الإنسان'
                ],
                'themes': ['الديمقراطية', 'الحقوق والواجبات', 'المجتمع']
            },
            'فنون': {
                'objectives': [
                    'تطوير الإبداع الفني',
                    'فهم الحركات الفنية',
                    'التعبير عن الذات'
                ],
                'themes': ['الرسم', 'النحت', 'الموسيقى']
            }
        }
    
    def get_context(self, query: str) -> str:
        """
        الحصول على السياق المنهجي للسؤال
        
        Args:
            query: السؤال أو الاستفسار
            
        Returns:
            السياق المنهجي الملائم
        """
        subject = self._identify_subject(query)
        
        if subject in self.curriculum_topics:
            context_data = self.curriculum_topics[subject]
            return self._build_context_string(subject, context_data)
        
        return ""
    
    def _identify_subject(self, query: str) -> str:
        """تحديد الموضوع من السؤال"""
        query_lower = query.lower()
        
        # البحث عن الموضوع المطابق
        for subject in self.curriculum_topics.keys():
            if any(word in query_lower for word in subject.split('_')):
                return subject
        
        # البحث بناءً على الكلمات الرئيسية
        keywords = {
            'رياضيات': ['عدد', 'حساب', 'معادلة', 'رسم بياني', 'جبر'],
            'علوم': ['جزيء', 'طاقة', 'تفاعل', 'حيوان', 'نبات'],
            'لغة_عربية': ['قصيدة', 'نصي', 'قواعد', 'نحو', 'كتابة'],
            'تاريخ_جغرافيا': ['تاريخ', 'حضارة', 'خريطة', 'جغرافيا', 'دول'],
            'تربية_مدنية': ['قانون', 'حقوق', 'واجبات', 'ديمقراطية', 'مجتمع']
        }
        
        for subject, keywords_list in keywords.items():
            if any(keyword in query_lower for keyword in keywords_list):
                return subject
        
        return ""
    
    def _build_context_string(self, subject: str, context_data: Dict) -> str:
        """بناء نص السياق"""
        context = f"\n### السياق المنهجي ({subject.replace('_', ' ')}):\n"
        
        context += "\n**الأهداف التعليمية:**\n"
        for objective in context_data['objectives']:
            context += f"- {objective}\n"
        
        context += "\n**المواضيع المرتبطة:**\n"
        for theme in context_data['themes']:
            context += f"- {theme}\n"
        
        return context
    
    def get_learning_standards(self, subject: str) -> List[str]:
        """الحصول على معايير التعلم لموضوع معين"""
        if subject in self.curriculum_topics:
            return self.curriculum_topics[subject]['objectives']
        return []
    
    def get_all_subjects(self) -> List[str]:
        """الحصول على جميع الموضوعات المتاحة"""
        return list(self.curriculum_topics.keys())
