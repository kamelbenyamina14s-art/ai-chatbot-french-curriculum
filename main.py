"""
تطبيق ذكاء اصطناعي للدردشة مع مراجع حديثة
يعتمد على المنهج الفرنسي
"""

import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import AIChatterbot

load_dotenv()

app = Flask(__name__)
CORS(app)

# تهيئة روبوت المحادثة
chatbot = AIChatterbot(
    api_key=os.getenv('OPENAI_API_KEY'),
    model=os.getenv('MODEL_NAME', 'gpt-4'),
    curriculum_type='french'
)

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    نقطة نهاية الدردشة الرئيسية
    تستقبل السؤال وترجع الإجابة مع المراجع
    """
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'الرسالة فارغة'}), 400
        
        # الحصول على الإجابة مع المراجع
        response = chatbot.get_response(user_message)
        
        return jsonify({
            'success': True,
            'message': user_message,
            'response': response['answer'],
            'references': response['references'],
            'sources': response['sources']
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/sources', methods=['GET'])
def get_sources():
    """
    الحصول على قائمة المصادر المتاحة
    """
    try:
        sources = chatbot.get_available_sources()
        return jsonify({
            'success': True,
            'sources': sources
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """فحص صحة التطبيق"""
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    debug_mode = os.getenv('DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
