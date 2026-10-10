#include <cuda_runtime.h>

__global__ void outer_product_kernel(const float* a, const float* b, float* C, int M, int N) {
    // Write code here    
    int x_id = threadIdx.x + blockIdx.x * blockDim.x;
    int y_id = threadIdx.y + blockIdx.y * blockDim.y;

    if ((x_id < N) && (y_id < M)) 
        C[y_id * N + x_id] = a[y_id] * b[x_id];
}

extern "C" void solve(const float* a, const float* b, float* C, int M, int N) {
    dim3 threads(16, 16);
    dim3 blocks((N + 15) / 16, (M + 15) / 16);
    outer_product_kernel<<<blocks, threads>>>(a, b, C, M, N);
    cudaDeviceSynchronize();
}
