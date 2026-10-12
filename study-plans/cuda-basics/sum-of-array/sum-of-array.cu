#include <cuda_runtime.h>
#define BLOCK_SIZE 256

__global__ void sum_kernel(const float* input, float* result, int N) {
    // Write code here
    // cannot write it as __shared__ int sdata[blockDim.x];
    __shared__ float sdata[BLOCK_SIZE]; 

    int tidx = threadIdx.x;
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    sdata[tidx] = (idx < N) ? input[idx] : 0;
    __syncthreads();

    for (int stride = BLOCK_SIZE / 2; stride; stride /= 2)
    {
        if (tidx < stride) 
            sdata[tidx] += sdata[tidx + stride]; 
        __syncthreads();
    }

    if (tidx == 0) atomicAdd(result, sdata[tidx]);
}

extern "C" void solve(const float* input, float* result, int N) {
    int threads = BLOCK_SIZE;
    int blocks = (N + threads - 1) / threads;
    cudaMemset(result, 0, sizeof(float));
    sum_kernel<<<blocks, threads>>>(input, result, N);
    cudaDeviceSynchronize();
}
