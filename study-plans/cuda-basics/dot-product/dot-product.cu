#include <cuda_runtime.h>
#define BLOCK_SIZE 256

__global__ void dot_kernel(const float* A, const float* B, float* result, int N) {
    // Write code here
    
    __shared__ float a_share[BLOCK_SIZE], b_share[BLOCK_SIZE];
    int tidx = threadIdx.x;
    int idx = blockIdx.x * blockDim.x + tidx;
    
    a_share[tidx] = (idx < N) ? A[idx] : 0 ;
    b_share[tidx] = (idx < N) ? B[idx] : 0 ;
    __syncthreads();
    a_share[tidx] *= b_share[tidx];
    __syncthreads();

    for (int stride = BLOCK_SIZE/2; stride; stride /= 2)
    {
        if (tidx < stride)
            a_share[tidx] += a_share[tidx + stride];
        __syncthreads();
    }
    if (tidx == 0) atomicAdd(result, a_share[0]);  
}

extern "C" void solve(const float* A, const float* B, float* result, int N) {
    int threads = BLOCK_SIZE;
    int blocks = (N + threads - 1) / threads;
    cudaMemset(result, 0, sizeof(float));
    dot_kernel<<<blocks, threads>>>(A, B, result, N);
    cudaDeviceSynchronize();
}
