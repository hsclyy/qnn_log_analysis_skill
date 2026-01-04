## QNN_STATUS_MEMORY_ALLOCATION_FAILED

### Typical Logs
- qnn_htp_device_create failed
- Error code: QNN_STATUS_MEMORY_ALLOCATION_FAILED

### Root Cause
- HTP memory insufficient
- Graph too large
- System heap pressure

### Solutions
1. Reduce model size or batch size
2. Use INT8 / FP16 model
3. Check SoC HTP memory config
4. Fallback to CPU/GPU for validation

## QNN_STATUS_MEMORY_ALLOCATION_FAILED (Graph Create)

### Typical Logs
- qnn_graph_create failed
- qnn_htp_graph_prepare failed
- Error code: QNN_STATUS_MEMORY_ALLOCATION_FAILED
- Failed during graph creation stage

### Root Cause
- Graph tensor count exceeds HTP capacity
- Large intermediate activation tensors
- Excessive constant weights loaded to HTP

### Solutions
1. Enable graph partitioning to split large graphs
2. Reduce input resolution or batch size
3. Apply operator fusion or pruning before export
4. Verify HTP supports all operators in the graph

## QNN_STATUS_MEMORY_ALLOCATION_FAILED (Inference Runtime)

### Typical Logs
- qnn_execute_graph failed
- qnn_htp_execute failed
- Error code: QNN_STATUS_MEMORY_ALLOCATION_FAILED
- Failure occurred during inference execution

### Root Cause
- Runtime activation buffers exceed HTP memory
- Dynamic input shapes cause unexpected buffer growth
- Concurrent QNN sessions consuming shared memory

### Solutions
1. Fix input shapes and avoid dynamic dimensions
2. Reduce number of concurrent QNN sessions
3. Use lower precision (INT8) to reduce activation memory
4. Serialize inference execution to avoid memory contention

## QNN_STATUS_MEMORY_ALLOCATION_FAILED (Device Initialization)

### Typical Logs
- qnn_htp_device_create failed
- qnn_backend_initialize failed
- Error code: QNN_STATUS_MEMORY_ALLOCATION_FAILED
- Failed to initialize HTP backend

### Root Cause
- HTP firmware memory fragmentation
- Previous QNN sessions not released properly
- Insufficient system heap for HTP device creation

### Solutions
1. Ensure proper cleanup of previous QNN contexts
2. Reboot device to clear HTP memory fragmentation
3. Check system memory pressure before initializing QNN
4. Validate HTP firmware and driver compatibility
