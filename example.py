from skill import analyze_log_skill

log1 = """
I qnn-net-run: Initializing QNN runtime
I qnn-net-run: Using backend: HTP
E QNN_HTP: qnn_htp_device_create failed
E QNN_HTP: Error code: QNN_STATUS_MEMORY_ALLOCATION_FAILED
E qnn-net-run: QNN inference failed
"""
log2 = """
I qnn-net-run: Initializing QNN runtime
I qnn-net-run: Using backend: HTP
I qnn-net-run: Loading model: model.dlc
I QNN_HTP: Creating QNN graph
E QNN_HTP: qnn_graph_create failed
E QNN_HTP: Error code: QNN_STATUS_MEMORY_ALLOCATION_FAILED
E qnn-net-run: Failed to prepare QNN graph
"""
log3 = """
I qnn-net-run: Initializing QNN runtime
I qnn-net-run: Using backend: HTP
I qnn-net-run: Loading model: model.dlc
I qnn-net-run: Preparing QNN graph
I qnn-net-run: Starting inference
E QNN_HTP: qnn_execute_graph failed
E QNN_HTP: Error code: QNN_STATUS_MEMORY_ALLOCATION_FAILED
E qnn-net-run: QNN inference failed during execution
"""





result1 = analyze_log_skill(log1)
result2 = analyze_log_skill(log2)
result3 = analyze_log_skill(log3)
print(result1)
print(result2)
print(result3)
# {'root_cause': 'HTP firmware memory fragmentation or insufficient system heap for HTP device creation', 'solutions': ['Ensure proper cleanup of previous QNN contexts', 'Reboot device to clear HTP memory fragmentation', 'Check system memory pressure before initializing QNN', 'Validate HTP firmware and driver compatibility'], 'confidence': 1.0}
# {'root_cause': 'Graph tensor count exceeds HTP capacity', 'solutions': ['Enable graph partitioning to split large graphs', 'Reduce input resolution or batch size', 'Apply operator fusion or pruning before export', 'Verify HTP supports all operators in the graph'], 'confidence': 1.0}
# {'root_cause': 'Runtime activation buffers exceed HTP memory', 'solutions': ['Fix input shapes and avoid dynamic dimensions', 'Reduce number of concurrent QNN sessions', 'Use lower precision (INT8) to reduce activation memory', 'Serialize inference execution to avoid memory contention'], 'confidence': 1.0}