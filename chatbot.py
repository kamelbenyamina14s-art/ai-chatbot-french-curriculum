"""
فئة روبوت المحادثة الذكي
"""

import openai
from references_manager import ReferencesManager
from french_curriculum import FrenchCurriculum
from datetime import datetime

class AIChatterbot:
    def __init__(self, api_key, model='gpt-4', curriculum_type='french'):
        """
        تهيئة روبوت المحادثة
        
        Args:
            api_key: مفتاح API من OpenAI
            model: نموذج الذكاء الاصطناعي المستخدم
            curriculum_type: نوع المنهج (french, international, etc)
        """
        openai.api_key = api_key
        self.model = model
        self.curriculum_type = curriculum_type
        self.references_manager = ReferencesManager()
        self.curriculum = FrenchCurriculum()
        self.conversation_history = []
        
    def get_response(self, user_message):
        """
        الحصول على إجابة مع مراجع حديثة
        
        Args:
            user_message: رسالة المستخدم
            
        Returns:
            dict: يحتوي على الإجابة والمراجع والمصادر
        """
        # إضافة الرسالة إلى السجل
        self.conversation_history.append({
            'role': 'user',
            'content': user_message
        })
        
        # الحصول على مراجع ذات صلة
        relevant_references = self.references_manager.search(user_message)
        
        # بناء السياق من المنهج الفرنسي
        curriculum_context = self.curriculum.get_context(user_message)
        
        # بناء الرسالة النظامية
        system_prompt = self._build_system_prompt(curriculum_context, relevant_references)
        
        # استدعاء OpenAI API
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {'role': 'system', 'content': system_prompt},
                *self.conversation_history
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        assistant_message = response.choices[0].message.content
        
        # إضافة الإجابة إلى السجل
        self.conversation_history.append({
            'role': 'assistant',
            'content': assistant_message
        })
        
        return {
            'answer': assistant_message,
            'references': relevant_references,
            'sources': self._format_sources(relevant_references)
        }
    
    def _build_system_prompt(self, curriculum_context, references):
        """بناء رسالة النظام"""
        prompt = """أنت مساعد ذكي متخصص في الإجابة على الأسئلة بناءً على المنهج الفرنسي والمراجع الحديثة.

المبادئ الأساسية:
1. اجعل الإجابات واضحة ومنظمة
2. استخدم المراجع الموثوقة والحديثة
3. اتبع المنهج الفرنسي في الشرح والتنظيم
4. لا تتردد في الاعتراف بحدود معرفتك

السياق من المنهج الفرنسي:
"""
        prompt += curriculum_context if curriculum_context else "لا توجد معلومات منهجية محددة"
        
        prompt += "\n\nالمراجع الحديثة المتاحة:\n"
        for ref in references[:5]:  # أعلى 5 مراجع
            prompt += f"- {ref['title']}: {ref['summary']}\n"
        
        prompt += "\nيرجى تضمين المراجع في إجابتك حيثما أمكن."
        
        return prompt
    
    def _format_sources(self, references):
        """تنسيق المصادر للعرض"""
        sources = []
        for ref in references:
            sources.append({
                'title': ref['title'],
                'url': ref.get('url', ''),
                'date': ref.get('date', ''),
                'type': ref.get('type', 'article')
            })
        return sources
    
    def get_available_sources(self):
        """الحصول على قائمة المصادر المتاحة"""
        return self.references_manager.get_all_sources()
    
    def clear_history(self):
        """مسح سجل المحادثة"""
        self.conversation_history = []
