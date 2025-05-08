import math

def module5_function(inputs):
    """
    模組5：使用answer1和answer4進行計算
    
    Args:
        inputs: 包含answer1和answer4的字典
        
    Returns:
        包含answer7的字典
    """
    print("\n===== 模組5：計算 =====")
    answer1 = inputs["answer1"]
    answer4 = inputs["answer4"]
    
    # 計算: answer1 加上 answer4 的平方根
    if answer4 >= 0:
        answer7 = answer1 + math.sqrt(answer4)
    else:
        print("警告：無法計算負數的平方根，使用絕對值")
        answer7 = answer1 + math.sqrt(abs(answer4))
    
    print(f"模組5計算結果：answer7={answer7}")
    
    return {
        "answer7": answer7
    }