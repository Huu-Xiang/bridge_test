# backend/routes.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backtest'))

from flask import Blueprint, request, jsonify
from backtest.backtest_engine import BacktestEngine
import os


api = Blueprint('api', __name__)

engine = BacktestEngine(os.getenv('TUSHARE_TOKEN'))  # 从环境变量获取token
results = {}

@api.route('/api/set_parameters', methods=['POST'])
def set_parameters():
    try:
        req_data = request.get_json()
        
        # 参数验证
        required_fields = ['ts_code', 'start_date', 'end_date']
        if not all(field in req_data for field in required_fields):
            return jsonify({'error': 'Missing required parameters'}), 400
        
        # 运行回测
        params = {
            'ts_code': req_data['ts_code'],
            'start_date': req_data['start_date'],
            'end_date': req_data['end_date'],
            'initial_cash': req_data.get('initial_cash', 1000000),
            'order_percentage': req_data.get('order_percentage', 0.2),
            'slippage': req_data.get('slippage', 0.0001)
        }
        
        global results
        results = engine.run_backtest(params)
        
        return jsonify({'status': 'success', 'data': results})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/api/get_results', methods=['GET'])
def get_results():
    return jsonify(results)
