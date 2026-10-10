#include <cuda_runtime.h>

__global__ void vector_sub(const float* A, const float* B, float* C, int N) {
    // Store N element-wise results in C; this kernel returns no value.
    int id = threadIdx.x + blockIdx.x * blockDim.x;
    if (id < N)
    {
        C[id] = A[id] - B[id];
    }
}

extern "C" void solve(const float* A, const float* B, float* C, int N) {
    int threads = 256;
    int blocks = (N + threads - 1) / threads;
    vector_sub<<<blocks, threads>>>(A, B, C, N);
    cudaDeviceSynchronize();
}