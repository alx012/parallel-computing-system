import networkx as nx
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor, wait
from db_utils import fetch_answers, save_result

def build_dag(modules):
    """建構 DAG 並做排序"""
    dag = nx.DiGraph()
    answer_to_module = {}

    for module in modules:
        dag.add_node(module["id"])
        for out in module["outputs"]:
            answer_to_module[out] = module["id"]

    for module in modules:
        for req in module["requires"]:
            if req in answer_to_module:
                dag.add_edge(answer_to_module[req], module["id"])

    return dag, list(nx.topological_sort(dag))

def draw_dag(modules):
    """DAG 圖形繪製"""
    dag, _ = build_dag(modules)
    pos = nx.spring_layout(dag, seed=42)  # 可用 shell_layout、kamada_kawai_layout 等不同風格
    labels = {node: f"Module {node}" for node in dag.nodes()}
    
    plt.figure(figsize=(10, 6))
    nx.draw(dag, pos, with_labels=True, labels=labels, node_color="skyblue", 
            node_size=2000, font_size=10, font_weight="bold", arrows=True)
    plt.title("模組依賴圖（DAG）", fontsize=14)
    plt.show()

def run_module(module, inputs):
    """執行模組邏輯"""
    print(f"模組 {module['id']} 開始執行，需要: {module['requires']}")
    # 呼叫對應的模組函數
    result = module["generator"](inputs)
    print(f"模組 {module['id']} 完成，輸出: {result}")
    save_result(module["id"], result)

def execute_modules(modules):
    """根據 DAG 執行模組（支援平行）"""
    module_map = {m["id"]: m for m in modules}
    dag, _ = build_dag(modules)
    completed = set()
    pending = set(module_map.keys())

    while pending:
        ready = [mid for mid in pending if all(pred in completed for pred in dag.predecessors(mid))]
        with ThreadPoolExecutor() as executor:
            futures = []
            for mid in ready:
                module = module_map[mid]
                inputs = fetch_answers(module["requires"])
                futures.append(executor.submit(run_module, module, inputs))
                completed.add(mid)
            wait(futures)
        pending -= set(ready)