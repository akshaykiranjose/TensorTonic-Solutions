#include <cuda_runtime.h>
#include <float.h>
#define BLOCK_SIZE 256

__global__ void max_kernel(const float* input, float* result, int N) {
    
    // Write code here
    int tidx = threadIdx.x;
    int idx = blockIdx.x * BLOCK_SIZE + threadIdx.x;

    __shared__ float sdata[BLOCK_SIZE];
    sdata[tidx] = (idx < N) ? input[idx] : -FLT_MAX ;
    __syncthreads();
    
    for (int stride = BLOCK_SIZE / 2; stride; stride /= 2)
    {
        if (tidx < stride)
             sdata[tidx] = max(sdata[tidx], sdata[tidx + stride]);
        __syncthreads();
    }
    if (tidx == 0)
    {
        float block_max = sdata[0];
        int* result_as_int = (int*) result;
        int old = *result_as_int;
        int assumed;
        do
        {   
            assumed = old;
            float new_max = fmaxf(__int_as_float(assumed), block_max);
            old = atomicCAS(result_as_int, assumed, __float_as_int(new_max));       
        } while (old != assumed);
    }    
}

extern "C" void solve(const float* input, float* result, int N) {
    int threads = BLOCK_SIZE;
    int blocks = (N + threads - 1) / threads;
    float neg_inf = -FLT_MAX;
    cudaMemcpy(result, &neg_inf, sizeof(float), cudaMemcpyHostToDevice);
    max_kernel<<<blocks, threads>>>(input, result, N);
    cudaDeviceSynchronize();
}
