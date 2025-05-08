def module4_function(inputs):
    """
    模組4：使用answer2和answer3進行計算
    
    Args:
        inputs: 包含answer2和answer3的字典
        
    Returns:
        包含answer6的字典
    """
    print("\n===== 模組4：計算 =====")
    answer2 = inputs["answer2"]
    answer3 = inputs["answer3"]
    
    # 計算: answer2 除以 answer3
    if answer3 != 0:
        answer6 = answer2 / answer3
    else:
        print("警告：除數為零，使用預設值0")
        answer6 = 0
    
    print(f"模組4計算結果：answer6={answer6}")
    
    return {
        "answer6": answer6
    }